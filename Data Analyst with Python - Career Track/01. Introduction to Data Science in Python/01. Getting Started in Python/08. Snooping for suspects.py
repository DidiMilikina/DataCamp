'''
Snooping for suspects
We need to narrow down the list of suspects for the kidnapping of Bayes. Once we have a list of suspects, we'll ask them for writing samples and compare them to the ransom note.

A witness to the crime noticed a green truck leaving the scene of the crime whose license plate began with 'FRQ'. We'll use this information to search for some suspects.

As a detective, you have access to a special function called lookup_plate.

lookup_plate accepts one positional argument: A string representing a license plate.

Instructions 3/3
30 XP
Create a variable called plate that represents the observed license plate: the first three letters were FRQ, but the witness couldn't see the final 4 letters. Use asterisks (*) to represent missing letters.
Call lookup_plate() using the variable plate.
Calling lookup_plate() with the license plate FRQ**** produced too many results. Luckily, lookup_plate() also accepts a keyword argument: color. Use the color of the car ('Green') to get a smaller list.
'''
SOLUTION
# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)

# Call lookup_plate() with the keyword argument for color
lookup_plate(plate, color='Green')