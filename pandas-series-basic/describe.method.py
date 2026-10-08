import pandas as pd

s = pd.Series(
    [10,2,30,30,55,12,230, None],
    index = ['z', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
)

# print(s.describe()) # return the multiple things that is important in term of data analytics

# print(s.value_counts()) # it return the all the frequency of the value but ignore the None or null value

# print(s.unique()) # it will return the distinct value only that means those value that is unique and also add the None or null values

# print(s.nunique()) # Returns the number of unique values except None or null

# print(s.sort_values())

# print(s.sort_index())

# print(s.agg(["sum", "mean", "min", "max"]))