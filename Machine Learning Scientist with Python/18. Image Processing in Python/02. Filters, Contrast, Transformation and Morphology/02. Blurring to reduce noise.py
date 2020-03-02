'''
Blurring to reduce noise
In this exercise you will reduce the sharpness of an image of a building taken during a London trip, through filtering.

Building in Lodon
Image loaded as building_image.
Instructions
100 XP
Import the Gaussian filter.
Apply the filter to the building_image, set the multichannel parameter to the correct value.
Show the original building_image and resulting gaussian_image.
'''
SOLUTION

# Import Gaussian filter 
from skimage.filters import gaussian

# Apply filter
gaussian_image = gaussian(building_image, multichannel = True)

# Show original and resulting image to compare
show_image(building_image, "Original")
show_image(gaussian_image, "Reduced sharpness Gaussian")