***************************************
Installation d'un environnement MuJoCo
***************************************

#. Installation en utilisant docker. C'est la plus simple et qui marche sur windows, mac et linux.

Dans la salle de cours, docker est déjà installé sur les machines linux. Si vous êtes sur votre propre machine, suivez les instructions ci-dessous pour installer docker.

.. dropdown:: Comment installer Docker sur votre machine si besoin ?

   .. tab-set::

      .. tab-item:: Installer Docker sur Linux

         Pour installer docker sur linux, vous pouvez suivre les instructions officielles: `https://docs.docker.com/engine/install/ <https://docs.docker.com/engine/install/>`_.

      .. tab-item:: Installer Docker sur Windows

         Pour installer docker sur Windows, vous pouvez suivre les instructions officielles: `https://docs.docker.com/desktop/install/windows-install/ <https://docs.docker.com/desktop/install/windows-install/>`_.

      .. tab-item:: Installer Docker sur Mac

         Pour installer docker sur Mac, vous pouvez suivre les instructions officielles: `https://docs.docker.com/desktop/install/mac-install/ <https://docs.docker.com/desktop/install/mac-install/>`_.

Vous pouvez suivre les instructions ci-dessous en fonction de votre système d'exploitation.

.. tab-set::

   .. tab-item:: Docker pour Linux (machines de la salle de cours)

      #. Créer un dossier pour stocker les fichiers du cours, télécharger le script d'installation et le rendre exécutable:

         .. code-block:: bash

           mkdir -p ~/rl/mujoco && cd ~/rl/mujoco && wget -O start.sh https://raw.githubusercontent.com/yguel/docker_mujoco_rl_101/main/start.sh && chmod +x start.sh

      #. Lancez le script start.sh

         .. code-block:: bash

            cd ~/rl/mujoco && ./start.sh

      Quand vous avez fini votre session de travail, vous devez fermer le docker proprement en utilisant ``CTRL+C`` dans le terminal où le script a été lancé.

      Le script est codé de telle sorte que si vous ne pouvez pas avoir votre répertoire de travail (workspace) persistant (c'est-à-dire que docker ne peut pas monter lier un dossier à l'intérieur de votre répertoire HOME à un volume docker), un workspace temporaire sera créé dans /tmp/rl/mujoco/workspace. Quand vous fermer la session docker avec ``CTRL+C``, alors le script fera automatiquement une sauvegarde de ce workspace temporaire dans le dossier que vous avez indiqué dans la variable d'environnement ``BACKUP_TARGET_DIR`` (par défaut ``$HOME/rl/docker_snapshots/mujoco_snapshots``). |br|
      Cette configuration n'est pas idéale, mais elle se rencontre fréquemment sur des machines de l'école ou de l'université et en entreprise où les droits d'accès du daemon docker sont limités. |br|
      Dans ce cas lorsque vous souhaitez reprendre votre travail, il vous suffira de restaurer votre workspace en décompressant la dernière sauvegarde faite dans le dossier ``$HOME/rl/docker_snapshots/mujoco_snapshots`` dans le dossier ``/tmp/rl/mujoco/workspace``.
      |br|
      Si vous avez un doute sur le type de workspace que vous utilisez (temporaire ou persistant), vous pouvez vérifier dans le terminal où le script a été lancé, au début de la session docker, un message vous indique quel type de workspace est utilisé.

      Exemple d'un workspace temporaire:

      .. code-block:: bash
         :emphasize-lines: 11,13

         ================================
         MuJoCo Desktop Environment Ready!
         ================================
         Access via:
            Desktop: http://localhost:6080
            Jupyter: http://localhost:8888
            VNC Client: localhost:5901
            Security: No password (safe for local development)

         Workspace folder:
            Host: Temporary: /tmp/rl/mujoco (will be backed up on exit)
            Container: /home/student/workspace
            ⚠️  Using temporary workspace - will be backed up on exit to: /home/testuser/rl/docker_snapshots/mujoco_snapshots
         ================================

      Exemple d'un workspace persistant:
      
      .. code-block:: bash
         :emphasize-lines: 11

         ================================
         MuJoCo Desktop Environment Ready!
         ================================
         Access via:
            Desktop: http://localhost:6080
            Jupyter: http://localhost:8888
            VNC Client: localhost:5901
            Security: No password (safe for local development)

         Workspace folder:
            Host: Persistent: /home/<username>/rl/mujoco
            Container: /home/student/workspace
         ================================

         

      .. Dans ce cas lorsque vous souhaitez reprendre votre travail, il vous suffira de restaurer votre workspace en utilisant le :download:`script de restauration automatique <resources/scripts/restore_rl_env.py>`:

      ..    .. code-block:: bash

      ..       ./restore_rl_env.py

      .. qui par défaut restaurera la dernière sauvegarde faite dans le dossier ``$HOME/rl/docker_snapshots/mujoco_snapshots``.

      .. dropdown:: Si vous rencontrez des problèmes

         Si vous rencontrez des problèmes, voyez les paramètres avancés avec la commande help:
         
            .. code-block:: bash

               ./start.sh --help

         Vous pouvez aussi directement lancer le docker avec des options personnalisées, exemple sans accélération matérielle NVIDIA:

            .. code-block:: bash

               docker run -it --rm --name mujoco-student \
                  --shm-size=4g \
                  -p 6080:6080 \
                  -p 8888:8888 \
                  -v $HOME/rl/mujoco/workspace:/home/student/workspace \
                  -e HOST_UID=$(id -u) \
                  -e HOST_GID=$(id -g) \
                  -e HOST_WORKSPACE_INFO="Persistent: $HOME/rl/mujoco" \
                  -e USE_TEMP_WORKSPACE="false" \
                  -e BACKUP_TARGET_DIR="$HOME/rl/docker_snapshots/mujoco_snapshots" \
                  -e VNC_RESOLUTION=1920x1080 \
                  -e VNC_DEPTH=24 \
                  -e VNC_DPI=96 \
                  -e NOVNC_PORT=6080 \
                  -e VNC_PORT=5901 \
                  -e DISPLAY=:1 \
                  -e LIBGL_ALWAYS_SOFTWARE=1 \
                  -e MUJOCO_GL=osmesa \
                  yguel/mujoco-desktop:v1.0

         exemple avec accélération matérielle NVIDIA:

            .. code-block:: bash

               docker run -it --rm --name mujoco-student \
                  --shm-size=4g \
                  -p 6080:6080 \
                  -p 8888:8888 \
                  -v $HOME/rl/mujoco/workspace:/home/student/workspace \
                  -e HOST_UID=$(id -u) \
                  -e HOST_GID=$(id -g) \
                  -e HOST_WORKSPACE_INFO="Persistent: $HOME/rl/mujoco" \
                  -e USE_TEMP_WORKSPACE="false" \
                  -e BACKUP_TARGET_DIR="$HOME/rl/docker_snapshots/mujoco_snapshots" \
                  -e VNC_RESOLUTION=1920x1080 \
                  -e VNC_DEPTH=24 \
                  -e VNC_DPI=96 \
                  -e NOVNC_PORT=6080 \
                  -e VNC_PORT=5901 \
                  --runtime=nvidia \
                  -e NVIDIA_VISIBLE_DEVICES=all \
                  -e DISPLAY=:1 \
                  -e LIBGL_ALWAYS_SOFTWARE=0 \
                  yguel/mujoco-desktop:v1.0


         exemple avec un workspace temporaire (à sauvegarder manuellement à la fin de la session):

            .. code-block:: bash

               docker run -it --rm --name mujoco-student \
                  --shm-size=4g \
                  -p 6080:6080 \
                  -p 8888:8888 \
                  -v /tmp/rl/mujoco/workspace:/home/student/workspace \
                  -e HOST_UID=$(id -u) \
                  -e HOST_GID=$(id -g) \
                  -e HOST_WORKSPACE_INFO="Temporary: /tmp/rl/mujoco (will have to be backed up on exit)" \
                  -e USE_TEMP_WORKSPACE="true" \
                  -e BACKUP_TARGET_DIR="$HOME/rl/docker_snapshots/mujoco_snapshots" \
                  -e VNC_RESOLUTION=1920x1080 \
                  -e VNC_DEPTH=24 \
                  -e VNC_DPI=96 \
                  -e NOVNC_PORT=6080 \
                  -e VNC_PORT=5901 \
                  -e DISPLAY=:1 \
                  -e LIBGL_ALWAYS_SOFTWARE=1 \
                  -e MUJOCO_GL=osmesa \
                  yguel/mujoco-desktop:v1.0

         dans ce cas n'oubliez pas de sauvegarder votre workspace à la fin de la session en utilisant le :download:`script de sauvegarde automatique <resources/scripts/save_rl_env.sh>`:

            .. code-block:: bash

               ./save_rl_env.sh 

   .. tab-item:: Docker pour Windows

      Note importante, ces instructions n'ont pas été testées, elles sont fournies à titre indicatif.
      Merci de me faire un retour si vous les testez et rencontrez des problèmes ou au contraire si tout fonctionne bien.

      Dans la suite il faut remplacer ``<VotreNom>`` par votre nom d'utilisateur windows.

      #. Avec docker desktop installé, ouvrez une fenêtre powershell et créez un dossier pour stocker les fichiers du cours:

         .. code-block:: bash

            mkdir $HOME\rl\mujoco

      #. Si vous n'avez pas d'accélération matérielle NVIDIA, lancer l'image docker manuellement en liant le dossier créé précédemment, en alouant les ports pour jupyter et noVNC, et alouant suffisamment de mémoire (ici 4Go, mais ne mettez pas plus de la moitié de la mémoire totale de votre machine):

         .. code-block:: bash

            docker run -it --rm --name mujoco-student `
               --shm-size=4g `
               -p 6080:6080 `
               -p 8888:8888 `
               -v C:\Users\<VotreNom>\rl\mujoco\workspace:/home/student/workspace `
               -e HOST_WORKSPACE_INFO="Persistent: C:\Users\<VotreNom>\rl\mujoco" `
               -e USE_TEMP_WORKSPACE="false" `
               -e BACKUP_TARGET_DIR="C:\Users\<VotreNom>\rl\docker_snapshots\mujoco_snapshots" `
               -e VNC_RESOLUTION=1920x1080 `
               -e VNC_DEPTH=24 `
               -e VNC_DPI=96 `
               -e NOVNC_PORT=6080 `
               -e VNC_PORT=5901 `
               -e DISPLAY=:1 `
               -e LIBGL_ALWAYS_SOFTWARE=1 `
               -e MUJOCO_GL=osmesa `
               yguel/mujoco-desktop:v1.0

      #. Si vous avez une carte graphique NVIDIA compatible avec l'accélération matérielle dans docker, vous pouvez lancer l'image docker avec les options supplémentaires suivantes (à ajouter avant le nom de l'image yguel/mujoco-desktop:v1.0):

         .. code-block:: bash

            docker run -it --rm --name mujoco-student `
               --shm-size=4g `
               -p 6080:6080 `
               -p 8888:8888 `
               -v C:\Users\<VotreNom>\rl\mujoco\workspace:/home/student/workspace `
               --runtime=nvidia `
               -e NVIDIA_VISIBLE_DEVICES=all `
               -e HOST_WORKSPACE_INFO="Persistent: C:\Users\<VotreNom>\rl\mujoco" `
               -e USE_TEMP_WORKSPACE="false" `
               -e BACKUP_TARGET_DIR="C:\Users\<VotreNom>\rl\docker_snapshots\mujoco_snapshots" `
               -e VNC_RESOLUTION=1920x1080 `
               -e VNC_DEPTH=24 `
               -e VNC_DPI=96 `
               -e NOVNC_PORT=6080 `
               -e VNC_PORT=5901 `
               -e DISPLAY=:1 `
               -e LIBGL_ALWAYS_SOFTWARE=0 `
               yguel/mujoco-desktop:v1.0
   


==========================================
Premières vérifications de l'installation
==========================================

#. Dans une autre fenêtre de navigateur, ouvrez l'URL suivante: `http://localhost:8888 <http://localhost:8888>`_. Vous devriez voir une interface jupyter.

