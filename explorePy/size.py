import numpy as np
import pandas as pd



def size(x):
    """
    takes in a dataframe and prints the shape and size of the dataframe

    inputs:
    x: data frame

    returns:
    data frame - number of rows, number of columns and memory size of data frame

    example usage:

    Using this toy data_frame
    frames = pd.DataFrame({'names': ["Rachel","Jim", "Arzan","Milos"],
                           'numbers': [2, 4, 6, 8],
                           'truths': [True, True, True, False],
                          })

    size(frames)    
    """
    # Calculate the number of rows and columns
    try:
        number_of_rows = x.shape[0]
        number_of_columns = x.shape[1]

        # Get column-wise memory usuage and then
        # sum it to get total memory used
        total_bytes_used = sum(x.memory_usage())
    except AttributeError:
        print("Error: Input to function needs to be a dataframe")


    try:
        # Create the results dataframe
        result_df = pd.DataFrame({'rows': [number_of_rows],
                                  'columns' : [number_of_columns],
                                  'size_in_bytes' : [total_bytes_used]})
        return result_df
    except UnboundLocalError:
        print("Error: Cannot create results dataframe")
