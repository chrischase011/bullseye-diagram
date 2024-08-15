import numpy as np
import matplotlib.pyplot as plt

# Number of dots
num_dots = 500

num_circles = 5
radii = np.linspace(0, 1, num_circles + 1)
angles = np.random.uniform(0, 2 * np.pi, num_dots)

# Generate radii with bias towards the center
radii_dots = np.sqrt(np.random.uniform(0, 1, num_dots)) * radii[1]

# Calculate x and y coordinates
x = radii_dots * np.cos(angles)
y = radii_dots * np.sin(angles)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the scatter plot
ax.scatter(x, y, color='limegreen', alpha=0.6)

# Draw concentric circles and label them
for radius in radii:
    circle = plt.Circle((0, 0), radius, color='black', fill=False, linestyle='--')
    ax.add_artist(circle)
    if radius != 0.45:  # Skip the label for the circle at radius 0.45
        ax.text(radius, 0, f'{radius*100:.0f}', fontsize=12, ha='center')

# Draw a red circle at radius 0.45 without a label
red_circle = plt.Circle((0, 0), 0.45, color='red', fill=False, linestyle='--')
ax.add_artist(red_circle)

# Set the limits and aspect ratio
ax.set_aspect('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Define the custom tick positions and labels
tick_positions = np.linspace(-1, 1, 11)
tick_labels = [str(i) for i in range(-100, 101, 20)]
ax.set_xticks(tick_positions)
ax.set_yticks(tick_positions)
ax.set_xticklabels(tick_labels)
ax.set_yticklabels(tick_labels)

# Labeling the plot
plt.title('Scatter Plot with Concentric Circles')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Remove grid and show plot
plt.grid(False)
plt.show()
