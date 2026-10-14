# PMI Library - group 5

`pmi-lib` is a small Python library for reading medical images, converting
DICOM data to NIfTI, and applying masked Gaussian filtering.

## Functions

- Read a single DICOM file or a directory containing one DICOM series.
- Read a NIfTI file.
- Write a NIfTI file.
- Convert DICOM files or directories to NIfTI (from the command line).
- Apply a Gaussian filter (inside a boolean mask).
- Test the full pipeline.

## Requirements

- Python 3.14 (or newer)
- NumPy
- SciPy
- pydicom
- NiBabel
- Click

## Installation

From the project directory, install the package:

```bash
python -m pip install -e .
```

This installs the `pmi_lib` package and the `dicom-to-nifti` command-line
executable. You can then convert DICOM images into NIfTI images from your
terminal.

## Command-line usage

Convert a DICOM file or directory to a NIfTI file:

```bash
dicom-to-nifti path/to/input.dcm path/to/output.nii.gz
```

The input may also be a directory containing DICOM slices:

```bash
dicom-to-nifti path/to/dicom_directory path/to/output.nii.gz
```

Use the help option to see the command arguments:

```bash
dicom-to-nifti --help
```

## Folder structure

```text
PMI-assignment-2/
├── src/
│   └── pmi_lib/
│       ├── __init__.py
│       ├── cli.py
│       ├── io.py
│       ├── processing.py
│       └── testing.py
├── pyproject.toml
├── README.md
├── setup.py
├── MANIFEST.in
└── LICENSE.md
```
