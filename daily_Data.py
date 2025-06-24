import numpy as np

# 4/2024 sleep (hr) 💤

sleep = np.array([
  [6.0, 6.0, 6.5, 8.0, 10.0, 5.0, 5.0], 
  [6.0, 6.0, 6.0, 6.0, 8.0, 5.0, 5.0],
  [8.0, 8.0, 8.0, 6.0, 5.0, 8.0, 5.0],
  [8.0, 8.0, 5.0, 5.0, 6.0, 5.0, 6.0],
])

# 4/2024 coffee (cups) ☕️

coffee = np.array([
  [1, 2, 1, 2, 1, 1, 0], 
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
])

# 4/2024 exercise (min) 🏃

exercise = np.array([
  [0, 0, 0, 45, 0, 45, 0], 
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
])

average1 = np.average(sleep)
average2 = np.average(coffee)
average3 = np.average(exercise)

print("My sleep average is " + str(round(average1, 2)) + " hours.")
print("My coffee intake average is " + str(round(average2, 2)) + " cups.")
print("My exercise average is " + str(round(average3, 2)) + " minutes.")