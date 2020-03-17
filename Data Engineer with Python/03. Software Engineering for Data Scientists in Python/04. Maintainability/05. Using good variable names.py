'''
Using good variable names
Just like functions, descriptive variable names can make your code much more readable. In this exercise, you'll write some code using good variable naming practices.

There's not always a clear best name for a variable. The exercise has been written to try and make a clear best choice from the provided options.

Instructions
100 XP
Choose the best variable name to hold the sample of pupil diameter measurements in millimeters from the following choices: d, diameter, pupil_diameter, or pupil_diameter_in_millimeters.
Take the mean of the measurements and assign it to a variable. Choose the best variable name to hold this mean from the following options: m, mean, mean_diameter, or mean_pupil_diameter_in_millimeters.
Print the resulting average pupil diameter.
'''
SOLUTION

from statistics import mean

# Sample measurements of pupil diameter in mm
pupil_diameter = [3.3, 6.8, 7.0, 5.4, 2.7]

# Average pupil diameter from sample
mean_diameter = mean(pupil_diameter)

print(mean_diameter)
