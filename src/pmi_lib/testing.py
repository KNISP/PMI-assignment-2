# Add a function test() that takes a file path (a string) to a DICOM file or directory with DICOM files and executes all
# functions above.

from dicom import read_dicom
from conversion import dicom_to_nifti
from nifti import read_nifti, write_nifti

def test(dicom_path, nifti_path):
    """Test the DICOM to Nifti conversion process."""
    dicom_data, dicom_spacing = read_dicom(dicom_path)
    print(f"Done reading DICOM files: shape={dicom_data.shape}, spacing={dicom_spacing}")

    dicom_to_nifti(dicom_path, nifti_path)
    print("Done converting to Nifti")

    nifti_data, nifti_spacing = read_nifti(nifti_path)
    print(f"Done reading Nifti file: shape={nifti_data.shape}, spacing={nifti_spacing}")

    print("Done testing")