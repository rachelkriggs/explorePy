# explorePy

### A Collaborative Software Development Project

February 2019

### Overview

explorePy is a python package loaded with methods to help explore and explain the contents of a Pandas dataframe.

### Functions

#### Function 1 | Variable summary
The function `variable_summary` will take a pandas data frame as input and provide the total quantity of each type of variable present in the data frame. The output of the function will be a dataframe of size 5 x 2 and will have one row for each variable type with its corresponding quantity. The function will look to identify 5 different types of variables: numerical, string, boolean, date, and an other category.

example output of `variable_summary`:

| variable_type | count |
| ------------- | ----- |
| numeric       | 5     |
| character     | 4     |
| boolean       | 1     |
| date          | 0     |
| other         | 1     |

#### Function 2 | Missing values per variable
For each column/variable in the pandas dataframe, this function will count the number of missing values present and report back on that number per column. The function `missing_values` will accept a dataframe as input and output a corresponding dataframe with the above information detailing the counts of missing values per column/variable. If the input is of size n x d, the output size will be d x 3.

example output of `missing_values`:

| variable      | missing_values | percent_missing |
| ------------- | ----- | ------ |
| column01_name | 0     | 0      |
| column02_name | 321   | 0.19   |
| column03_name | 0     | 0      |
| column04_name | 1     | 0.0006 |
| ...           | ...   | ...    |

#### Function3 | Dataset Size/Info
The function `size` will take in a dataframe and print the shape and size of the dataframe. For the size, the function will print how much memory the dataframe consumes in Bytes or Megabytes. The output of the function will be a dataframe of size 1 x 3.

example output of `size`:

| rows  | columns | size_in_memory |
| ----- | ------- | -------------- |
| 1690  | 27      | 1.4 MB         |

### Comparable Functions Available in the Python and R Ecosystems
The following are existing functions in Python and R that are similar to those developed within our project.

#### Python
[df.info()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html): provides summary information about a pandas dataframe, including data types for variables and number of null values.   
[df.shape()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html): provides the dimensions of a pandas dataframe.    
[df.count()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.count.html): provides the number of non-missing values in each column or row of the dataframe.  

#### R
 [dim()](https://www.rdocumentation.org/packages/base/versions/3.5.2/topics/dim): used to obtain the shape of a dataframe.   
[ncol()](https://www.rdocumentation.org/packages/base/versions/3.5.2/topics/nrow) and [nrow()](https://www.rdocumentation.org/packages/base/versions/3.5.2/topics/nrow): used to get the number of rows and columns in a dataframe.       
[str()](https://www.rdocumentation.org/packages/utils/versions/3.5.2/topics/str): provides summary information about the dataframe, including some of the same information as above (i.e. dim, ncol and nrow). str() provides descriptive information about variable and data types in the dataframe.   
[is.na()](https://www.statmethods.net/input/missingdata.html): provides the number of missing values in the columns of the data frame.


### Collaborators:

| name | github handle |
| ---- | ------ |
| Rachel K. Riggs | [@rachelkriggs](https://github.com/rachelkriggs) |
| Milos Milic     | [@milicmil](https://github.com/milicmil) |
| Arzan Irani     | [@nazra-inari](https://github.com/nazra-inari) |
| James Pushor    | [@jpush1773](https://github.com/jpush1773)
