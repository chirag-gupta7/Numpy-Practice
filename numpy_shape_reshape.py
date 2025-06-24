# NumPy .shape and .reshape() Examples

import numpy as np

# .shape
# NumPy arrays have a property called .shape that returns a tuple containing number of elements each dimension has.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) 

print(arr.shape)     # Output: (2, 4)

# When we print arr.shape, we get (2, 4) because there are two dimensions:
# The 1st dimension has 2 elements (for the rows).
# The 2nd dimension has 4 elements (for the columns).

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) 

print(arr.shape)     # Output: (4, 3)

# When we print arr.shape, we get (4, 3) because there are two dimensions:
# The 1st dimension has 4 elements (for the rows).
# The 2nd dimension has 3 elements (for the columns).

# .reshape()
# If we want to change the shape of an array, we use the .reshape() function.

# Suppose we want to convert the following 1D array into a 2D one:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8]) 
new_arr = arr.reshape(2, 4)

print(new_arr)

# Output:
# [[1 2 3 4]
# [5 6 7 8]]

# Here we are turning the arr array into two dimensions:
# The 1st dimension has 2 rows.
# The 2nd dimension has 4 columns.

month_results = np.array([56, 100, 33, 0, 45, 45, 46, 34, 89, 180, 60, 45, 45, 44, 46, 45, 0, 0, 15, 90, 301, 197, 20, 60, 45, 45, 42, 45])

weekly_results = month_results.reshape(4, 7)
print(weekly_results)