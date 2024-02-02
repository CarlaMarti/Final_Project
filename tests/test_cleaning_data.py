import unittest
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Importa las funciones que necesitan ser probadas
from scripts.cleaning.duplicates import deal_with_duplicates
from scripts.cleaning.irrelevant import delete_last_two_columns
from scripts.cleaning.mistaken import mistakendata
from scripts.cleaning.nulos import eliminar_nulos
from scripts.cleaning.outliers import outliersfunction
from scripts.cleaning.repeated import repeated_values


class TestCleaningDataFunctions(unittest.TestCase):
    """
    Test para las funciones de limpieza de datos
    """

    def setUp(self):
        """
        Prepara los datos de prueba
        """
        self.df = pd.DataFrame(
            {
                "CLIENTNUM": [1, 2, 3, 4, 5],
                "Dependent_count": [2, 3, -1, 1, 4],
                "Columna1": [10, 20, 30, 40, 50],
                "Columna2": [15, 25, 35, 45, 55],
                "Gender": ["male", "female", "male", "female", "male"],
            }
        )

    def test_deal_with_duplicates(self):
        """
        Prueba la función deal_with_duplicates
        """
        df_cleaned = deal_with_duplicates(self.df.copy())
        self.assertEqual(len(df_cleaned), len(self.df.drop_duplicates("CLIENTNUM")))

    def test_delete_last_two_columns(self):
        """
        Prueba la función delete_last_two_columns
        """
        df_cleaned = delete_last_two_columns(self.df.copy())
        self.assertEqual(len(df_cleaned.columns), len(self.df.columns) - 2)

    def test_mistakendata(self):
        """
        Prueba la función mistakendata
        """
        df_cleaned = mistakendata(self.df.copy())
        self.assertFalse((df_cleaned["Dependent_count"] < 0).any())

    def test_eliminar_nulos(self):
        """
        Prueba la función eliminar_nulos
        """
        df_cleaned = eliminar_nulos(self.df.copy())
        self.assertFalse(df_cleaned.isnull().any().any())

    def test_images_downloaded(self):
        """
        Prueba la función outliersfunction
        """
        df_cleaned = outliersfunction(self.df.copy())

        assert os.path.exists(
            "outliers/before"
        ), "Folder 'outliers/before' does not exist"
        assert os.path.exists(
            "outliers/after"
        ), "Folder 'outliers/after' does not exist"

        before_images = os.listdir("outliers/before")
        after_images = os.listdir("outliers/after")

        assert len(before_images) > 0, "No images found in 'outliers/before' folder"
        assert len(after_images) > 0, "No images found in 'outliers/after' folder"

        print("Images downloaded successfully!")

    def test_repeated_values(self):
        """
        Prueba la función repeated_values
        """
        df_cleaned = repeated_values(self.df.copy())
        self.assertEqual(len(df_cleaned["Gender"].unique()), 2)


if __name__ == "__main__":
    unittest.main()
