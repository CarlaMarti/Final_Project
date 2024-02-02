import os
import unittest


class TestFunctions(unittest.TestCase):
    """
    Script to test the exploratory analysis encoded
    """

    def test_plot_correlations_directory(self):
        """
        Test if plot_correlations function generates directory
        """
        self.assertTrue(os.path.exists("correlations"))

    def test_plot_correlations_files(self):
        """
        Test if plot_correlations function generates files
        """
        files = os.listdir("correlations")
        self.assertTrue(len(files) > 0, "No files found in 'correlations' folder")

    def test_graphs_directory(self):
        """
        Test if graphs function generates directory
        """
        self.assertTrue(os.path.exists("graphs"))

    def test_graphs_files(self):
        """
        Test if graphs function generates files
        """
        files = os.listdir("graphs")
        self.assertTrue(len(files) > 0, "No files found in 'graphs' folder")


if __name__ == "__main__":
    unittest.main()
