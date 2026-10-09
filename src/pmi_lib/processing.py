import numpy as np
from scipy.ndimage import gaussian_filter

def masked_gaussian_filter(pixel_data, bool_mask, sd):
    # Use 32-bit floating point precision for the image and the mask.
    

    # Error handling 
    # als pixel data & bool mask niet even groot 
    if np.shape(pixel_data) != np.shape(bool_mask):
        raise ValueError("Image and mask shapes should be the same")
    


    # M×(G(M×I, σ) / G(M, σ))
    gaus_filt = gaussian_filter(pixel_data, sd) #G(M, σ) - filtered

    #add mask to image
    masked_image = pixel_data.copy()
    for i in range(len(pixel_data[0])):
        for j in range(len(pixel_data[1])):

            if bool_mask[i, j] == False:
                masked_image[i, j] = 0

    
    mask_gaus_filt = gaussian_filter(masked_image, sd) / gaus_filt #(G(M×I, σ) / G(M, σ))
    mask_gaus_filt = np.nan_to_num(mask_gaus_filt)


    #Apply mask to masked_filt / filt 
    for i in range(len(pixel_data[0])):
            for j in range(len(pixel_data[1])):
            
                if bool_mask[i, j] == False:
                    mask_gaus_filt[i, j] = 0

    return mask_gaus_filt



# Test data
pixel_data = np.arange(50, step=2).reshape((5,5))
bool_mask = np.ones((5, 5), dtype=bool)
bool_mask[2] = [0,0,0,0,0]
sd = 3

masked_gaussian_filter(pixel_data, bool_mask, sd)


