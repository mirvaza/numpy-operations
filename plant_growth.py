import numpy as np

#creating matrix
arr = np.array([
    [12, 15, 18],
    [10, 14, 17],
    [11, 16, 20]
])
print("Plant Growth Matrix:")
print(arr)

#reshaping: converting matrix into single row
report=arr.reshape(1,9)
print("\nReshaped Growth Data:")
print(report)


#Apply Fertilizer Growth Factor
factor = np.array([
    1.1, 1.05, 1.08,
    1.1, 1.07, 1.06,
    1.09, 1.04, 1.1
])
updated_value = values * factor
print("\nGrowth After Fertilizer:")
print(updated_value)
