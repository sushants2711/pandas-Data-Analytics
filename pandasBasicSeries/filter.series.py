import pandas as pd

s = pd.Series(
    [10,20,30,40,10,-22,34,100,3],
    index = ["a","b","c","d","e","f","g","h", "aa"]
)

# print(s[s > 20])

# print(s[s > 50])

# print(s[ (s > 20) & (s < 80)])  # find the data between range

# print(s[s % 2 == 0])  # print all even numbers

# print(s[s % 2 != 0])  # print all odd numbers

# print(s[s<0])  # print all negative numbers

# print(s[s != 100])  # print the value that is not equal to 0

