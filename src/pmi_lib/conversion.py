import nibabel as nib
import numpy as np
from dicom import read_dicom

def dicom_to_nifti(dicom_path, nifti_path):
    """ converting single DICOM files or directories with DICOM files to a Nifti file."""
    # Note that nibabel uses RAS orientation and column-major ordering. We need to convert the image to row-major
    # ordering and LPS orientation.
    dicom_image = read_dicom(dicom_path)
    data = dicom_image
    data = np.flip(data, (-1, -2))
    data = np.transpose(data)
    nib.save(data, nifti_path)


