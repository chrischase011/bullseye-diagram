import matplotlib.pyplot as plt
import matplotlib.patches as patches
import mplcursors

def draw_bullseye(ax, radii, colors, line_length, labels):
    for radius, color in zip(radii, colors):
        circle = patches.Circle((0, 0), radius, color=color, fill=True)
        ax.add_patch(circle)
    
    ax.plot([-line_length / 2, line_length / 2], [0, 0], color='black', lw=2)  # Horizontal line
    ax.plot([0, 0], [-line_length / 2, line_length / 2], color='black', lw=2)  # Vertical line
    
    # Add labels for each ring
    for radius, label in zip(reversed(radii), reversed(labels)):
        ax.text(-0.1, radius - 0.1, label, horizontalalignment='center', verticalalignment='center', fontsize=10.5, color='black', fontweight='bold', alpha=0.7)
        ax.text(0, radius, label, horizontalalignment='center', verticalalignment='center', fontsize=10, color='white', fontweight='bold')
    
    ax.set_xlim(-line_length / 2, line_length / 2)
    ax.set_ylim(-line_length / 2, line_length / 2)
    ax.set_aspect('equal', 'box')
    ax.axis('off') 

def plot_scatter(ax, x, y, labels, color='blue', marker='o', size=100):
    scatter = ax.scatter(x, y, color=color, marker=marker, s=size, zorder=5)
    cursor = mplcursors.cursor(scatter, hover=True)
    cursor.connect(
        "add", lambda sel: sel.annotation.set_text(f'{labels[sel.index]}: {x[sel.index]}, {y[sel.index]}')
    )
    # Ensure the annotations are fully opaque
    cursor.connect(
        "add", lambda sel: sel.annotation.set_fontsize(12)
    )
    cursor.connect(
        "add", lambda sel: sel.annotation.get_bbox_patch().set_alpha(1)
    )
    cursor.connect(
        "add", lambda sel: sel.annotation.set_visible(True) 
    )
    cursor.connect(
        "remove", lambda sel: sel.annotation.set_visible(False)
    )

def main():
    radii = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    colors = ['black', 'white', 'black', 'white', 'black', 'white', 'black', 'white', 'red', 'white']  # Colors for each circle
    labels = ['100000', '90000', '80000', '70000', '60000', '50000', '40000', '30000', '20000', '10000']  # Labels for each ring
    line_length = 200  # Length of the lines, you can increase this to make the bullseye bigger

    # Ito yung sample ng data
    # Each data point is represented by a pair of x, y coordinates, and a label for the data point
    x = [10, -15, 20, -25, 5, 0]
    y = [5, -20, 15, -10, 25, 6]
    data_labels = ['data1', 'data2', 'data3', 'data4', 'data5', 'data6']

    fig, ax = plt.subplots()
    
    # Background color
    fig.patch.set_facecolor('gray')
    ax.set_facecolor('gray')
    
    fig.canvas.manager.set_window_title('Bullseye Diagram') # Set the title of the window
    
    draw_bullseye(ax, radii, colors, line_length, labels)
    
    plot_scatter(ax, x, y, data_labels, color='green',  marker='o', size=100)
    
    plt.show()

if __name__ == "__main__":
    main()
