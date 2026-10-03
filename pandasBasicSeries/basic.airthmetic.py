import pandas as pd

s = pd.Series([10,20,30,40,50])

# print(s+5)

# print(s*10)

# print(s + s*10//100)

d = pd.Series([1,2,3,4,5])

# print(s + d)

# print(s[s>10] * 2)

# increase all value grater than 30 by 10%
s = s [s > 30]
s = s + (s * 10) // 100
print(s)

# decrease the value less than 40 by 5
# print(s[s < 40] - 5)

# Multiply values greater than or equal to 50 by 2

# add 100 to values less than or equal to 20

# replace values greater than 40 with their square values

# divide the value less than 30 by 2

# add 10 % bonus only to values between 30 and 50
