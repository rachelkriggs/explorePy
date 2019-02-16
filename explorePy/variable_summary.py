import numpy as np
import pandas as pd



def variable_summary2(frames):
    """
    takes a data frame as input and provides the total quantity of each type of variable present in the data frame
    inputs:
    frames: data frame
    returns:
    data frame - variable type and count of each type
    """
    #https://stackoverflow.com/questions/19900202/how-to-determine-whether-a-column-variable-is-numeric-or-not-in-pandas-numpy
    #pandas data types
    #https://pbpython.com/pandas_dtypes.html

    #holds the list of values of the column names
    cols = list(frames.columns.values)
    #holds the number for column length
    col_len = len(cols)

    #holds the number of columns of each variable type

    int_count = 0
    char_count = 0
    bool_count = 0
    date_count = 0
    other_count = 0

    for i in range (0, col_len):
        if frames[cols[i]].dtype == np.int64:
        #if np.issubdtype(frames[cols[i]].dtype, np.number) == True:
            int_count = int_count + 1
        elif frames[cols[i]].dtype == np.object:
            char_count = char_count + 1
        elif frames[cols[i]].dtype == np.bool:
            bool_count = bool_count + 1
        elif frames[cols[i]].dtype == np.datetime64:
            date_count = date_count + 1
        else:
            other_count = other_count + 1
    print(char_count)

    result_df = pd.DataFrame({'rows': "count",
                                  'columns' : [int_count],
                                  'size_in_byes' : [char_count]})



    data3 = pd.DataFrame({'Variable type': ["numeric","character", "boolean","date","other"], 'count': [int_count, char_count, bool_count, date_count,other_count] })



    #print out a data frame

    print(data3)
