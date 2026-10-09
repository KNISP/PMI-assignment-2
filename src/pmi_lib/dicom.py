import os
import numpy as np
from pydicom import dcmread
from pydicom.pixels import apply_rescale

def _get_z_position(dicom_image):
    """
    Returns the z-coordinate of the Image Position Patient DICOM attribute.
    """
    return dicom_image.ImagePositionPatient[2]


def _get_spacing(dicom_list):
    n = len(dicom_list)  # The number of slices in the list.
    dx, dy = dicom_list[0].PixelSpacing  # Read the X and Y pixel spacing from the first slice.
    
    if n > 1:
        # There are multiple slices. Get the offset of the first and last slice, calculate the
        # Euclidean distance, and divide it by n-1 to get the slice spacing.
        z_first = np.array(dicom_list[0].ImagePositionPatient)
        z_last = np.array(dicom_list[-1].ImagePositionPatient)
        dz = np.linalg.norm(z_last - z_first) / (n - 1)
        return [dx, dy, dz]
    else:
        # There is just one slice. There is no slice spacing.
        return [dx, dy]


def read_dicom(file_path):
    # Check if file_path is a directory. If it is, then iterate over the directory and create a 3d volume.
    # If it is not a directory, then open the file as usual.

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file or directory {file_path} does not exist.")
    elif os.path.isdir(file_path):
        # Read all DICOM files.
        dicom_images = []
        for file_name in os.listdir(file_path):
            full_path = os.path.join(file_path, file_name)
            if os.path.isfile(full_path):
                dicom_images.append(dcmread(full_path))  # Read the image.

        # Sort the files on the Instance Number.
        sorted_images = sorted(dicom_images, key=_get_z_position)

        # Calculate the spacing.
        spacing = _get_spacing(sorted_images)
            
        slices = []
        for dicom_image in sorted_images:
            slices.append(apply_rescale(dicom_image.pixel_array, dicom_image))  # Convert from stored pixel values to real values.
        
        data = np.array(slices)
        return data, spacing
    else:
        dicom_image = dcmread(file_path)  # Read the image.
        spacing = _get_spacing([dicom_image])  # Calculate the spacing.
        data = apply_rescale(dicom_image.pixel_array, dicom_image)  # Convert from stored pixel values to real values.
        return data, spacing