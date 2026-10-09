import nibabel as nib
import numpy as np
from dicom import read_dicom
from nifti import write_nifti

def dicom_to_nifti(dicom_path, nifti_path):
    """ converting single DICOM files or directories with DICOM files to a Nifti file."""
    
    img, spacing = read_dicom(dicom_path)
    img = np.flip(img, (-1, -2))
    img = np.transpose(img)
    write_nifti(img, spacing, nifti_path)
