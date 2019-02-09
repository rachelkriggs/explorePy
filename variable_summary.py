import numpy as np
import pandas as pd



def variable_summary(x):
    """
    takes a data frame as input and provides the total quantity of each type of variable present in the data frame

    inputs:
    x: data frame

    returns:
    data frame - variable type and count of each type
    """
    return x.variable_summary()
