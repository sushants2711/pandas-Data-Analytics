import pandas as pd

s = pd.read_excel("pandas-dataframe-basic/pandas-lear.xlsx")

# print(s)

# print(s)

# read with sheet name

# s = pd.read_excel("pandas-dataframe-basic/pandas-lear.xlsx", sheet_name="sheet1")

# multiple sheets read

# s = pd.read_excel("pandas-dataframe-basic/pandas-lear.xlsx", sheet_name=None) # it create a dictionary of dataframe through which we can select multiple sheet at a same time

# for a particular columns

# s = pd.read_excel("pandas-dataframe-basic/pandas-lear.xlsx", usecols=["Product", "Quantity"])  # to get a particular columns

# print(s)

# s = pd.read_excel("pandas-dataframe-basic/pandas-lear.xlsx", usecols="A: C") # means take column A to C

# print(s[["Customer", "Product"]]) # a list through which we can print a multiple columns

# print(s.iloc[0]) # access the value or row 0

# print(s.iloc[0:4])  # access multiple rows while use of indexing iloc we get the value n-1

# print(s.loc[0: 4])  # access multiple rows while use of labeling loc we get the value till n


# s.index = ["a", "b", "c", "d", "e", "f", "g", "h"]  # create a index for Dataframe

# print(s)


# slicing row and column means i want 0,1,2 row and 0,1,2 i want column 

# print(s.iloc[0: 3, 0: 3])  # the first one i used to row slicing and the 2nd one is used to column slicing

# using loc
print(s.loc[0: 4, ["Customer", "Product"]])