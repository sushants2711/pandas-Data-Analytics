import pandas as pd

data = pd.Series([10, 20, 30, 40])

print(data[3])


# Actual way to access the series using properties

# 1. iloc[] - It is used to access the value through index

print(data.iloc[0]) # to access single value 

print("--- --- ---")

print(data.iloc[0: 3]) # access multiple value through index till n-1

print("--- --- ---")

print(data.iloc[[0, 2, 3]]) # access multiple value based on particular index

# 2. loc[] - It is used to access with labeled based value. If we not define labeled than by default index is labeled and we also access the value through index as labeled.

print(data.loc[0]) # to access single value 

print(data.loc[0: 3]) # to access multiple value till n

print(data.loc[[0, 2, 3]]) # access multiple value based on particular index

