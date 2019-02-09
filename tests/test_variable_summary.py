
import pytest
import numpy as np
import pandas as pd


# Creating the test data frame



frames = pd.DataFrame({'index': [1, 2, 3, 4], 'letters': ["a","b", "c","d"],
                   'numbers': [1, 2, 3, 4], 'booleans': [True, False, False, True]})

# Test that checks input is data frames

# Tests for the output size data frame

# input is data frame


def test_correct_input():
    assert isinstance(frames, pd.DataFrame)

#outputs are correct data frame dimensions

def test_output_size():
    assert frames.shape == (5,2)


# test that variable-type is an string and count is an integer

def test_column_type_integer_variable_type():
    assert np.issubdtype(frames['variable_type'].dtype, np.string)

def test_column_type_integer_variable_type():
    assert np.issubdtype(frames['variable_type'].dtype, np.character)
