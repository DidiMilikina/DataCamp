'''
Find contours of an image that is not binary
Let's work a bit more on how to prepare an image to be able to find its contours and extract information from it.

We'll process an image of two purple dices loaded as image_dices and determine what number was rolled for each dice.

Purple dices
In this case, the image is not grayscale or binary yet. This means we need to perform some image pre-processing steps before looking for the contours. First, we'll transform the image to a 2D array grayscale image and next apply thresholding. Finally, the contours are displayed together with the original image.

color, measure and filters modules are already imported so you can use the functions to find contours and apply thresholding.

We also import io module to load the image_dices from local memory, using imread. Read more here.

Instructions 1/4
35 XP
1
Transform the image to grayscale using rgb2gray().

2
Obtain the optimal threshold value for the image and set it as thresh.

3
Apply thresholding to the image once you have the optimal threshold value thresh, using the corresponding operator.

4
Apply the corresponding function to obtain the contours and use a value level of 0.8.
'''
SOLUTION

1
# Make the image grayscale
image_dices = color.rgb2gray(image_dices)

2
# Make the image grayscale
image_dices = color.rgb2gray(image_dices)

# Obtain the optimal thresh value
thresh = filters.threshold_otsu(image_dices)

3
# Make the image grayscale
image_dices = color.rgb2gray(image_dices)

# Obtain the optimal thresh value
thresh = filters.threshold_otsu(image_dices)

# Apply thresholding
binary = image_dices > thresh

4
# Make the image grayscale
image_dices = color.rgb2gray(image_dices)

# Obtain the optimal thresh value
thresh = filters.threshold_otsu(image_dices)

# Apply thresholding
binary = image_dices > thresh

# Find contours at a constant value of 0.8
contours = measure.find_contours(binary, 0.8)

# Show the image
show_image_contour(image_dices, contours)