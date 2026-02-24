import numpy as np
#Creating sales matrix
sales = np.array([ [30000, 25000, 20000],   # Employee 1
                   [40000, 35000, 30000],   # Employee 2
                   [20000, 15000, 10000]    # Employee 3
])
print("Original Sales Matrix:")
print(sales)


#Deleting product B
sales = np.delete(sales, 1, axis=1)
print("\nAfter Deleting Product B:")
print(sales)


#Slicing: Select product C
product_c = sales[:, 1]
print("\nProduct C Before Bonus:")
print(product_c)


#Broadcasting: Double Product C Sales
sales[:, 1] = sales[:, 1] * 2
print("\nAfter Doubling Product C for Bonus:")
print(sales)



#Reshaping: Convert to single row format
single_row = sales.reshape(1, -1)

print("\nFinal Single Row Format for Payroll:")
print(single_row)
