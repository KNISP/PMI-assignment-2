from dicom import read_dicom
from conversion import dicom_to_nifti
from nifti import read_nifti
from filtering import masked_gaussian_filter

def test(dicom_path, nifti_path):
    """Test the DICOM to Nifti conversion process."""
    dicom_data, dicom_spacing = read_dicom(dicom_path)
    print(f"Done reading DICOM files: shape={dicom_data.shape}, spacing={dicom_spacing}")

    dicom_to_nifti(dicom_path, nifti_path)
    print("Done converting to Nifti")

    nifti_data, nifti_spacing = read_nifti(nifti_path)
    print(f"Done reading Nifti file: shape={nifti_data.shape}, spacing={nifti_spacing}")

    mask = dicom_data > 0  # Create a mask for non-zero values.
    std = 1.0  # Standard deviation for the Gaussian filter.

    filtered_data = masked_gaussian_filter(dicom_data, mask, std)
    print(f"Done filtering: shape={filtered_data.shape}")

    print("Done testing")