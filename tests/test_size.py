
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
    assert frames.shape == (1,3)


# test that rows is an integer and columns is an integer and size in memory is float

def test_column_type_integer_rows():
    assert np.issubdtype(frames['letters'].dtype, np.character)

def test_column_type_integer_columns():
    assert np.issubdtype(frames['columns'].dtype, np.number)

def test_column_type_float_size_in_memory():
    assert np.issubdtype(frames['size_in_memory'].dtype, np.float)
