'''
Recognizing packages
The structure of your directory tree is printed below. You'll be working in the file my_script.py that you can see in the tree.

recognizing_packages
├── MY_PACKAGE
│   └── _init_.py
├── package
│   └── __init__.py
├── package_py
│   └── __init__
│       └── __init__.py
├── py_package
│   └── __init__.py
├── pyackage
│   └── init.py
└── my_script.py
Instructions
100 XP
Use the information from the context to identify the packages in the directory that follow the minimal structure.
import the two packages that follow the minimal package requirements.
Use help() to print information about each imported package.
'''
SOLUTION

# Import local packages
import py_package
import package

# View the help for each package
help(py_package)
help(package)
