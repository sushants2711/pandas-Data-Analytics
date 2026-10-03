import pandas as pd

data = pd.Series([10, 20, 30, 40])

s = data.astype(float)

print(s)

print(data.dtype)
print(s.dtype)