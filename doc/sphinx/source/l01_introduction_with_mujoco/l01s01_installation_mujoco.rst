***************************************
Installation d'un environnement MuJoCo
***************************************

#. Installation en utilisant docker. C'est la plus simple et qui marche sur windows, mac et linux.

.. tab-set::

   .. tab-item:: Docker pour linux

      #. Créer un dossier pour stocker les fichiers du cours

         .. code-block:: bash

            mkdir -p ~/rl/mujoco

      #. Télécharger le fichier :download:`start.sh <resources/scripts/start.sh>` et placez le dans le dossier `~/rl/mujoco`

      #. Rendez le script start.sh exécutable:

         .. code-block:: bash
            cd ~/rl/mujoco && chmod +x start.sh

      #. Lancez le script start.sh

         .. code-block:: bash

            cd ~/rl/mujoco && ./start.sh

      #. Dans une autre fenêtre de navigateur, ouvrez l'URL suivante: `http://localhost:8888 <http://localhost:8888>`_. Vous devriez voir une interface jupyter.

      #. Dans une fenêtre de navigateur, ouvrez l'URL suivante: `http://localhost:6080 <http://localhost:6080>`_. Vous devriez voir une fenêtre NO VNC, vous n'avez plus qu'à cliquer pour vous connecter et vous devriez voir un bureau linux.

      #. Dans cette dernière fenêtre, vous pouvez maintenant ouvrir un terminal et exécuter les vérifications.
   

========================================
Première vérification de l'installation
========================================

Pour faire une première vérification que l'installation de MuJoCo s'est bien passée, vous pouvez exécuter la commande suivante dans un terminal:

.. code-block:: bash

   cd ~/workspace/examples && python3 mujoco_example.py