'''
Creating setup.py
In order to make your package installable by pip you need to create a setup.py file. In this exercise you will create this file for the text_analyzer package you've been building.

Instructions
100 XP
import the needed function, setup, from the setuptools package.
Complete the name & packages arguments; keep in mind your package is located in a directory named text_analyzer.
List yourself as the author.
'''
SOLUTION

# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='DM',
      packages=['text_analyzer'])
