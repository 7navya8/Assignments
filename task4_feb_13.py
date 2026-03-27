# create numpy array with the following temperature in degree Celsius 
# (28,32,40,37,26,38).convert the list into numpy array.
# print maximum and minimum temperature and calculate average temperature and 
# display last 3 dyas temperature
import numpy as np

# Temperatures in degree Celsius
temps = [28, 32, 40, 37, 26, 38]

# Convert list into numpy array
temp_array = np.array(temps)

# Print maximum and minimum temperature
print("Maximum Temperature:", temp_array.max())
print("Minimum Temperature:", temp_array.min())

# Calculate average temperature
print("Average Temperature:", temp_array.mean())

# Display last 3 days temperature
print("Last 3 Days Temperature:", temp_array[-3:])