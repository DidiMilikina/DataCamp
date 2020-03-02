'''
Aerial image
In this exercise, we will improve the quality of an aerial image of a city. The image has low contrast and therefore we can not distinguish all the elements in it.

Aerial image, airport taken from the air
Image loaded as image_aerial.
For this we will use the normal or standard technique of Histogram Equalization.

Instructions
100 XP
Import the required module from scikit-image.
Use the histogram equalization function from the module previously imported.
'''
SOLUTION

# Import the required module
from skimage import exposure

# Use histogram equalization to improve the contrast
image_eq =  exposure.equalize_hist(image_aerial)

# Show the original and resulting image
show_image(image_aerial, 'Original')
show_image(image_eq, 'Resulting image')