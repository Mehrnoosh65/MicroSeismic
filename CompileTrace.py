# code by Mehrnoosh Behzadi
# Feb 2013
# Uni Hamburg
from obspy import read
import os
import numpy as np

# Set the path to the directory containing the mseed files
mseed_directory = "E:\BehzadiPhD\FieldData-Microseismic\Cascade\7No12"

# List all files in the directory
all_files = os.listdir(mseed_directory)

# Filter the mseed files
mseed_files = [file_name for file_name in all_files if file_name.endswith('.mseed')]

# Initialize the data list to store seismograms
data = []

for file_name in mseed_files:
    full_path = os.path.join(mseed_directory, file_name)
    st = read(full_path)
    h = np.array(st[0].data)

    s = h.shape[0]
    if s < 36040:
        l = 36040 - s
        A = np.ones(l) * h[0]
        h = np.concatenate((A, h))
    elif s > 36040:
        h = h[:36040]

    data.append(h)

# Convert the data list to a 2D NumPy array
seismogram = np.column_stack(data)
