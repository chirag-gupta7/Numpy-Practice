import numpy as np

# Steps taken in the last week (replace these with your actual phone data)
# Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
weekly_steps = np.array([8543, 10287, 6432, 9876, 12045, 15623, 7890])

# By default, these math operations apply to the array as though it were a list of numbers. 
# However, by specifying the axis parameter, we can apply an operation along the specified axis of an array:
#
# temperatures = np.array([[50, 51, 54, 59, 59, 53, 54, 51],
#                          [45, 50, 38, 44, 40, 46, 43, 39]])
#
# np.sum(temperatures, axis=0)   # Sum of each column
# np.min(temperatures, axis=1)   # Min of each row
#
# axis=0: each column (vertical direction, down the rows)
# axis=1: each row (horizontal direction, across the columns)
#
# Visual representation:
#                    axis 1 →
#           col-0  col-1  col-2  col-3
#   axis 0  row-0   [  ]   [  ]   [  ]   [  ]
#     ↓     row-1   [  ]   [  ]   [  ]   [  ]
#           row-2   [  ]   [  ]   [  ]   [  ]

print("Weekly Steps Analysis:")
print("=" * 30)
print("Daily steps:", weekly_steps)
print("Days of week: Mon, Tue, Wed, Thu, Fri, Sat, Sun")
print()

# Calculate statistics using NumPy methods
min_steps = weekly_steps.min()
max_steps = weekly_steps.max()
total_steps = weekly_steps.sum()
average_steps = weekly_steps.mean()  # Note: use .mean() instead of .average()

print("Statistics:")
print(f"Minimum steps in a day: {min_steps}")
print(f"Maximum steps in a day: {max_steps}")
print(f"Total steps for the week: {total_steps}")
print(f"Average steps per day: {average_steps:.2f}")

# Additional analysis
print()
print("Additional Insights:")
print(f"Range (max - min): {max_steps - min_steps}")
print(f"Standard deviation: {weekly_steps.std():.2f}")

# Find which day had min and max steps
min_day_index = np.argmin(weekly_steps)
max_day_index = np.argmax(weekly_steps)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(f"Least active day: {days[min_day_index]} ({min_steps} steps)")
print(f"Most active day: {days[max_day_index]} ({max_steps} steps)")