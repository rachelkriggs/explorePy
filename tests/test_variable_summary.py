
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
    assert x.shape == (5,2), "The data frame should be 1 by 3"


# test that variable-type is an string and count is an integer

def test_column_type_integer_variable_type(x):
    assert np.issubdtype(x['variable_type'].dtype, np.object), "variable_type column should be an object type"

def test_column_type_integer_count(x):
    assert np.issubdtype(x['count'].dtype, np.int64), "count column should be an integer type"
