import os
import unittest


class TestFunctions(unittest.TestCase):
    """
    Script to test the exploratory analysis encoded
    """

    def test_plot_general_distributions(self):
        """
        Test if plot_correlations function generates directory
        """
        self.assertTrue(os.path.exists("exploring_data"))

    def test_plot_general_distributions_directory2(self):
        """
        Test if plot_correlations function generates directory
        """
        self.assertTrue(os.path.exists("exploring_data/general"))

    def test_plot_general_distributions_files(self):
        """
        Test if plot_correlations function generates files
        """
        files = os.listdir("exploring_data/general")
        self.assertTrue(len(files) > 0, "No files found.")


if __name__ == "__main__":
    unittest.main()
