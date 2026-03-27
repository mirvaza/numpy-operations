import numpy as np

# Traffic flow matrix (vehicles per unit time)
# Each element represents traffic from one junction to another
traffic = np.array([
    [10, 20, 30],
    [15, 25, 35],
    [20, 30, 40]
])

# Transformation matrix (represents traffic signal adjustments / route redistribution)
# These values decide how traffic is redistributed
transform = np.array([
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
])

# Display original matrices
print("Original Traffic Flow Matrix:")
print(traffic)

print("\nTransformation Matrix:")
print(transform)

# Apply matrix transformation using NumPy dot product
# This simulates optimization of traffic flow
optimized = np.dot(traffic, transform)

print("\nOptimized Traffic Flow Matrix:")
print(optimized)
