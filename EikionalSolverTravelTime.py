# code by Mehrnoosh Behzadi
# Sep 2013
# Uni Hamburg
import numpy as np
from scipy.ndimage import distance_transform_edt

def calculate_travel_time(velocity_model, source_location, receiver_location):
    """
    Calculates the travel time of a seismic ray in a 3D velocity model of the ground using the FMM method.

    Args:
    - velocity_model: NumPy array of shape (nz, ny, nx) containing the velocity model in m/s.
    - source_location: Tuple (z, y, x) containing the source location in grid coordinates.
    - receiver_location: Tuple (z, y, x) containing the receiver location in grid coordinates.

    Returns:
    - Travel time in seconds.
    """

    # Define the grid spacing
    dz, dy, dx = 1.0, 1.0, 1.0

    # Calculate the reciprocal of the squared velocity model
    inv_v2 = 1.0 / (velocity_model ** 2)

    # Initialize the distance function with large values everywhere except at the source
    distance = np.ones_like(velocity_model) * np.inf
    distance[source_location] = 0.0

    # Calculate the distance function using the FMM method
    distance = distance_transform_edt(inv_v2, sampling=(dz, dy, dx), return_distances=True, return_indices=False,
                                      method='fast', initial=distance)

    # Calculate the travel time by dividing the distance by the velocity
    travel_time = distance[receiver_location] / velocity_model[receiver_location]

    return travel_time

# Load the ASCII velocity model from the text file
velocity_model_file = "velocity_model.txt"
RCC = np.loadtxt(velocity_model_file)

# Define the source and receiver locations (modify as needed)
source_location = (0, 0, 0)  # Example source location at grid coordinates (0, 0, 0)
receiver_location = (10, 10, 10)  # Example receiver location at grid coordinates (10, 10, 10)

# Calculate the travel time using the velocity model and locations
travel_time = calculate_travel_time(RCC, source_location, receiver_location)
print("Travel time:", travel_time, "seconds")
