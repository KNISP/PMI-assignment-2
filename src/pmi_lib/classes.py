import numpy as np
from typing import Any

class Image:
    def __init__(self, data: np.array, spacing: tuple[float, ...] | None =None):
        """
        Initialize an Image object.
        :param data: The image data as a numpy array.
        :param spacing: The spacing of the image in each dimension. Default is None, which will be set to 1.0 for each dimension.
        """
        if type(data) is not np.ndarray:
            raise TypeError(f"Data must be a numpy array, got {type(data)} instead.")
        if type(spacing) is not tuple or spacing is not None:
            raise TypeError(f"Spacing must be a tuple or None, got {type(spacing)} instead.")

        if data.ndim != len(spacing):
            raise ValueError(f"Data dimensions {data.ndim} do not match spacing dimensions {len(spacing)}.")

        # Default spacing to 1.0 for each dimension if not provided
        if spacing is None:
            self.spacing = (1.0,) * data.ndim
        else:
            self.spacing = spacing

        self.data = data

    def __repr__(self) -> str: # or use __str__
        """
        Return a string representation of the Image object.
        """
        return f"A {type(self.data)} image with shape {self.data.shape} and a spacing of {self.spacing} mm."

    def __len__(self) -> int:
        """
        Return the length of the outer dimension of the image data (number of slices).
        """
        return self.data.shape[0]

    def __array__(self, dtype: np.typing.DTypeLike | None = None, *, copy: bool | None = None) -> np.ndarray:
        """
        Return the image data as a numpy array with the specified dtype.
        """
        self.data = self.data.astype(dtype, copy=copy)
        return self.data

    def __getitem__(self, key: Any) -> np.ndarray:
        """
        Return the image data at the specified index.
        """
        return self.data[key]

    def get_pixel_area(self) -> float:
        """
        Calculate the pixel area for 2D images.
        """
        if self.data.ndim < 2:
            raise ValueError("Data must be at least 2D to calculate pixel area.")

        return self.spacing[0]*self.spacing[1]

    def get_voxel_volume(self) -> float:
        """
        Calculate the voxel volume for 3D images.
        """
        if self.data.ndim < 3:
            raise ValueError("Data must be at least 3D to calculate voxel volume.")

        return self.spacing[0]*self.spacing[1]*self.spacing[2]

class DicomImage(Image):
    def __init__(self, data: np.array, metadata: dict, spacing: tuple[float, ...] | None =None):
        """
        Initialize a DicomImage object.
        :param data: The image data as a numpy array.
        :param metadata: The metadata of the DICOM image.
        :param spacing: The spacing of the image in each dimension. Default is None, which will be set to 1.0 for each dimension.
        """
        super().__init__(data, spacing)
        self.metadata = metadata
