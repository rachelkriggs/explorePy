
import pytest
import numpy as np
import pandas as pd


# Creating the test data frame



frames = pd.DataFrame({'index': [1, 2, 3, 4], 'letters': ["a","b", "c","d"],
                   'numbers': [1, 2, 3, 4], 'booleans': [True, False, False, True]})

# Test that checks input is data frames

# Tests for the output size data frame

# input is data frame


def test_correct_input(x):
    assert isinstance(x, pd.DataFrame), "The input is not a data frame"

#outputs are correct data frame dimensions

def test_output_size(x):
    assert x.shape == (1,3), "The data frame should be 1 by 3"


# test that rows is an integer and columns is an integer and size in memory is float

def test_column_type_integer_rows(x):
    assert np.issubdtype(x['letters'].dtype, np.object), "letters column should be an object type"

def test_column_type_integer_columns(x):
    assert np.issubdtype(x['columns'].dtype, np.int64), "letters column should be an integer type"

def test_column_type_float_size_in_memory(x):
    assert np.issubdtype(x['size_in_memory'].dtype, np.float64),"size_in_memory column should be an integer type"
