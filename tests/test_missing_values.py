import pytest
import numpy as np
import pandas as pd
import os
import sys

# By default, python only searches for packages and modules to import
# from the directories listed in sys.path
# The idea is to add another path that inlcudes the function we want to test
# This allows us to import that function
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath("./explorePy"))))

# Now that we have added the path, we can import the function we want to test
from explorePy.missing_values import missing_values

# Dummy input DataFrame
frames = pd.DataFrame({'letters': ["a","b", np.nan,"d"],
                       'numbers': [1.0, 2.0, 3.0, np.nan],
                       'booleans': [np.nan, False, np.nan, True],
                       'dates': [np.datetime64("2003-01-02"), np.datetime64("2002-02-02"),
                                 np.datetime64("2004-03-03"), np.datetime64("2005-04-04")],
                       'integers': [2, 3, 4, 5]
                      })

# Let's get the output of our function with the test DataFrame
result_df = missing_values(frames)


# Test to check if the input to our function is a DataFrame
def test_correct_input():
    assert isinstance(frames, pd.DataFrame), "Input is not DataFrame"

# Test to check if the data type of the first column of the output DataFrame
# is string
def test_first_column_is_string():
    assert pd.api.types.is_string_dtype(result_df['columns']), "1st column data type is not string"

# Test to check if the data type of the second column of the output DataFrame
# is numeric
def test_second_column_is_numeric():
    assert pd.api.types.is_numeric_dtype(result_df['no_of_missing_vals']), "2nd column data type is not numeric"

# Test to check if the data type of the third column of the output DataFrame
# is numeric
def test_third_column_is_numeric():
    assert pd.api.types.is_numeric_dtype(result_df['perecent_missing_vals']), "3rd column data type is not numeric"
