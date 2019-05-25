import numpy as np
import pandas as pd


def missing_values(x):
    """
    Counts the number of missing values present in a data frame
    and reports back the number and percent of missing for each variable(column)

    inputs:
    x: data frame

    returns:
    data frame - variables, count of missing values and proportion of values that are missing

    example usage:

    Using this toy data_frame
    frames = pd.DataFrame({'names': ["Rachel","Jim", "Arzan","Milos"],
                           'numbers': [2, 4, 6, 8],
                           'truths': [True, True, True, False],
                          })

    missing_values(frames)
    """

    # Create an empty list to store the count and percentages of NAs in each column
    number_of_nas = []
    percent_of_nas = []


    try:
        # Get the toal number of rows
        total_rows_df = x.shape[0]

        # Let's get the name of the columns in each dataframe
        name_of_columns = x.columns
    except AttributeError:
        print("Error: Input to function should be a dataframe")


    try:
        # Loop through each column, count the number of NAs and append it to the list.
        for i in name_of_columns:

            # Total number of NA's in the column
            total_nas = sum(x[i].isnull())

            # Percent of NA's in the column
            percent_nas = round(total_nas/total_rows_df,4)

            # Append values to list.
            number_of_nas.append(total_nas)
            percent_of_nas.append(percent_nas)


        # Create the dataframe to report the results
        result_df = pd.DataFrame()
        result_df["columns"] = name_of_columns
        result_df["no_of_missing_vals"] = number_of_nas
        result_df["perecent_missing_vals"] = percent_of_nas

        return result_df

    except UnboundLocalError:
        print("Error: Cannot create results dataframe.")
