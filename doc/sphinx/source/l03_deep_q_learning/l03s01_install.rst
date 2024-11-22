*******************************
Installer les outils logiciels 
*******************************



================================
Upgrader l'environnement conda
================================

.. code-block:: bash

   conda312_init
   conda activate rltutorials
   pip install swig
   pip install "gymnasium[all]"
   pip install torch

=======================
Testez l'installation
=======================

Téléchargez le tutoriel qui se présente sous la forme d'un notebook Jupyter et exécutez-le pour vérifier que tout fonctionne correctement (en appuyant sur le bouton ">>" de la barre d'outils de JupyterLab).

Téléchargez le fichier suivant en faisant (click droit puis "Enregistrer le lien sous...") :
:download:`Tutorial_Deep_Q_Learning.ipynb <resources/notebooks/Tutorial_Deep_Q_Learning.ipynb>`


========================================================
Utiliser google colab en cas de problème d'installation
========================================================

Si vous avez des problèmes d'installation, vous pouvez utiliser Google Colab pour exécuter le notebook Jupyter. 
Pour cela, il suffit d'ouvrir google colab dans un navigateur web:

* `https://colab.research.google.com/ <https://colab.research.google.com/>`_

Puis de faire 'File > Open notebook' et de coller l'URL suivante dans le champ 'GitHub' :
* `https://github.com/yguel/apprentissage_par_renforcement_et_simulation/blob/main/doc/sphinx/source/l03_deep_q_learning/resources/notebooks/Tutorial_Deep_Q_Learning.ipynb <https://github.com/yguel/apprentissage_par_renforcement_et_simulation/blob/main/doc/sphinx/source/l03_deep_q_learning/resources/notebooks/Tutorial_Deep_Q_Learning.ipynb>`_