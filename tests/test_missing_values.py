
import pytest
import numpy as np
import pandas as pd


# Creating the test data frame



frames = pd.DataFrame({'index': [1, 2, 3, 4], 'letters': ["a","b", "c","d"],
                   'numbers': [1, 2, 3, 4], 'booleans': [True, False, False, True]})

# Test that checks input is data frames

# Tests for the output missing_values data frame

#input is data frame


def test_correct_input():
    assert isinstance(frames, pd.DataFrame)


# test that variable is a string, missing_values is an integer and percent_missing is float

def test_column_type_integer_variable():
    assert np.issubdtype(frames['variable'].dtype, np.character)

def test_column_type_integer_missing_values():
    assert np.issubdtype(frames['missing_values'].dtype, np.number)

def test_column_type_float_size_in_percent_missing():
    assert np.issubdtype(frames['size_in_memory'].dtype, np.float)
