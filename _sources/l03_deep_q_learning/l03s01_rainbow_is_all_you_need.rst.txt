.. _l03s01_rainbow_is_all_you_need:

############################
De DQN à Rainbow (TP 1 h 15)
############################

Le tutoriel `Rainbow is all you need <https://github.com/Curt-Park/rainbow-is-all-you-need>`_
décompose l'algorithme **Rainbow** en neuf chapitres : chacun part du DQN de base et lui
ajoute **une seule** amélioration, jusqu'à les combiner toutes.

Chaque chapitre est un notebook autonome qui entraîne un agent sur ``CartPole-v1``
(20 000 pas), trace la courbe d'apprentissage et produit une **vidéo** de la politique
apprise. Tout est préinstallé dans le docker du cours : vous n'avez rien à installer.

.. note::

   Ces notebooks sont écrits avec `marimo <https://marimo.io/>`_ et non avec Jupyter.
   Un notebook marimo est un fichier ``.py`` ordinaire, et il est **réactif** : quand vous
   modifiez une cellule, toutes celles qui en dépendent se ré-exécutent automatiquement.
   Il n'y a donc jamais d'état caché incohérent, mais **changer un hyperparamètre relance
   l'entraînement**. Réfléchissez à votre modification avant de la lancer.

===================
Avant de commencer
===================

Récupérer le script de lancement
---------------------------------

Ce TP utilise une version du script de lancement qui démarre aussi le serveur de notebooks.

.. code-block:: bash

   mkdir -p ~/rl/mujoco && cd ~/rl/mujoco && rm -f start.sh && wget -O start.sh https://raw.githubusercontent.com/yguel/docker_mujoco_rl_101/main/start.sh && chmod +x start.sh

.. tip::

   Ce script remplace celui que vous utilisiez jusqu'ici.

==========
Lancement
==========

.. code-block:: bash

   cd ~/rl/mujoco && ./start.sh

Le script vérifie l'image, la met à jour si besoin, puis démarre l'environnement. Au bout
d'une trentaine de secondes, il affiche le récapitulatif des services. Les trois doivent
être marqués ok (✅) comme ci-dessous :

.. code-block:: text

   Checking services status...
   ✅ VNC server is running
   ✅ noVNC is running
   ✅ Jupyter notebook is running
   ✅ marimo (Rainbow notebooks) is running
   ================================
   MuJoCo Desktop Environment Ready!
   ================================
   Access via:
     Desktop: http://localhost:6080
     Jupyter: http://localhost:8888
     Rainbow notebooks (marimo): http://localhost:2718

Si la ligne ``marimo`` porte un ``❌`` ou un ``⚠️``, reportez-vous au dépannage en fin de
page avant d'aller plus loin.

Vous avez alors trois accès, **dans votre propre navigateur** :

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Adresse
     - Contenu
   * - http://localhost:2718
     - **Les 9 chapitres du TP** (serveur marimo)
   * - http://localhost:6080
     - Le bureau Ubuntu complet (VS Code, terminal, MuJoCo)
   * - http://localhost:8888
     - Jupyter, pour les notebooks des séances précédentes

Pour ce TP, travaillez sur http://localhost:2718.

