import numpy as np
from .io import read_dicom, write_nifti
import click

@click.command()
@click.argument('dicom_path', type=click.Path(exists=True, file_okay=True), required=True)
@click.argument('nifti_path', required=True)
def dicom_to_nifti(dicom_path, nifti_path):
    """
    Convert a DICOM file or directory to a NIfTI file.

    :param dicom_path: path to the DICOM file or directory
    :param nifti_path: path to the output NIfTI file
    """
    # don't bother CLI users with python exceptions
    try:
        dcm_img, spacing = read_dicom(dicom_path)
    except (FileNotFoundError, ValueError) as error:
        raise click.ClickException(error)
    except Exception:
        raise click.ClickException("An unexpected error occurred while reading the DICOM input.")

    try:
        # convert from LPS to RAS orientation (mirror Y and X) and from row-major (ZYX) to column-major (XYZ) order
        data = np.flip(dcm_img, (-1, -2))
        nii_img = np.transpose(data)
    except Exception:
        raise click.ClickException("An unexpected error occurred while converting the DICOM input.")

    try:
        write_nifti(nii_img, spacing, nifti_path)
    except ValueError as error:
        raise click.ClickException(error)
    except Exception:
        raise click.ClickException("An unexpected error occurred while writing the NIfTI output.")
