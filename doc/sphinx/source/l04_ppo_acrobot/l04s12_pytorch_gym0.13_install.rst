**********************************************************
Installer les packages python pour expérimenter avec PPO
**********************************************************

================================
Upgrader l'environnement conda
================================

.. code-block:: bash

   conda312_init
   conda activate rltutorials
   conda install tensordict 
   pip install torchrl tqdm

======================
Tester l'installation
======================

En lançant JupyterLab

Soit dans la même console que celle où vous avez lancé la dernière commande (``pip install agilerl``):

.. code-block:: bash

   jupyter lab

Soit dans une nouvelle console, lancez:

.. code-block:: bash

   conda312_init
   conda activate rltutorials
   jupyter lab

Télecharger le jupyter notebook pour expérimenter avec PPO: