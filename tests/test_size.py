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
from explorePy.size import size

# Dummy input DataFrame
frames = pd.DataFrame({'letters': ["a","b", np.nan,"d"],
                       'numbers': [1.0, 2.0, 3.0, np.nan],
                       'booleans': [np.nan, False, np.nan, True],
                       'dates': [np.datetime64("2003-01-02"), np.datetime64("2002-02-02"),
                                 np.datetime64("2004-03-03"), np.datetime64("2005-04-04")],
                       'integers': [2, 3, 4, 5]
                      })

# Let's get the output of our function with the test DataFrame
result_df = size(frames)

# Test to check if the input to our function is a DataFrame
def test_correct_input():
    assert isinstance(frames, pd.DataFrame), "Input is not DataFrame"

# Test to check output dimensions of DataFrame
def test_output_size():
    assert result_df.shape == (1,3), "The data frame should be 1 by 3"

# Test to check if the number of rows of the input DataFrame is reported as
# numeric
def test_column_type_numeric_rows():
    assert pd.api.types.is_numeric_dtype(result_df['rows']), "'rows' column data is not numeric"

# Test to check if the number of columns of the input DataFrame is reported as
# numeric
def test_column_type_numeric_columns():
    assert pd.api.types.is_numeric_dtype(result_df['columns']), "'columns' column data is not numeric"

# Test to check if the size in memory of the input DataFrame is reported as
# numeric
def test_column_type_numeric_size():
    assert pd.api.types.is_numeric_dtype(result_df['size_in_bytes']), "'size_in_bytes' column data is not numeric"
