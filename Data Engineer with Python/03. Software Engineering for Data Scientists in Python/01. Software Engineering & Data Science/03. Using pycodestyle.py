'''
Using pycodestyle
We saw earlier that pycodestyle can be run from the command line to check a file for PEP 8 compliance. Sometimes it's useful to run this kind of check from a Python script.

In this exercise, you'll use pycodestyle's StyleGuide class to check multiple files for PEP 8 compliance. Both files accomplish the same task, but they differ greatly in formatting and readability. You can view the contents of the files by following their links below.

Instructions
100 XP
Import the pycodestyle package.
Create an instance of StyleGuide named style_checker.
There are two files that we'll be checking; they're named 'nay_pep8.py' and 'yay_pep8.py'. Pass a list containing these file names to our style_checker's check_files method.
print() the results of our style check to the console. Make sure to read the output!
'''
SOLUTION

# Import needed package
import pycodestyle

# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['nay_pep8.py', 'yay_pep8.py'])

# Print result of PEP 8 style check
print(result.messages)
