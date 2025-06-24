import numpy as np

# Steps taken in the last week (replace these with your actual phone data)
# Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
weekly_steps = np.array([8543, 10287, 6432, 9876, 12045, 15623, 7890])

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