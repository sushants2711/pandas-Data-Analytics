import pandas as pd

# series create with default index
data = pd.Series([10, 20, 30, 40])

print(data.dtype)

data2 = pd.Series([10.22, 20.2, 30.3, 40.12])

print(data2.dtype)

data3 = pd.Series(["sys", "us", "abc"])
print(data3.dtype)

data4 = pd.Series([True, False, False, True, True])
print(data4.dtype)

data5 = pd.Series(["Apple", 43, 45.55, True])
print(data5.dtype)

data6 = pd.Series([4,44,67,5.45])
print(data6.dtype)

data7 = pd.Series([4,4,4,3,2,5, None])
print(data7.dtype)

data8 = pd.Series(["sys", "us", "abc", None])
print(data8.dtype)

data9 = pd.Series([True, False, False, True, True, None])
print(data9.dtype)