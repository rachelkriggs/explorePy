import numpy as np
import pandas as pd



def size(x):
    """
    takes in a dataframe and prints the shape and size of the dataframe

    inputs:
    x: data frame

    returns:
    data frame - number of rows, number of columns and memory size of data frame
    """
    # Calculate the number of rows and columns
    number_of_rows = x.shape[0]
    number_of_columns = x.shape[1]

    # Get column-wise memory usuage and then
    # sum it to get total memory used
    total_bytes_used = sum(x.memory_usage())

    # Create the results dataframe
    result_df = pd.DataFrame({'rows': [number_of_rows],
                              'columns' : [number_of_columns],
                              'size_in_bytes' : [total_bytes_used]})

    return result_df
