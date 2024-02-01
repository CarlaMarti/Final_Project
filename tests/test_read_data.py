import unittest
from click.testing import CliRunner
import pandas as pd
from scripts.read_data import main

class TestMainFunction(unittest.TestCase):

    def test_read_data_option(self):
        runner = CliRunner()
        result = runner.invoke(main, ['--read_data'])
        self.assertEqual(result.exit_code, 0)  # Verificar que el código de salida sea 0
        self.assertIn("You will now read the dataset!", result.output)  # Verificar que el mensaje de lectura aparezca
        self.assertIn("You have read the dataset!", result.output)  # Verificar que el mensaje de lectura exitosa aparezca

        # Verificar que se haya impreso el dataframe
        df = pd.read_csv("Dataset.csv", sep=',')  # Leer el dataframe original
        original_output = df.to_string()  # Convertir el dataframe original a string
        self.assertIn(original_output, result.output)  # Verificar que el dataframe impreso sea igual al original

if __name__ == '__main__':
    unittest.main()
