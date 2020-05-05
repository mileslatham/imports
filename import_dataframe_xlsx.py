'''
Miles Latham (05-05-20)
Additional example of an xlsx file with a more complex structure
'''
# import statements:
import pandas as pd  # the "as pd" component just allows you to reference pandas functions with the shortcut "pd."
import os  # used to specify filepaths

'''
One thing that you often encounter with webscraped or downloaded data is files that have a somwhat more complex 
structure than the csv in the other example here. Especially with downloaded excel files, the structure is often optimized 
for human readability with multiple nested column names, merged cells, and that sort of thing. Unfortunately that 
makes things a little more complicated when you want to import the data. Below, we're importing a somewhat more complex 
datafile I just found with some GDP data. The table we're interested in is Table 1- if you take a look at the xlsx file
you'll see that there are multiple header and column rows. 

There are two ways to deal with this. The first is by selecting the header row and index column which best approximate 
the row/column names you want. This is what I do below, additionally specifying the sheet name that we want to read. 
NOTE: remember that python indexes at 0, so row 1 in the excel sheet is row 0 here. 
'''
gdp_filepath = os.path.join('data', 'gdp1q20_Adv.xlsx')
gdp_df = pd.read_excel(gdp_filepath,
                       sheet_name='Table 1',
                       header=3,
                       index_col=0)
print(gdp_df.columns)

"""
The above is a good start, but it's still not ideal because we haven't linked the quarter names in the header columns
to the years each quarter belongs to. A better way, which allows us to store all of the data in the multiple header rows,
is called multi-indexing. 
"""
gdp_multi_indexed = pd.read_excel(gdp_filepath,
                                  sheet_name='Table 1',
                                  headers=[1, 3],
                                  index_col=[0, 1],
                                  skiprows=2,
                                  skip_footer=3,
                                  )
print(gdp_multi_indexed.columns)
"""
Above, we're doing a few things differently. First, we're specifying a range of header rows instead of just one. 
This tells pandas that all of those rows need to be included in the header information. Next, we're doing the same thing 
for the index columns. This tells pandas that both the line number and line description should be included in the index. 
Lastly, we're telling pandas to skip the first two rows of the excel sheet and the last three rows, since those 
contain extraneous information.

Based on this information, pandas is able to infer that the header rows are hierarchical, and should be stacked to 
delineate the unique columns for each quarter/year combination. 
"""

