import numpy as np
# Calories burned (Rows = Trainers, Columns = Sessions)
calories = np.array([
    [200, 250, 300],
    [180, 220, 260],
    [210, 240, 280]
])
print("Calories Matrix:")
print(calories)

# Convert 3x3 matrix into single row
flat_data = calories.flatten()
print("\nFlattened Data:")
print(flat_data)

# Transpose matrix
print("\nTranspose of Matrix:")
print(calories.T)

# Total calories per trainee (row-wise sum)
total_calorie = calories.sum(axis=1)
print("\nTotal Calories per Trainee:")
print(total_calorie)

# Average calories burned
average = calories.mean()
print("\nAverage Calories Burned:")
print(average)

# Multiply intensity level using dot()
intensity = np.array([1.0, 1.1, 1.2])
weight = calories.dot(intensity)

print("\nWeighted Performance:")
print(weight)
