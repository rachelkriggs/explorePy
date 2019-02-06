# explorePy

#### A Collaborative Software Development Project

February 2019

#### Overview

explorePy is a python package loaded with methods to help explore and explain the contents of a Pandas dataframe.

#### Functions

###### Function 1 | Variable summary
The function will take a pandas data frame as input and provide the total quantity of each type of variable present in the data frame. The output of the function will be a dataframe and will have one row for each variable type with its corresponding quantity. The function will look to identify 6 different types of variables: numerical, categorical, boolean, string, date, and an others category

###### Function 2 | Missing values per variable
For each column/variable in the pandas dataframe, this function will count the number of missing values present and report back on that number per column. The function will accept a dataframe as input and output a corresponding dataframe with the above information detailing the counts of missing values per column/variable

###### Function3 | Dataset Size/Info
This function will take in a dataframe and print the shape and size of the dataframe. For the size, the function will print how much memory the dataframe consumes in Bytes or Megabytes. The function will also return information about the average size of each entry. The function will also provide data about the total number of observations and variables present in the data.

#### Comparable Functions Available in the Python and R Ecosystems
The following are existing functions in Python and R that are similar to those developed within our project.

###### Python
[df.info()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html): provides summary information about a pandas dataframe, including data types for variables and number of null values.   
[df.shape()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html): provides the dimensions of a pandas dataframe.    
[df.count()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.count.html): provides the number of non-missing values in each column or row of the dataframe.  

###### R
 [dim()](https://www.rdocumentation.org/packages/base/versions/3.5.2/topics/dim): used to obtain the shape of a dataframe.   
[ncol()](https://www.rdocumentation.org/packages/base/versions/3.5.2/topics/nrow) and [nrow()](https://www.rdocumentation.org/packages/base/versions/3.5.2/topics/nrow): used to get the number of rows and columns in a dataframe.       
[str()](https://www.rdocumentation.org/packages/utils/versions/3.5.2/topics/str): provides summary information about the dataframe, including some of the same information as above (i.e. dim, ncol and nrow). str() provides descriptive information about variable and data types in the dataframe.   
[is.na()](https://www.statmethods.net/input/missingdata.html): provides the number of missing values in the columns of the data frame.


#### Collaborators:

| name | github handle |
| ---- | ------ |
| Rachel K. Riggs | [@rachelkriggs](https://github.com/rachelkriggs) |
| Milos Milic     | [@milicmil](https://github.com/milicmil) |
| Arzan Irani     | [@nazra-inari](https://github.com/nazra-inari) |
| James Pushor    | [@jpush1773](https://github.com/jpush1773)
