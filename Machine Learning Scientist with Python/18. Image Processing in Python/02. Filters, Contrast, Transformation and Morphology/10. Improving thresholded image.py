'''
Improving thresholded image
In this exercise, we'll try to reduce the noise of a thresholded image using the dilation morphological operation.

World map
Image already loaded as world_image.
This operation, in a way, expands the objects in the image.

Instructions
100 XP
Import the module.
Obtain the binarized and dilated image, from the original image world_image.
'''
SOLUTION

# Import the module
from skimage import morphology

# Obtain the dilated image 
dilated_image = morphology.dilation(world_image)

# See results
show_image(world_image, 'Original')
show_image(dilated_image, 'Dilated image')