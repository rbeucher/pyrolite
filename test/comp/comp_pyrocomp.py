import unittest
import numpy as np
import pyrolite.comp
from pyrolite.util.synthetic import test_df
from pyrolite.geochem.ind import REE

np.random.seed(81)


class TestPyroComp(unittest.TestCase):
    def setUp(self):
        self.cols = ["MgO", "SiO2", "CaO"]

        # can run into interesting singular matrix errors with bivariate random data
        self.tridf = test_df(cols=self.cols, index_length=100)
        self.bidf = self.tridf.loc[:, self.cols[:2]]
        self.multidf = test_df(cols=REE(), index_length=100)

    def test_renormalise_default(self):
        df = self.bidf.copy(deep=True) * 100  # copy df
        df["SiO2"] += 50  # modify df
        dfval = df["SiO2"].values[0]
        out = df.pyrocomp.renormalise()  # renorm
        self.assertTrue(df["SiO2"].values[0] == dfval)  # check original hasn't changed
        self.assertTrue((np.allclose(out.sum(axis=1), 100.0)))  # check output

    def test_renormalise_components(self):
        df = self.tridf.copy(deep=True) * 100  # copy df
        out = df.pyrocomp.renormalise(components=self.cols[:2])  # renorm
        self.assertTrue(
            (np.allclose(out[self.cols[:2]].sum(axis=1), 100.0))
        )  # check output

    def test_ALR_default(self):
        df = self.tridf.copy(deep=True)  # copy df
        out = df.pyrocomp.ALR()
        self.assertTrue(hasattr(out, "alr_index"))
        self.assertTrue(hasattr(out, "inverts_to"))
        self.assertTrue(out.inverts_to == self.cols)

    def test_ALR_name_index(self):
        df = self.tridf.copy(deep=True)  # copy df
        ind = "SiO2"
        out = df.pyrocomp.ALR(ind=ind)
        self.assertTrue(hasattr(out, "alr_index"))
        self.assertTrue(hasattr(out, "inverts_to"))
        self.assertTrue(all([ind in colname for colname in out.columns]))
        self.assertTrue(out.inverts_to == self.cols)

    def test_inverse_ALR_default(self):
        df = self.tridf.copy(deep=True)  # copy df
        intermediate = df.pyrocomp.ALR()
        out = intermediate.pyrocomp.inverse_ALR()
        self.assertTrue((out.columns == self.cols).all())
        self.assertTrue(np.allclose(out, df))

    def test_CLR_default(self):
        df = self.tridf.copy(deep=True)  # copy df
        out = df.pyrocomp.CLR()
        self.assertTrue(hasattr(out, "inverts_to"))
        self.assertTrue(out.inverts_to == self.cols)

    def test_inverse_CLR_default(self):
        df = self.tridf.copy(deep=True)  # copy df
        intermediate = df.pyrocomp.CLR()
        out = intermediate.pyrocomp.inverse_CLR()
        self.assertTrue((out.columns == self.cols).all())
        self.assertTrue(np.allclose(out, df))

    def test_ILR_default(self):
        df = self.tridf.copy(deep=True)  # copy df
        out = df.pyrocomp.ILR()
        self.assertTrue(hasattr(out, "inverts_to"))
        self.assertTrue(out.inverts_to == self.cols)

    def test_inverse_ILR_default(self):
        df = self.tridf.copy(deep=True)  # copy df
        intermediate = df.pyrocomp.ILR()
        out = intermediate.pyrocomp.inverse_ILR()
        self.assertTrue((out.columns == self.cols).all())
        self.assertTrue(np.allclose(out, df))

    def test_boxcox_default(self):
        df = self.tridf.copy(deep=True)  # copy df
        out = df.pyrocomp.boxcox()
        self.assertTrue(hasattr(out, "boxcox_lmbda"))

    def test_inverse_boxcox_default(self):
        df = self.tridf.copy(deep=True)  # copy df
        intermediate = df.pyrocomp.boxcox()
        out = intermediate.pyrocomp.inverse_boxcox()
        self.assertTrue((out.columns == self.cols).all())
        self.assertTrue(np.allclose(out, df))

    def test_logratiomean_default(self):
        df = self.tridf.copy(deep=True)  # copy df
        out = df.pyrocomp.logratiomean()


if __name__ == "__main__":
    unittest.main(argv=[""], exit=False)
