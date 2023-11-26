import matplotlib.pyplot as plt
import numpy as np

# Generate angle values in the range 0-360 degrees
angles = np.arange(0, 361, 1)

# Convert angles to radians for the sine function
angles_rad = np.radians(angles)

# Calculate sine values for each angle
sin_values = np.sin(angles_rad)

# Plot the sine function
plt.plot(angles, sin_values, label='sin(x)')
plt.title('Sine Function')
plt.xlabel('Angle (degrees)')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()
