import os
import numpy as np
from dicom import read_dicom
from nifti import write_nifti
import click

@click.command()
@click.argument('dicom_path', type=click.Path(exists=True, file_okay=True), required=True)
@click.argument('nifti_path', required=True)
def dicom_to_nifti(dicom_path, nifti_path):
    """ converting single DICOM files or directories with DICOM files to a Nifti file."""
    if not os.path.exists(dicom_path):
        raise FileNotFoundError(f"The file or directory {dicom_path} does not exist.")
    
    img, spacing = read_dicom(dicom_path)
    img = np.flip(img, (-1, -2))
    img = np.transpose(img)
    write_nifti(img, spacing, nifti_path)
