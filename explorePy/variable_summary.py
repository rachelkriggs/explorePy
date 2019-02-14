import numpy as np
import pandas as pd


def variable_summary(frames):
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

    cols = list(frames.columns.values)
    col_len = len(cols)


    cols2 = frames.shape[1]

    int_count = 0
    char_count = 0
    bool_count = 0
    date_count = 0
    other_count = 0

    for i in range (0, col_len):
        if frames[cols[i]].dtype == np.int64:
        #if np.issubdtype(frames[cols[i]].dtype, np.number) == True:
            int_count = int_count + len(frames[cols[i]])
        elif frames[cols[i]].dtype == np.object:
            char_count = char_count + len(frames[cols[i]])
        elif frames[cols[i]].dtype == np.bool:
            bool_count = bool_count + len(frames[cols[i]])
        elif frames[cols[i]].dtype == np.datetime64:
            date_count = date_count + len(frames[cols[i]])
        else:
            other_count = other_count + len(frames[cols[i]])
    print(char_count)

    result_df = pd.DataFrame({'rows': "count",
                                  'columns' : [int_count],
                                  'size_in_byes' : [char_count]})

    #I left this option to maybe print out a np array
    data2 = np.array([['variable type','count'],
                    ['numeric',int_count],
                    ['character',char_count],
                    ['boolean',bool_count],
                    ['date',date_count],
                    ['other',other_count]])

    #or print out
    frames2 = pd.DataFrame(np.atleast_2d(data2))
    print(frames2)
    return frames.variable_summary()
