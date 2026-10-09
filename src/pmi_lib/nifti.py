import nibabel as nib
import numpy as np
def read_nifti(file_path):
    """takes a file path (a string) and returns the pixel data (a NumPy array) and the voxel
spacing (a tuple of floats)."""
    nifti_image = nib.load(file_path)
    data = nifti_image.get_fdata()
    spacing = nifti_image.header.get_zooms()
    return data, spacing


def write_nifti(data, spacing, file_path):
   """ takes the pixel data (anything that can be converted into a numpy array), the voxel
spacing (a sequence of floats), and a file path (a string). Raise a ValueError when the arguments to write_nifti() are incompatible."""
   data = np.asarray(data)
   spacing = tuple(spacing)

   if len(spacing) != data.ndim:
       raise ValueError("The arguments to write_nifti() are incompatible.")
