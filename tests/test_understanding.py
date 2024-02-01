import unittest
from click.testing import CliRunner
from scripts.understanding import main

class TestScript(unittest.TestCase):
    def test_understanding_option(self):
        runner = CliRunner()
        result = runner.invoke(main, ['--understanding'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Dataset Overview:', result.output)
        self.assertIn('Number of rows:', result.output)
        self.assertIn('Number of columns:', result.output)
        self.assertIn('Columns and data types:', result.output)
        self.assertIn('Column Names:', result.output)
        self.assertIn('Description:', result.output)
        self.assertIn('Unique Values per Column:', result.output)
        self.assertIn('Missing Values per Column:', result.output)
        self.assertIn('Example of Unique Values per Column:', result.output)
        self.assertIn('Sample of Data:', result.output)

if __name__ == '__main__':
    unittest.main()
