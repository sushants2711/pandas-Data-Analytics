import pandas as pd

dataSeries = pd.Series(
    [10, 20, 30, 30, 30, 12, 23, 20, 20, 20, 100],
    index = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "h"]
)

# print(dataSeries)


# print(dataSeries.head())  # return the first 5 values from the series
# print(dataSeries.head(2)) # return the first n values from the series

# print(dataSeries.tail()) # return the last 5 values from the series
# print(dataSeries.tail(1)) # return the last n values from the series

# print(dataSeries.shape) # how many rows/values?  The comma is important because (5,) is a one-dimensional shape.

# print(dataSeries.size) # total number of values

# print(dataSeries.ndim) # how many dimensions?

# print(dataSeries.dtype) # it show the data type of the series

# print(dataSeries.index) # it return the index of the series

# print(dataSeries.values) #  it return the value of the series

dataSeries.index.name = "Number System Data"

# print(dataSeries)

# print(dataSeries.sum())  # find the sum of all series
# print(dataSeries.mean()) # average of the series
# print(dataSeries.median()) # show the middle of the value
print(dataSeries.mode())  # show the repeating value that comes most number of time if the value is not repeating it return the whole series
# print(dataSeries.min()) # minimum value of the series
# print(dataSeries.max()) # maximum value of the series
# print(dataSeries.prod()) # multiply of the series
# print(dataSeries.count()) # count the total number of value and skip the null value