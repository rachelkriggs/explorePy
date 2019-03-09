import numpy as np
import pandas as pd
import datetime


def variable_summary(frames):
    """
    takes a data frame as input and provides the total quantity of each type of variable present in the data frame

    inputs:
    frames: data frame

    returns:
    data frame - variable type and count of each type

    example usage:

    Using this toy data_frame
    frames = pd.DataFrame({'names': ["Rachel","Jim", "Arzan","Milos"],
                           'numbers': [2, 4, 6, 8],
                           'truths': [True, True, True, False],
                          })

    variable_summary(frames)    
    """

    try:
        #holds the list of values of the column names
        cols = list(frames.columns.values)
        #holds the number for column length
        col_len = len(cols)
    except AttributeError:
        print("Error: Input to function must be a dataframe")

    #holds the number of columns of each variable type

    int_count = 0
    char_count = 0
    bool_count = 0
    date_count = 0
    other_count = 0

    try:
        # performs the count
        for i in range (0, col_len):
            if frames[cols[i]].dtype == np.int64 or frames[cols[i]].dtype == np.float:
                int_count = int_count + 1
            elif type(frames[[cols[i]]].dropna().values[0][0]) == str:
                char_count = char_count + 1
            elif type(frames[[cols[i]]].dropna().values[0][0]) == np.bool:
                bool_count = bool_count + 1
            elif (type(frames[[cols[i]]].dropna().values[0][0]) == np.datetime64 or type(frames[cols[i]][0]) == pd._libs.tslibs.timestamps.Timestamp):
                date_count = date_count + 1
            else:
                other_count = other_count + 1

        # Create results dataframe
        result_df = pd.DataFrame({'variable_type': ["numeric","string", "boolean","date","other"], 'count': [int_count, char_count, bool_count, date_count,other_count] })

        #print out a data frame of the summary results
        return(result_df)
    except UnboundLocalError:
        print("Error: Could not count types of variables")
