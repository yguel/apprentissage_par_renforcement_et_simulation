**********************************************************
Installer les packages python pour jouer contre un agent
**********************************************************

================================
Upgrader l'environnement conda
================================

.. code-block:: bash

   conda312_init
   conda activate rltutorials
   conda install -c conda-forge jupyterlab
   conda install swig
   pip install "gymnasium[all]"
   pip install torch
   conda install 'pettingzoo[all]'
   pip install imageio agilerl tqdm ipywidgets

Installer les `ROMs <https://github.com/Farama-Foundation/AutoROM>`_ (l'usage est limité).

.. code-block:: bash
   
   pip install "autorom[accept-rom-license]"


.. ======================
.. Tester l'installation
.. ======================