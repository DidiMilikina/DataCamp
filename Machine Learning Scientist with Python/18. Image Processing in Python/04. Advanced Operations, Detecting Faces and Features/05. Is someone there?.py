'''
Is someone there?
In this exercise, you will check whether or not there is a person present in an image taken at night.

LAndscape of starry night with a young man in the left bottom corner
Image preloaded as night_image.
The Cascade of classifiers class from feature module has been already imported. The same is true for the show_detected_face() function, that is used to display the face marked in the image and crop so it can be shown separately.

Instructions
100 XP
Load the trained file from the data module.
Initialize the detector cascade with the trained file.
Detect the faces in the image, setting the minimum size of the searching window to 10 pixels and 200 pixels for the maximum.
'''
SOLUTION

# Load the trained file from data
trained_file = data.lbp_frontal_face_cascade_filename()

# Initialize the detector cascade
detector = Cascade(trained_file)

# Detect faces with min and max size of searching window
detected = detector.detect_multi_scale(img = night_image,
                                       scale_factor=1.2,
                                       step_ratio=1,
                                       min_size=(10, 10),
                                       max_size=(200, 200))

# Show the detected faces
show_detected_face(night_image, detected)