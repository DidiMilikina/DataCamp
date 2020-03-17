'''
Writing a class for your package
We've covered how classes can be written in Python. In this exercise, you'll be creating the beginnings of a Document class that will be a foundation for text analysis in your package. Once the class is written you will modify your package's __init__.py file to make it easily accessible by your users.

Below is the structure of where you'll be working.

working_dir
├── text_analyzer
│    ├── __init__.py
│    ├── counter_utils.py
│    ├── document.py
└── my_script.py
Instructions 1/2
50 XP
1
2
You are working in document.py.
Finish the def statement that will create a new Document instance when a user calls Document().
Use your knowledge of PEP 8 conventions to complete the definition of the newly named class method.
'''
SOLUTION

# Define Document class
class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of MyClass
    def __init__(self, text):
        # Store text parameter to the text attribute
        self.text = text
