#---------------------------------------------------------
# Py-Plotting
# Created by Winston Yamanaka
# Created on 2025-05-16
# Last edit: 2025-05-16
# Description: This script demonstrates how to generate plots using NumPy and Matplotlib.
# It creates datasets of various sizes and visualizes one of them.
#---------------------------------------------------------

import numpy as np  # NumPy is used for numerical operations and array handling
import matplotlib.pyplot as plt  # Matplotlib is used for plotting
import time  # Time module is used to measure performance

# 1: Define 3 x-value arrays with increasing number of points
x_100 = np.linspace(1, 10, 100)  # 100 points from 1 to 10
x_10000 = np.linspace(1, 10, 10_000)  # 10,000 points
x_1000000 = np.linspace(1, 10, 1_000_000)  # 1,000,000 points (may slow down system)

# 2: Define corresponding y-values using the natural logarithm
# Using np.log ensures safe evaluation (x > 0)
y_100 = np.log(x_100)
y_10000 = np.log(x_10000)
y_1000000 = np.log(x_1000000)

# 3: Create a plot for the 10,000-point dataset
plt.figure(figsize=(10, 5))  # Set plot size
plt.plot(x_10000, y_10000, label='log(x), 10,000 points', color='darkorange')  # Plot line
plt.title('Logarithmic Plot of 10,000 Points')  # Add a title
plt.xlabel('x')  # Label x-axis
plt.ylabel('log(x)')  # Label y-axis
plt.legend()  # Show legend
plt.grid(True)  # Enable grid
plt.show()  # Display the plot

# 4: Time how long it takes to plot 1,000,000 points
start_time = time.time()  # Start timer
plt.figure(figsize=(10, 5))  # New figure for large dataset
plt.plot(x_1000000, y_1000000, label='log(x), 1,000,000 points', color='purple')  # Plot line
plt.title('Logarithmic Plot of 1,000,000 Points')
plt.xlabel('x')
plt.ylabel('log(x)')
plt.legend()
plt.grid(True)
plt.show()  # Show the large plot
end_time = time.time()  # End timer

# Print time it took to render the large plot
print(f"Time taken to plot 1,000,000 points: {end_time - start_time:.3f} seconds")
