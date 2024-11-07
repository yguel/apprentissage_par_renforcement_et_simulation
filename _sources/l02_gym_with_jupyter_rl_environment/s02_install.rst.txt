*******************************
Installer les outils logiciels
*******************************

=================
Installer conda
=================

Télécharger et installer Miniconda :

.. code-block:: bash

   mkdir -p ~/system/python/anaconda
   cd ~/system/python/anaconda
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda3-latest-2024.09.sh
   bash Miniconda3-latest-2024.09.sh -b -u -p miniconda312
   rm Miniconda3-latest-2024.09.sh

Ajouter le bout de code qui suit à votre fichier de configuration du shell ``~/.bashrc``:

.. literalinclude:: resources/code/conda312_init_bashrc
   :language: bash
   :caption: Fonction pour lancer facilement conda depuis la console
   :linenos:

===========================================
Installer OpenAI Gym et Jupyter avec conda
===========================================

.. code-block:: bash

   conda312_init
   conda create -n rltutorials
   conda activate rltutorials
   conda install -c conda-forge jupyterlab
   pip install rlberry[torch]
   pip install gym

======================
Tester l'installation
======================

En lançant JupyterLab

Soit dans la même console que celle où vous avez lancé la dernière commande (``pip install gym``):

.. code-block:: bash

   jupyter lab

Soit dans une nouvelle console, lancez:

.. code-block:: bash

   conda312_init
   conda activate rltutorials
   jupyter lab

Cela doit ouvrir une nouvelle fenêtre ou un nouvel onglet de navigateur avec JupyterLab, comme sur l'image ci-dessous:

.. image:: resources/img/jupyterlab.png
   :width: 800px
   :align: center
   :alt: JupyterLab