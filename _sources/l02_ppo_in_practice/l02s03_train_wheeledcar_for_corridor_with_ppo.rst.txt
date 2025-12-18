**************************************************************
Entraîner l'algorithme PPO à piloter le robot dans le couloir
**************************************************************

====================
Travail à effectuer
====================

Pour ce projet, il faut entraîner un agent PPO à piloter un robot à roues différentielles dans un couloir en utilisant le simulateur MuJoCo. Le robot doit être capable d'avancer dans le couloir en évitant les obstacles (murs, bosses, trous) qui peuvent se trouver sur son chemin. 
Les étapes à réaliser sont les suivantes:

#. Il faut créer un environnement d'apprentissage par renforcement de type Gym en utilisant le simulateur MuJoCo et en particulier définir les fonctions ``step`` et ``reset`` de l'environnement.
   Cet environnement pourra être défini dans un fichier ``corridor_env.py``.
   Plusieurs options sont possibles pour définir les actions et les observations de l'environnement.
   Le choix le plus simple est définir:

   * les actions comme étant un couple (v, omega) où v est la vitesse linéaire du robot et omega sa vitesse angulaire. Pour cela il faudra convertir (v, omega) en vitesses des roues gauches et droites du robot.
   * les observations comme étant:
   
      #. la position (x,y) et l'orientation (theta) du robot dans le couloir.
      #. une carte discrétisée du couloir autour du robot (par exemple une grille 24x24 où chaque cellule indique la présence ou non d'un mur, d'une bosse ou d'un trou pour une discrétisation de 0.25cm).

   * Il faut définir une fonction de récompense adaptée pour entraîner l'agent à piloter le robot dans le couloir. Celle qui sera utilisée dans la fonction ``step`` de l'environnement.
     Par exemple, on peut définir une récompense positive lorsque le robot avance dans le couloir et une récompense négative lorsqu'il heurte un mur ou une bosse et une récompense très négative lorsqu'il tombe dans un trou.
     On peut aussi définir une récompense négative proportionnelle à la distance entre le robot et les obstacles les plus proches (murs, bosses, trous).

#. Il faut ensuite entraîner un agent PPO en utilisant l'environnement défini précédemment en adaptant une implémentation de PPO. Pour cela, on peut utiliser :

   * l'implémentation de référence de PPO vue dans le cours issue de la bibliothèque ``cleanrl``.
   * l'implémentation de PPO disponible dans la bibliothèque AgileRL.

   Pour toutes ces implémentations il existe des exemples d'entraînement d'agents PPO sur des environnements Gym standards (CartPole, Acrobot, etc.) qui pourront être adaptés pour entraîner l'agent dans l'environnement défini précédemment. Tenez également compte de l'utilisation d'une carte qu'on peut assimiler à une image (utilisation de réseaux de neurones convolutifs).
   
   Créez un script ``ppo_corridor_train.py`` qui entraîne l'agent PPO dans l'environnement défini précédemment.
   
#. Une fois l'agent entraîné, il faut évaluer ses performances en le testant dans l'environnement et en visualisant son comportement (par exemple en utilisant la fonction ``render`` de l'environnement Gym).
   Créez un script ``ppo_corridor_use.py`` qui teste l'agent PPO entraîné dans l'environnement défini précédemment et visualise son comportement.

========================================
Note: Programmation modulaire en python
========================================

Pour ce projet, il est recommandé d'adopter une approche de programmation modulaire en python en séparant les différentes parties du code dans des fichiers distincts:

* L'environnement Gym dans un fichier ``corridor_env.py``.
* Le script d'entraînement de l'agent PPO dans un fichier ``ppo_corridor_train.py``.
* Le script de test de l'agent PPO dans un fichier ``ppo_corridor_use.py``.

Chaque fichier est importable en python en utilisant la commande ``import``. 
Exemple depuis le script ``ppo_corridor_train.py``:   

.. code-block:: python

   from corridor_env import CorridorEnv # importer l'environnement Gym

Pour que l'interpréteur python puisse trouver les fichiers à importer, il faut s'assurer que le répertoire courant (celui où se trouvent les scripts) est bien dans la variable d'environnement ``PYTHONPATH``.
Cela peut être fait en lançant le script depuis le répertoire où se trouvent les fichiers ou en ajoutant le répertoire courant au ``PYTHONPATH`` avant de lancer le script:

.. code-block:: bash

   export PYTHONPATH=$PYTHONPATH:.
   python ppo_corridor_train.py