#. Dans une autre fenêtre de navigateur, ouvrez l'URL suivante: `http://localhost:6080 <http://localhost:6080>`_. Vous devriez voir une fenêtre NO VNC, vous n'avez plus qu'à cliquer pour vous connecter et vous devriez voir un bureau linux comme sur la :numref:`fig_docker_ubuntu_start` ci-dessous:

   .. figure:: resources/img/docker_ok.gif
      :name: fig_docker_ubuntu_start
      :align: center

      Interface graphique utilisant un navigateur pour interagir avec le docker  yguel/mujoco-desktop:v1.0 sous ubuntu avec noVNC.

#. Dans cette dernière fenêtre, vous pouvez maintenant ouvrir un terminal et exécuter les vérifications suivantes.

Assurez-vous que vous utilisez le navigateur web du docker (celui ouvert avec l'URL `http://localhost:6080 <http://localhost:6080>`_) pour faire les vérifications suivantes (cela sera beaucoup plus pratique pour copier/coller les commandes et télécharger les fichiers au bon endroit).
Le navigateur devrait normalement être ouvert à la page suivante: 'https://yguel.github.io/apprentissage_par_renforcement_et_simulation/l01_introduction_with_mujoco/l01s01_installation_mujoco.html#premiere-verification-de-l-installation'.

Pour faire une première vérification que l'installation de MuJoCo s'est bien passée, télécharger le fichier :download:`test_mujoco_gl.py <resources/mujoco_python/test_install/test_mujoco_gl.py>`.

vous pouvez exécuter la commande suivante dans un terminal qui place le fichier dans le dossier `~/rl/mujoco/workspace/examples` et l'exécute:

.. code-block:: bash

   mv ~/Downloads/test_mujoco_gl.py ~/workspace/examples/ && cd ~/workspace/examples && python3 test_mujoco_gl.py