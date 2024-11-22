===============================
Comment gymnasium fonctionne ?
===============================

Documentation tirée de `gymnasium <https://gymnasium.farama.org/introduction/basic_usage/>`_.

.. figure:: resources/img/AE_loop.png
         :align: center
         :width: 30%


Dans l'apprentissage par renforcement, la boucle classique "agent-environnement" est une représentation simplifiée de l'interaction entre un agent et un environnement. 
L'agent reçoit une observation de l'environnement, sélectionne une action, que l'environnement utilise pour déterminer la récompense et la prochaine observation. 
Ce cycle se répète jusqu'à ce que l'environnement se termine (termine).

Pour Gymnasium, la boucle "agent-environnement" est implémentée comme suit pour un seul épisode (jusqu'à la fin de l'environnement).

.. literalinclude:: resources/code/gymnasium_loop.py
   :language: python
   :caption: Boucle agent-environnement pour un épisode avec Gymnasium
   :linenos:
   :emphasize-lines: 9, 11


À la ligne 9, une action est sélectionnée par l'agent et envoyée à l'environnement.
Gymnasium renvoie un tuple contenant l'observation, la récompense, un booléen indiquant si l'épisode est terminé parce qu'un état final est atteint, un booléen indiquant si l'épisode est terminé parce que l'horizon de temps est atteint et des informations supplémentaires stockées dans info.

L'épisode se termine lorsque soit un état final est atteint, soit l'horizon de temps est atteint, c'est-à-dire que l'un des deux booléens est True (ligne 11).
