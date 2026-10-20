from .cli import dicom_to_nifti
from .io import read_dicom, read_nifti
from .processing import masked_gaussian_filter


def test(file_path: str):
    """
    Test the functions in the pmi_lib module.

    :param file_path: path to the DICOM file or directory
    """
    # read DICOM files
    dcm_img, dcm_spacing = read_dicom(file_path)
    print(
        f"1. read_dicom executed successfully: shape={dcm_img.shape}, spacing={dcm_spacing} \\n"
    )

    # convert DICOM to NIfTI
    nii_path = "test_output.nii.gz"
    dicom_to_nifti.callback(
        file_path, nii_path
    )  # uses write_nifti internally, callback handles click decorator
    print(
        f"2. dicom_to_nifti & write_nifti executed successfully: output file={nii_path}\\n"
    )

    # read NIfTI file
    nii_img, nii_spacing = read_nifti(nii_path)
    print(
        f"3. read_nifti executed successfully: shape={nii_img.shape}, spacing={nii_spacing}\\n"
    )

    # apply masked Gaussian filter
    mask = dcm_img > 0
    std = tuple(0.8 for _ in range(dcm_img.ndim))
    mask_filt_img = masked_gaussian_filter(dcm_img, mask, std)
    print(
        f"4. masked_gaussian_filter executed successfully: shape={mask_filt_img.shape}\\n"
    )

    print(
        f"--> all tests passed successfully! (do not forget to delete the {nii_path} file when you're done)"
    )
