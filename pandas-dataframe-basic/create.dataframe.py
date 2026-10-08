import pandas as pd

# A dataframe is a 2d structure (rows & columns) in pandas similar to excel sheet or structure table. We keep each column as a different datatype.

# Their are different ways to create a dataframe in pandas

# using dictionary and provide multiple value in the form of an array
emp1 = {
    "id" : [101, 102, 103],
    "name": ["Sushant", "Abhi", "Bhavya"],
    "salary": [49000, 44000, 39000]
}

df = pd.DataFrame(emp1)

# print(df)


# using dictionary and provide multiple value in the form of an array and also define with using of an pandas dataframe
emp2 = pd.DataFrame({
    "id" : [101, 102, 103],
    "name": ["Sushant", "Abhi", "Bhavya"],
    "salary": [49000, 44000, 39000]
})

# print(emp2)

# using list 
emp3 = [
    [1,2,3],
    ["Sushant", "Abhi", "Bhavya"],
    [49000, 44000, 39000]
]

col = ["id", "name", "salary"]

df2 = pd.DataFrame(emp3, columns=col)

# print(df2)


emp4 = pd.DataFrame(
    {
        "id": [1, 2, 3, 4],
        "name": ["sushant", "abhi", "akash", "sourav"],
        "age": [21, 22, 22, 23]
    }
    #    index=["a", "aa", "ab", "abb"]
)

# print(emp4)



emp5 = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["sushant", "abhi", "akash", "sourav"],
    "age": [21, 22, 22, 23]
})

emp5.index = ["a", "b", "c", "d"]

print(emp5)