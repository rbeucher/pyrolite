.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_plotting_stem.py:


Stem Plots
============

Stem plots are commonly used to visualise discrete distributions of data,
and are useful to highlight discrete observations where the precision of values along
one axis is high (e.g. an independent spatial measure like depth) and the other is less
so (such that the sampling frequency along this axis is important, which is not
emphasised by a scatter plot).


.. code-block:: default

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from pyrolite.plot import pyroplot
    from pyrolite.plot.stem import stem


    np.random.seed(82)







First let's create some example data:



.. code-block:: default

    x = np.linspace(0, 10, 10) + np.random.randn(10) / 2.0
    y = np.random.rand(10)
    df = pd.DataFrame(np.vstack([x, y]).T, columns=["Depth", "Fe3O4"])







A minimal stem plot can be constructed as follows:


.. code-block:: default

    ax = df.pyroplot.stem(color="k", figsize=(5, 3))



.. image:: /examples/plotting/images/sphx_glr_stem_001.png
    :class: sphx-glr-single-img





Stem plots can also be used in a vertical orientation, such as for visualising
discrete observations down a drill hole:



.. code-block:: default

    ax = df.pyroplot.stem(
        orientation="vertical",
        s=12,
        linestyle="--",
        linewidth=0.5,
        color="k",
        figsize=(3, 5),
    )
    # the yaxes can then be inverted using:
    ax.invert_yaxis()
    # and if you'd like the xaxis to be labeled at the top:
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")



.. image:: /examples/plotting/images/sphx_glr_stem_002.png
    :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  1.739 seconds)


.. _sphx_glr_download_examples_plotting_stem.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example


  .. container:: binder-badge

    .. image:: https://mybinder.org/badge_logo.svg
      :target: https://mybinder.org/v2/gh/morganjwilliams/pyrolite/develop?filepath=docs/source/examples/plotting/stem.ipynb
      :width: 150 px


  .. container:: sphx-glr-download

     :download:`Download Python source code: stem.py <stem.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: stem.ipynb <stem.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
