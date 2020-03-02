'''
Perspective
In this exercise, you will detect the corners of a building using the Harris corner detector.

Building from a bottom perspective
Image preloaded as building_image.
The functions show_image() and show_image_with_corners() have already been preloaded for you. As well as the color module for converting images to grayscale.

Instructions
100 XP
Import the corner_harris() function from the feature module.
Convert the building_image to grayscale.
Apply the harris detector to obtain the measure response image with the possible corners.
Find the peaks of the corners.
'''
SOLUTION

# Import the corner detector related functions and module
from skimage.feature import corner_harris, corner_peaks

# Convert image from RGB-3 to grayscale
building_image_gray = color.rgb2gray(building_image)

# Apply the detector  to measure the possible corners
measure_image = corner_harris(building_image_gray)

# Find the peaks of the corners using the Harris detector
coords = corner_peaks(measure_image, min_distance=2)

# Show original and resulting image with corners detected
show_image(building_image, "Original")
show_image_with_corners(building_image, coords)