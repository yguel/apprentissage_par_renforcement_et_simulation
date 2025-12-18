#!/usr/bin/env bash
set -euo pipefail

SUDO="sudo -H -E"
export DEBIAN_FRONTEND=noninteractive

# --- Detect CUDA from torch (best signal for what extensions will build against) ---
CUDA_VER="$(python3 - <<'PY'
import torch
print(torch.version.cuda or "")
PY
)"

if [ -z "$CUDA_VER" ]; then
  echo "[INFO] CPU-only torch detected. Installing agilerl without DeepSpeed CUDA ops."
  $SUDO DS_BUILD_OPS=0 DS_BUILD_AIO=0 DS_BUILD_SPARSE_ATTN=0 \
    python3 -m pip install --break-system-packages agilerl
  exit 0
fi

CUDA_MAJOR="${CUDA_VER%%.*}"
CUDA_MINOR="${CUDA_VER#*.}"
echo "[INFO] torch CUDA version: $CUDA_VER (major=$CUDA_MAJOR minor=$CUDA_MINOR)"

# --- If nvcc already exists, skip toolkit install ---
if command -v nvcc >/dev/null 2>&1; then
  echo "[INFO] nvcc already present: $(command -v nvcc)"
else
  echo "[INFO] nvcc not found. Installing CUDA toolkit via apt..."

  # Base deps
  $SUDO apt-get update
  $SUDO apt-get install -y --no-install-recommends \
    ca-certificates curl gnupg lsb-release software-properties-common

  # Identify OS
  . /etc/os-release
  echo "[INFO] OS: ${ID:-unknown} ${VERSION_ID:-unknown} (${VERSION_CODENAME:-unknown})"

  # Install NVIDIA CUDA repository keyring (Ubuntu/Debian)
  # This is the supported way to add the CUDA apt repository.
  if [ "${ID:-}" = "ubuntu" ]; then
    # e.g. 22.04 -> ubuntu2204, 24.04 -> ubuntu2404
    UB_VER="${VERSION_ID//./}"     # "2204"
    KEYRING_URL="https://developer.download.nvidia.com/compute/cuda/repos/ubuntu${UB_VER}/x86_64/cuda-keyring_1.1-1_all.deb"
  elif [ "${ID:-}" = "debian" ]; then
    # e.g. 12 -> debian12
    DEB_VER="${VERSION_ID}"
    KEYRING_URL="https://developer.download.nvidia.com/compute/cuda/repos/debian${DEB_VER}/x86_64/cuda-keyring_1.1-1_all.deb"
  else
    echo "[ERROR] Unsupported distro ID='${ID:-}'. This script supports ubuntu/debian containers."
    exit 1
  fi

  echo "[INFO] Installing cuda-keyring from: $KEYRING_URL"
  tmpdeb="$(mktemp --suffix=.deb)"
  curl -fsSL "$KEYRING_URL" -o "$tmpdeb"
  $SUDO dpkg -i "$tmpdeb"
  rm -f "$tmpdeb"

  $SUDO apt-get update

  # Install the toolkit matching torch CUDA (e.g., cuda-toolkit-12-1)
  TOOLKIT_PKG="cuda-toolkit-${CUDA_MAJOR}-${CUDA_MINOR}"
  echo "[INFO] Installing package: $TOOLKIT_PKG"
  if ! $SUDO apt-get install -y --no-install-recommends "$TOOLKIT_PKG"; then
    echo "[WARN] $TOOLKIT_PKG not available. Trying fallback: cuda-toolkit-${CUDA_MAJOR}"
    $SUDO apt-get install -y --no-install-recommends "cuda-toolkit-${CUDA_MAJOR}"
  fi
fi

# --- Set CUDA_HOME (NVIDIA packages typically create these paths) ---
if [ -d "/usr/local/cuda-${CUDA_MAJOR}.${CUDA_MINOR}" ]; then
  export CUDA_HOME="/usr/local/cuda-${CUDA_MAJOR}.${CUDA_MINOR}"
elif [ -d "/usr/local/cuda" ]; then
  export CUDA_HOME="/usr/local/cuda"
else
  echo "[ERROR] CUDA toolkit installed but CUDA_HOME path not found under /usr/local."
  echo "        Checked: /usr/local/cuda-${CUDA_MAJOR}.${CUDA_MINOR} and /usr/local/cuda"
  exit 1
fi

export PATH="$CUDA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$CUDA_HOME/lib64:$CUDA_HOME/lib:${LD_LIBRARY_PATH:-}"

echo "[INFO] CUDA_HOME=$CUDA_HOME"
echo "[INFO] nvcc: $(command -v nvcc || true)"
nvcc --version || true

# --- Install agilerl (keep Debian pip/setuptools/wheel as-is; do NOT upgrade them) ---
echo "[INFO] Installing agilerl (with dependencies)..."
$SUDO python3 -m pip install --break-system-packages agilerl

echo "[OK] Done."
