"""
Test for the feature_engineering_ function
"""
import unittest
import pandas as pd
from scripts.engineering.new_variables import creating_variables
from scripts.engineering.encoding import encoding_categorical


class TestCreatingVariables(unittest.TestCase):
    """
    Testing creating variables
    """
    def test_creating_variables(self):
        """
        Testing the creation code
        """
        df = pd.read_csv("FinalProject.csv")
        df_changed = creating_variables(df)
        self.assertNotEqual(
            len(df.columns),
            len(df_changed.columns),
            "Same number of columns",
        )

    def test_encoding_categorical(self):
        """
        Testing the encoding code
        """
        df2 = pd.read_csv("FinalProject.csv")
        df2_changed = df2.copy()
        df2_changed = encoding_categorical(df2_changed)
        df2.drop(
            columns=[
                "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
                "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2",
            ],
            inplace=True,
        )
        self.assertNotEqual(
            len(df2.columns),
            len(df2_changed.columns),
            "Same number of columns",
        )


if __name__ == "__main__":
    unittest.main()
