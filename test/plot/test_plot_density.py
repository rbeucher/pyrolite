import unittest
import matplotlib.pyplot as plt
import matplotlib.axes
import pandas as pd
import numpy as np
from numpy.random import multivariate_normal
import logging
from pyrolite.plot.density import density


logger = logging.getLogger(__name__)


class TestDensityplot(unittest.TestCase):
    """Tests the Densityplot functionality."""

    def setUp(self):
        self.cols = ["MgO", "SiO2", "CaO"]
        data = np.array([0.5, 0.4, 0.3])
        cov = np.array([[2, -1, -0.5], [-1, 2, -1], [-0.5, -1, 2]])

        self.biarr = multivariate_normal(data[:2], cov[:2, :2], 100)
        self.triarr = multivariate_normal(data, cov, 100)

        self.biarr[0, 1] = np.nan
        self.triarr[0, 1] = np.nan

    def test_none(self):
        """Test generation of plot with no data."""
        for arr in [np.empty(0)]:
            with self.subTest(arr=arr):
                out = density(arr)
                self.assertTrue(isinstance(out, matplotlib.axes.Axes))
                plt.close("all")

    def test_one(self):
        """Test generation of plot with one record."""

        for arr in [self.biarr[0, :], self.triarr[0, :]]:
            with self.subTest(arr=arr):
                out = density(arr)
                self.assertTrue(isinstance(out, matplotlib.axes.Axes))
                plt.close("all")

    def test_multiple(self):
        """Test generation of plot with multiple records."""
        for arr in [self.biarr, self.triarr]:
            with self.subTest(arr=arr):
                out = density(arr)
                self.assertTrue(isinstance(out, matplotlib.axes.Axes))
                plt.close("all")

    def test_modes(self):  #
        """Tests different ploting modes."""
        for arr in [self.biarr, self.triarr]:
            with self.subTest(arr=arr):
                for mode in ["density", "hist2d", "hexbin"]:
                    with self.subTest(mode=mode):
                        out = density(arr, mode=mode)
                        self.assertTrue(isinstance(out, matplotlib.axes.Axes))
                        plt.close("all")

    def test_bivariate_logscale(self):  #
        """Tests logscale for different ploting modes using bivariate data."""
        arr = self.biarr
        with np.errstate(invalid="ignore"): # ignore for tests
            arr[arr < 0] = np.nan
        for logspacing in [(True, True), (False, False), (False, True), (True, False)]:
            lx, ly = logspacing
            with self.subTest(logx=lx, logy=ly):
                for mode in ["density", "hist2d", "hexbin"]:
                    with self.subTest(mode=mode):
                        out = density(arr, mode=mode, logx=lx, logy=ly)
                        self.assertTrue(isinstance(out, matplotlib.axes.Axes))
                        plt.close("all")

    def tearDown(self):
        plt.close("all")


if __name__ == "__main__":
    unittest.main()