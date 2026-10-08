import pandas as pd

s = pd.read_excel("pandas-dataframe-basic/pandas-lear.xlsx")

# s = s[s["Quantity"] > 4]

# print(s[s["Quantity"] > 5 ])

# print(s)


# Show all employee whose Sales is greater than 10,000

# df1 = s[s["Sales"] > 100000]

# print(df1)

# Displayy all the data that product belongs to Monitor

# df2 = s[s["Product"] == "Monitor"]

# print(df2)

# Find the order data whose sales is greater than 10000 and less than 40000

df3 = s[s["Sales"].between(10000, 60000)]

print(df3)

df4 = s[(s["Sales"] >= 10000) & (s["Sales"] <= 60000)]

print(df4)