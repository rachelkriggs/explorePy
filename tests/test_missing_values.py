
import pytest
import numpy as np
import pandas as pd


# Creating the test data frame



frames = pd.DataFrame({'index': [1, 2, 3, 4], 'letters': ["a","b", "c","d"],
                   'numbers': [1, 2, 3, 4], 'booleans': [True, False, False, True]})

# Test that checks input is data frames

# Tests for the output missing_values data frame

#input is data frame


def test_correct_input(x):
    assert isinstance(x, pd.DataFrame),  "Input is not a pandas data frame"


# test that variable is a string, missing_values is an integer and percent_missing is float

def test_column_type_integer_variable(x):
    assert np.issubdtype(x['variable'].dtype, np.character),"Input is not a pandas data frame"

def test_column_type_integer_missing_values(x):
    assert np.issubdtype(x['missing_values'].dtype, np.int64), "missing vales column should be a number"

def test_column_type_float_size_in_percent_missing(x):
    assert np.issubdtype(x['size_in_memory'].dtype, np.int64), "size in memory column should be a number"
