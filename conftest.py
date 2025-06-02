# conftest.py
import sys
import os

# add image_converter folder to sys.path so pytest can find the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'image_converter')))
