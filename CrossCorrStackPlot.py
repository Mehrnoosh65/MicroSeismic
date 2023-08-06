# code by Mehrnoosh Behzadi
# Mar 2013
# Uni Hamburg
import numpy as np
import matplotlib.pyplot as plt

def plot_slice(X, Y, Z, RCC, x_pos=None, y_pos=None, z_pos=None):
    # Create a 3D plot and set the data for the specified slice positions
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if x_pos is not None:
        ax.plot_surface(X[:, x_pos, :], Y[:, x_pos, :], Z[:, x_pos, :], facecolors=RCC[:, x_pos, :])
    if y_pos is not None:
        ax.plot_surface(X[y_pos, :, :], Y[y_pos, :, :], Z[y_pos, :, :], facecolors=RCC[y_pos, :, :])
    if z_pos is not None:
        ax.plot_surface(X[:, :, z_pos], Y[:, :, z_pos], Z[:, :, z_pos], facecolors=RCC[:, :, z_pos])

    # Set axis labels and plot title
    ax.set_xlabel('Width [m]', fontsize=20)
    ax.set_ylabel('Length [m]', fontsize=20)
    ax.set_zlabel('Depth [m]', fontsize=20)
    ax.set_title('Field data - Star receiver array - in 3D\nFirst Arrivals - P wave travel times', fontsize=20)
    
    # Reverse the z-axis to represent depth
    ax.set_zlim(4400, 0)
    ax.view_init(elev=20, azim=230)

    # Display the plot
    plt.show()

def main():
    # Prompt user for velocity model dimensions
    width = int(input("Enter the width of the velocity model (in meters): "))
    length = int(input("Enter the length of the velocity model (in meters): "))
    depth = int(input("Enter the depth of the velocity model (in meters): "))

    # Create meshgrid
    X, Y, Z = np.meshgrid(np.arange(0, width + 100, 100),
                          np.arange(0, length + 100, 100),
                          np.arange(0, depth + 100, 100))

    # Prompt user to input velocity model
    RCC = np.zeros((width // 100 + 1, length // 100 + 1, depth // 100 + 1))
    for i in range(depth // 100 + 1):
        RCC[:, :, i] = np.array(input(f"Enter the RCC values for depth {i*100} m (space-separated): ").split(),
                                dtype=float)

    # Plot slices for the specified positions
    x_pos = int(input("Enter the X position for the first slice: "))
    y_pos = int(input("Enter the Y position for the second slice: "))
    z_pos = int(input("Enter the Z position for the third slice: "))

    plot_slice(X, Y, Z, RCC, x_pos=x_pos, y_pos=y_pos, z_pos=z_pos)

if __name__ == "__main__":
    main()
