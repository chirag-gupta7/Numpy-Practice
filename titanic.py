import numpy as np
passengers = np.array([
   [1, 0, 3, 22],
   [2, 1, 1, 38],
   [3, 1, 3, 26],
   [4, 1, 1, 35],
   [5, 0, 3, 35],
   [6, 0, 3, 18],
   [7, 0, 1, 54],
   [8, 0, 3, 2],
   [9, 1, 3, 27],
  [10, 1, 2, 14],
  [11, 1, 3, 4],
  [12, 1, 1, 58],
  [13, 0, 3, 20],
  [14, 0, 3, 39],
  [15, 0, 3, 14],
  [16, 1, 2, 55],
  [17, 0, 3, 2],
  [18, 1, 2, 12],
  [19, 0, 3, 31],
  [20, 1, 3, 8],
  [21, 0, 2, 35],
  [22, 1, 2, 34],
  [23, 1, 3, 15],
  [24, 1, 1, 28],
  [25, 0, 3, 8],
  [26, 1, 3, 38],
  [27, 0, 3, 2],
  [28, 0, 1, 1],
  [29, 1, 3, 5],
  [30, 0, 3, 18],
  [31, 0, 1, 40],
  [32, 1, 1, 70],
  [33, 1, 3, 33],
  [34, 0, 2, 66],
  [35, 0, 1, 28],
  [36, 0, 1, 42],
  [37, 1, 3, 5],
  [38, 0, 3, 18],
  [39, 0, 3, 18],
  [40, 1, 3, 14],
  [41, 0, 3, 40],
  [42, 0, 2, 27],
  [43, 0, 3, 29],
  [44, 1, 2, 0],
  [45, 1, 3, 19],
  [46, 0, 3, 33],
  [47, 0, 3, 14],
  [48, 1, 3, 22],
  [49, 0, 3, 41],
  [50, 0, 3, 18]
])

array_shape = passengers.shape
print(f"Shape of the passengers array: {array_shape}")

average_Age = np.mean(passengers[:, 3])
print(f"Average age of passengers: {average_Age:.2f}")

# Find the oldest passenger
max_age = np.max(passengers[:, 3])
oldest_passenger_index = np.argmax(passengers[:, 3])
oldest_passenger_number = passengers[oldest_passenger_index, 0]
print(f"Oldest passenger: Passenger #{oldest_passenger_number} with age {max_age}")

# Find the youngest passenger
min_age = np.min(passengers[:, 3])
youngest_passenger_index = np.argmin(passengers[:, 3])
youngest_passenger_number = passengers[youngest_passenger_index, 0]
print(f"Youngest passenger: Passenger #{youngest_passenger_number} with age {min_age}")

# Calculate survival statistics
survival_data = passengers[:, 1]  # Extract survival column (0 = died, 1 = survived)
total_passengers = len(survival_data)
survivors = np.sum(survival_data)  # Count of people who survived (sum of 1s)
deaths = total_passengers - survivors

survival_percentage = (survivors / total_passengers) * 100

print(f"\nSurvival Statistics:")
print(f"Total passengers: {total_passengers}")
print(f"Survivors: {survivors}")
print(f"Deaths: {deaths}")
print(f"Survival percentage: {survival_percentage:.1f}%")

