import numpy as np
import pandas as pd


def missing_values(x):
    """
    counts the number of missing values present in a data frame and reports back number and percent missing for each variable

    inputs:
    x: data frame

    returns:
    data frame - variables, count of missing values and proportion of values that are missing
    """

    return x.missing_values()
