import os
import numpy as np
from pydicom import dcmread
from pydicom.pixels import apply_rescale

def get_z_position(dicom_image):
    """
    Returns the z-coordinate of the Image Position Patient DICOM attribute.
    """
    return dicom_image.ImagePositionPatient[2]


def get_spacing(dicom_list):
    """
    Returns the x and y (and z) spacing of the DICOM images in the list.
    """
    n = len(dicom_list)
    dx, dy = dicom_list[0].PixelSpacing # get pixel spacing from the first image (same spacing for all)
    
    # Calculate the z spacing if there are multiple images (z_end - z_start) / (n - 1)
    if n > 1:
        z_first = np.array(dicom_list[0].ImagePositionPatient)
        z_last = np.array(dicom_list[-1].ImagePositionPatient)
        dz = np.linalg.norm(z_last - z_first) / (n - 1)
        return [dx, dy, dz]
    else:
        return [dx, dy]


def read_dicom(file_path):
    """
    Reads a DICOM file and returns the pixel data as a numpy array.
    """
    if os.path.isfile(file_path):
        dicom_file = dcmread(file_path)  # Read the image.
        dicom_array = dicom_file.pixel_array  # Get the pixel data.
        dicom_image = apply_rescale(dicom_array, dicom_file)  # Apply rescale for HU.
        spacing = get_spacing([dicom_file])  # Get the spacing.
    elif os.path.isdir(file_path):
        dicom_files = [dcmread(os.path.join(file_path, f)) for f in os.listdir(file_path)]
        dicom_files.sort(key=get_z_position)  # Sort by z-position.
        dicom_arrays = [f.pixel_array for f in dicom_files]  # Get the pixel data.
        dicom_image = [apply_rescale(a, f) for a, f in zip(dicom_arrays, dicom_files)]  # Apply rescale for HU.
        spacing = get_spacing(dicom_files)  # Get the spacing.
    else:
        raise ValueError(f"Invalid file path: {file_path}")
    
    return np.array(dicom_image), spacing