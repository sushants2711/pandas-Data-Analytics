import pandas as pd

s = pd.Series(
    [10,20,30,40,10,-22,34,100,3, None],
    index = ["a","b","c","d","e","f","g","h", "aa", "aac"]
)

# print(s[s > 20])

# print(s[s > 50])

# print(s[ (s > 20) & (s < 80)])  # find the data between range

# print(s[s % 2 == 0])  # print all even numbers

# print(s[s % 2 != 0])  # print all odd numbers

# print(s[s<0])  # print all negative numbers

# print(s[s != 100])  # print the value that is not equal to 0

# print(s.isna())

# print(s.isnull())

# print(s.notna())

# s.fillna(0)

# s.fillna(s.mean())

# s.dropna()

# print(s.var())  # s.var() means variance in Pandas.

# Variance tells you how spread out the values are from their average (mean).


# print(s.duplicated())

# s.drop_duplicates()

# s.str.upper()
# s.str.lower()
# s.str.title()
# s.str.len()

# names.str.contains("a")
# names.str.startswith("S")
# names.str.endswith("t")

# names.str.replace("a", "A")