.. note::

   Depuis le bureau (http://localhost:6080) vous retrouvez aussi une icône
   **Rainbow Notebooks** et la commande ``start-rainbow.sh`` dans un terminal. C'est le
   même serveur : utilisez ce qui vous arrange.

Quand vous avez fini votre session de travail, fermez le docker proprement avec ``CTRL+C``
dans le terminal où le script a été lancé.

Vos fichiers
-------------

Au premier lancement, les neuf chapitres sont recopiés dans
``~/workspace/rainbow-is-all-you-need/`` (côté conteneur), c'est-à-dire dans votre workspace
persistant. C'est **cette** copie que vous modifiez et elle survit à l'arrêt du docker.


L'original reste intact dans ``/opt/rainbow-is-all-you-need/``. 

.. note:: Si vous cassez un notebook

  Vous pouvez à tout moment récupérer l'original, par exemple pour ``01_dqn.py`` se situant dans ``/opt``:

  .. code-block:: bash

    cp /opt/rainbow-is-all-you-need/01_dqn.py ~/workspace/rainbow-is-all-you-need/

================
Les 9 chapitres
================

.. list-table::
   :header-rows: 1
   :widths: 8 32 44 16

   * - #
     - Fichier
     - Brique ajoutée
     - Durée
   * - 01
     - ``01_dqn.py``
     - DQN : mémoire de rejeu + réseau cible
     - 25 s
   * - 02
     - ``02_double_q.py``
     - Double DQN : découple sélection et évaluation
     - 26 s
   * - 03
     - ``03_per.py``
     - Prioritized Experience Replay
     - 1 min 06
   * - 04
     - ``04_dueling.py``
     - Dueling Network : sépare :math:`V(s)` et :math:`A(s,a)`
     - 36 s
   * - 05
     - ``05_noisy_net.py``
     - NoisyNet : exploration apprise, remplace :math:`\varepsilon`-greedy
     - 33 s
   * - 06
     - ``06_categorical_dqn.py``
     - C51 : on apprend la **distribution** du retour
     - 33 s
   * - 07
     - ``07_n_step_learning.py``
     - Retours à :math:`n` pas
     - 31 s
   * - 08
     - ``08_rainbow.py``
     - **Rainbow** : les six briques combinées
     - 1 min 47
   * - 09
     - ``09_rainbow_iqn.py``
     - Rainbow + Implicit Quantile Networks
     - 3 min 20

Durées mesurées dans le conteneur du cours, sur 4 cœurs CPU et sans carte graphique :
**environ 9 min 30 de calcul pour les neuf chapitres**.

=====================
Déroulé de la séance
=====================

Vous n'aurez **pas** le temps de traiter les neuf chapitres en profondeur en 1 h 15. Le but
est de maîtriser le squelette (ch. 01), de comprendre comment on y greffe une amélioration
(ch. 02), puis de voir ce que donne l'assemblage complet (ch. 08). Les autres chapitres sont
à faire chez vous.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Temps
     - Activité
   * - 0 – 5 min
     - Lancement de ``./start.sh``, ouverture de http://localhost:2718.
   * - 5 – 10 min
     - **Lancez tout de suite le calcul de fond** (voir ci-dessous).
   * - 10 – 30 min
     - **Chapitre 01 — DQN.** Lisez, exécutez, regardez la vidéo. Questions Q1 à Q3.
   * - 30 – 45 min
     - **Chapitre 02 — Double DQN.** Comparez le code avec celui du 01. Questions Q4 et Q5.
   * - 45 – 65 min
     - **Chapitre 08 — Rainbow.** Lancez l'entraînement dès l'ouverture, lisez pendant qu'il tourne. Questions Q6 et Q7.
   * - 65 – 75 min
     - Comparaison des neuf courbes produites par le calcul de fond. Question Q8.

Le calcul de fond
------------------

Dès le début de la séance, ouvrez un terminal sur le bureau (http://localhost:6080) et
lancez :

.. code-block:: bash

   cd ~/workspace/rainbow-is-all-you-need
   for f in 0*.py; do echo "=== $f ==="; python3 "$f"; done

Les notebooks marimo étant de simples fichiers ``.py``, ils s'exécutent directement. En une
dizaine de minutes vous obtiendrez les vidéos et les courbes des neuf agents dans
``videos/``, que vous pourrez comparer en fin de séance sans rien attendre.

====================
Questions à rendre
====================

Déposez sur Moodle un fichier texte ou PDF avec vos réponses, quelques lignes chacune.

Chapitre 01 — DQN
------------------

#. **Q1.** Dans la classe ``DQNAgent``, deux réseaux coexistent : ``dqn`` et ``dqn_target``.
   Repérez où ``dqn_target`` est mis à jour. Que se passerait-il si on le mettait à jour à
   chaque pas plutôt que tous les ``target_update`` pas ?
#. **Q2.** ``epsilon_decay = 1 / 2000`` avec ``num_frames = 20000``. À partir de quel pas
   l'agent est-il essentiellement glouton ? Que voyez-vous sur la courbe à ce moment-là ?
#. **Q3.** Le score maximal atteignable est 200 (``max_episode_steps=200``). Votre agent
   l'atteint-il ? Est-il *stable* à 200 ou retombe-t-il ?

Chapitre 02 — Double DQN
-------------------------

#. **Q4.** Comparez la méthode ``_compute_dqn_loss`` des chapitres 01 et 02. Écrivez les
   deux formules de la cible. En quoi la seconde corrige-t-elle le biais d'optimisme ?
#. **Q5.** Sur CartPole, l'écart entre DQN et Double DQN est faible. Pourquoi ? Dans quel
   type d'environnement l'écart deviendrait-il important ?

Chapitre 08 — Rainbow
----------------------

#. **Q6.** Rainbow combine six améliorations. Lesquelles reconnaissez-vous dans le code ?
   Citez pour chacune la classe ou la ligne qui l'implémente.
#. **Q7.** NoisyNet remplace l'exploration :math:`\varepsilon`-greedy. Trouvez dans le code
   du chapitre 08 la preuve que ``epsilon`` a bien disparu de la boucle de décision.

Synthèse
---------

#. **Q8.** À partir des courbes des neuf chapitres, classez les améliorations de la plus
   utile à la moins utile **sur CartPole**. Cette conclusion est-elle transposable aux jeux
   Atari du papier Rainbow ? Justifiez en une ou deux phrases.

=====================
Pour aller plus loin
=====================

* Les chapitres 03 à 07, un par un : chacun isole une seule brique de Rainbow.
* Le chapitre 09 : Rainbow + IQN, la version distributionnelle la plus aboutie.
* Faites varier ``num_frames``, ``memory_size`` et ``batch_size`` dans le chapitre 01 et
  observez l'effet sur la courbe d'apprentissage.

==========
Dépannage
==========

.. dropdown:: http://localhost:2718 ne répond pas

   Vérifiez d'abord la ligne ``marimo (Rainbow notebooks)`` dans le récapitulatif affiché
   au démarrage.

   * ``⚠️`` : le serveur démarre encore, attendez dix secondes et rechargez la page.
   * ``❌`` : il n'a pas démarré. Ouvrez un terminal sur le bureau
     (http://localhost:6080) et lancez ``start-rainbow.sh`` pour voir l'erreur. Le journal
     est dans ``~/marimo.log``.

.. dropdown:: La ligne « marimo (Rainbow notebooks) » n'apparaît pas du tout

   Votre image docker est antérieure au tutoriel. Faites ``CTRL+C`` puis relancez
   ``./start.sh`` : il téléchargera la mise à jour (environ 60 Mo).

.. dropdown:: « workspace is not writable »

   Vos notebooks sont alors dans ``~/rainbow-is-all-you-need`` et **seront perdus** à
   l'arrêt du conteneur. Prévenez l'enseignant et sauvegardez vos réponses ailleurs
   en attendant.

.. dropdown:: Une fenêtre « Ubuntu Upgrade Available » apparaît sur le bureau

   Fermez-la, elle est sans effet sur le TP.

.. dropdown:: J'ai cassé un notebook

   .. code-block:: bash

      cp /opt/rainbow-is-all-you-need/01_dqn.py ~/workspace/rainbow-is-all-you-need/

===========
Références
===========

#. `V. Mnih et al., "Human-level control through deep reinforcement learning", Nature, 2015 <https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf>`_
#. `H. van Hasselt et al., "Deep Reinforcement Learning with Double Q-learning", 2015 <https://arxiv.org/pdf/1509.06461.pdf>`_
#. `T. Schaul et al., "Prioritized Experience Replay", 2015 <https://arxiv.org/pdf/1511.05952.pdf>`_
#. `Z. Wang et al., "Dueling Network Architectures for Deep Reinforcement Learning", 2015 <https://arxiv.org/pdf/1511.06581.pdf>`_
#. `M. Fortunato et al., "Noisy Networks for Exploration", 2017 <https://arxiv.org/pdf/1706.10295.pdf>`_
#. `M. G. Bellemare et al., "A Distributional Perspective on Reinforcement Learning", 2017 <https://arxiv.org/pdf/1707.06887.pdf>`_
#. `M. Hessel et al., "Rainbow: Combining Improvements in Deep Reinforcement Learning", 2017 <https://arxiv.org/pdf/1710.02298.pdf>`_
#. `W. Dabney et al., "Implicit Quantile Networks for Distributional Reinforcement Learning", 2018 <https://arxiv.org/pdf/1806.06923.pdf>`_
