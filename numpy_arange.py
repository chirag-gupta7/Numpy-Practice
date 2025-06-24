# NumPy .arange() Examples

import numpy as np

# .arange()
# In Python, we have the built-in .range() function that we use in a for loop. Well, NumPy has something that looks similar called the .arange() function.

# The .arange() function, short for "array range", is a function that creates an array with evenly spaced values.

# For example:

arr = np.arange(5)

print(arr)    # Output: [0 1 2 3 4]

# You can go further with its three parameters:

# start is the first value in the array.
# stop is end of the range.
# step is step size of the intervals.

# For example:

arr = np.arange(start=1, stop=10, step=3)

print(arr)   # Output: [1 4 7]

# We start with the value 1.
# We stop at the value 10.
# We go up 3 each time.
# Now you might be thinking... why isn't 10 included? 🤔 The reason is that the stop value is always an upper limit that's not part of the range.

# Practical Example: Halley's Comet appearances
# Halley's Comet has an orbital period of approximately 76 years and last appeared in 1986.
# Let's create an array of years when it will appear next from 1986 to 3000:

halley_years = np.arange(start=1986, stop=3001, step=76)

print("Halley's Comet will appear in these years:")
print(halley_years)
# Output: [1986 2062 2138 2214 2290 2366 2442 2518 2594 2670 2746 2822 2898 2974]

