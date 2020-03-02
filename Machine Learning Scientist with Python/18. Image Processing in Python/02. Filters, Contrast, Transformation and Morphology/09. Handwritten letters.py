'''
Handwritten letters
A very interesting use of computer vision in real-life solutions is performing Optical Character Recognition (OCR) to distinguish printed or handwritten text characters inside digital images of physical documents.

Let's try to improve the definition of this handwritten letter so that it's easier to classify.
As we can see it's the letter R, already binary, with with some noise in it. It's already loaded as upper_r_image.

Apply the morphological operation that will discard the pixels near the letter boundaries.

Instructions
100 XP
Import the module from scikit-image.
Apply the morphological operation for eroding away the boundaries of regions of foreground pixels.
'''
SOLUTION

# Import the morphology module
from skimage import morphology

# Obtain the eroded shape 
eroded_image_shape = morphology.binary_erosion(upper_r_image) 

# See results
show_image(upper_r_image, 'Original')
show_image(eroded_image_shape, 'Eroded image')