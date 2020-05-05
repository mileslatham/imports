A dataframe is the primary data structure used in the Pandas library. Dataframes allow for the storage of two-dimensional data and can be indexed by row and column labels. In this sense, they’re basically structured the same way as an excel sheet or SAS dataset. In Python, dataframes are beneficial compared to other data types like dictionaries because they allow for fast, vectorized calculations, instead of iterating over the rows/values within the container. When working with large datasets, this is often essential. 

One note: dataframes are not equivalent to an RDBMS or SAS dataset, in that DFs only exist in-memory and do not persistently store your data. As such, it’s best to think of them as a way to load and manipulate data. Any program that uses a DF will also have some final location to save the data in a different format or will use the data in the DF to create some chart/result. 

There are a few ways to create a dataframe in Python, as well as built-in functions to read existing data into a dataframe. Since we’re primarily going to be loading data from other sources, I’ll focus on the latter. 

You can read a pretty simple, general introduction to pandas dataframes here: 
https://towardsdatascience.com/pandas-dataframe-a-lightweight-intro-680e3a212b96

Here is the introductory documentation directly from the Pandas docs (Their documentation is often not very clear to beginners so don’t worry if you have trouble following): 
https://pandas.pydata.org/pandas-docs/stable/getting_started/dsintro.html#dataframe

Pandas has fuctions to read data from a variety of different source types, but the the two functions you’re likely to use first are read_csv() and read_excel(). 

The documentation for each is below: 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

In this folder, I’ve included a python file which shows how to use the read_csv() function, although the syntax for reading other tabulated data as well as excel files is relatively similar. 

Additionally, the csv I’m importing in the tutorial is relatively simple. For an example of a more complex file in excel format, check out this example: 
https://marcel-jan.eu/datablog/2019/03/08/showing-a-complex-excel-sheet-whos-boss-with-python-and-pandas/
