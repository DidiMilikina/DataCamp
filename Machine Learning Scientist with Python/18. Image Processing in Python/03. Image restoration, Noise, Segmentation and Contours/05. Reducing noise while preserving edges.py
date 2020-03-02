'''
Reducing noise while preserving edges
In this exercise, you will reduce the noise in this landscape picture.

Landscape of a river
Preloaded as landscape_image.
Since we prefer to preserve the edges in the image, we'll use the bilateral denoising filter.

Instructions
100 XP
Import the denoise_bilateral function from its module.
Apply bilateral filter denoising.
Show the original noisy and the resulting denoised image.
'''
SOLUTION

# Import bilateral denoising function
from skimage.restoration import denoise_bilateral

# Apply bilateral filter denoising
denoised_image = denoise_bilateral(landscape_image, 
                                   multichannel=True)

# Show original and resulting images
show_image(landscape_image, 'Noisy image')
show_image(denoised_image, 'Denoised image')