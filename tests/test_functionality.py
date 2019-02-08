
import pytest
import numpy as np
import pandas as pd


# Creating the test data frame that is in exploreR

data = np.array([['','letters','numbers','booleans'],
                ['1',"a",1,True],
                ['2',"b",2,False],
                ['3',"c",3,False],
                ['4',"d",4,True]])

frames = pd.DataFrame(data=data[1:,1:],    # values
        index=data[1:,0],    # 1st column as index
        columns=data[0,1:])  # 1st row as the column names


# Test that checks for missing values
