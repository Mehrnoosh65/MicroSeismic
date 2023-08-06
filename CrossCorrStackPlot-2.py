# code by Mehrnoosh Behzadi
# Feb 2013
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

def load_velocity_model():
    while True:
        velocity_model_file = input("Enter the path to the ASCII velocity model file: ")
        try:
            # Load the ASCII velocity model from the text file
            RCC = np.genfromtxt(velocity_model_file, delimiter=' ')  # Update delimiter if needed
            if RCC.ndim != 3:
                raise ValueError("Velocity model must be a 3D array.")
            width, length, depth = RCC.shape[0] * 100, RCC.shape[1] * 100, RCC.shape[2] * 100
            break
        except (IOError, ValueError) as e:
            print("Error: ", e)
            print("Please check the file path and format and try again.")

    return RCC, width, length, depth

def main():
    # Load the velocity model from the ASCII file
    RCC, width, length, depth = load_velocity_model()

    # Create meshgrid
    X, Y, Z = np.meshgrid(np.arange(0, width + 100, 100),
                          np.arange(0, length + 100, 100),
                          np.arange(0, depth + 100, 100))

    # Plot slices for the specified positions
    x_pos = int(input("Enter the X position for the first slice: "))
    y_pos = int(input("Enter the Y position for the second slice: "))
    z_pos = int(input("Enter the Z position for the third slice: "))

    plot_slice(X, Y, Z, RCC, x_pos=x_pos, y_pos=y_pos, z_pos=z_pos)

if __name__ == "__main__":
    main()
