'''
Listing requirements in setup.py
We created a setup.py file earlier, but we forgot to list our dependency on matplotlib in the install_requires argument. In this exercise you will practice listing your version specific dependencies by correcting the setup.py you previously wrote for your text_analyzer package.

Instructions
100 XP
import the needed function, setup, from the setuptools package.
List yourself as the author.
Specify your install_requires to require matplotlib version 3.0.0 or above.
'''
SOLUTION

# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='DM',
      packages=['text_analyzer'],
      install_requires=['matplotlib>=3.0.0'])
