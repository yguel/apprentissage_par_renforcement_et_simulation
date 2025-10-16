***************************************************
Pratiquons avec MuJoCo et l'environnement corridor
***************************************************

Assurez-vous que vous utilisez le navigateur web du docker (celui ouvert avec l'URL `http://localhost:6080 <http://localhost:6080>`_) pour faire les vérifications suivantes (cela sera beaucoup plus pratique pour copier/coller les commandes et télécharger les fichiers au bon endroit).
Dans ce navigateur ouvrez cette page: 'https://yguel.github.io/apprentissage_par_renforcement_et_simulation/l01_introduction_with_mujoco/l01s02_corridor_101.html'.

=================
Premier exercice 
=================

Télécharger les fichiers suivants dans le dossier `~/rl/mujoco/workspace/t00_corridor`

.. code-block:: bash

   mkdir -p ~/rl/mujoco/workspace/t00_corridor && cd ~/rl/mujoco/workspace/t00_corridor

#. :download:`corridor_3x100.xml <resources/mujoco_python/corridor_101/corridor_3x100.xml>`
#. :download:`t00_corridor.py <resources/mujoco_python/corridor_101/t00_corridor.py>`

Ouvrez le fichier `t00_corridor.py` et complétez le code pour réaliser les 3 exercices suivants:

#. Afficher l'environnement dans une fenêtre graphique
#. Utilisez le clavier pour afficher les paramètres de la caméra
#. Modifier les paramètres de la caméra pour avoir une bonne vue du couloir au démarrage

Pour exécuter le code il vous suffit de lancer la commande suivante dans un terminal:

.. code-block:: bash

   cd ~/rl/mujoco/workspace/t00_corridor && python3 t00_corridor.py

Pour valider l'exercice 3, vous devez fermer la fenêtre graphique et relancer la commande, la vue de la caméra doit être correcte au démarrage.