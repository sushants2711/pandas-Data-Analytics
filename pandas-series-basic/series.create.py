import pandas as pd

# series create with default index
data = pd.Series([10, 20, 30, 40])

print(data)

# series create with labeled indexing
dataLab = pd.Series(
    [10, 20, 30],
    index=["a", "b", "c"]
)

print(dataLab)

# series create with help of dictionary

dataWithDict = pd.Series({
    "A": 90,
    "B": 10,
    "C": 55,
    "E": 89
})

print(dataWithDict)

# define data and index labeled and than merge 
d1 = [100, 200, 300, 30]
l1 = ["a", "b", "c", "d"]

s = pd.Series(d1, index = l1)
print("The new Series")
print(s)