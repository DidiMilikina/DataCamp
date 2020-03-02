'''
Edges
In this exercise you will identify the shapes in a grapefruit image by detecting the edges, using the Canny algorithm.

Grapefruits
Image preloaded as grapefruit.
The color module has already been preloaded for you.

Instructions
100 XP
Import the canny edge detector from the feature module.
Convert the image to grayscale, using the method from the color module used in previous chapters.
Apply the canny edge detector to the grapefruit image.
'''
SOLUTION

# Import the canny edge detector 
from skimage.feature import canny

# Convert image to grayscale
grapefruit = color.rgb2gray(grapefruit)

# Apply canny edge detector
canny_edges = canny(grapefruit)

# Show resulting image
show_image(canny_edges, "Edges with Canny")