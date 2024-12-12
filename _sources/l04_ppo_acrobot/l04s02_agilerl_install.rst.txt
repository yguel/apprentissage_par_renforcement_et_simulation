**********************************************************
Installer les packages python pour expérimenter avec PPO
**********************************************************

================================
Upgrader l'environnement conda
================================

.. code-block:: bash

   conda312_init
   conda activate rltutorials
   pip install imageio
   pip install agilerl
   pip install tqdm
   pip install ipywidgets

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

Téléchargez les fichiers suivants en faisant (click droit puis "Enregistrer le lien sous...") :

   * :download:`ppo_cartpoleV1_train.ipynb <resources/notebooks/ppo_cartpoleV1_train.ipynb>`
   * :download:`ppo_cartpoleV1_use.ipynb <resources/notebooks/ppo_cartpoleV1_use.ipynb>` 

Vous pouvez aussi récupérer un agent déjà entraîné pour le cartpole:

   * :download:`PPO_cartpole_trained_agent.pt <resources/notebooks/PPO_cartpole_trained_agent.pt>`