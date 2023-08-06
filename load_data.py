# code by Mehrnoosh Behzadi
# Jan 2013
# Uni Hamburg
import scipy.io as sio

def load_data(mat_file_path):
    data = sio.loadmat(mat_file_path)
    SeisHPz = data['SeisHPz']
    geometry_data = sio.loadmat('/scratch/local1/u250118/FieldData-Microseismic/Cascade/GeometeryCascadia.mat')
    FT = geometry_data['FT']
    return SeisHPz, FT
