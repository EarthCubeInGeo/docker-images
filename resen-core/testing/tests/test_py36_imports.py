#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    test_imports.py

    This is intended to be used to check that all expected python packages are avaiable. Works
    well for identifying strangeness that may occur with conda when installing multiple python
    packages with differing dependency requirements.

"""

import unittest
import importlib

class ImportTester(unittest.TestCase):
    # In the future, get this list from a Pipfile and 
    # include a test for package version number
    packages = ['paramiko','IPython','pymongo','mechanize','netCDF4','cryptography','pytest',
                'nbformat','numpy','matplotlib','scipy','tables','sgp4','pandas','sympy',
                'sqlalchemy','h5py','pytz','bokeh','yaml','cython','apexpy','cartopy',
                'spacepy','aacgmv2','pymap3d','mangopy','madrigalWeb','visuamisr',
                'citationhelper','viresclient','hdfviewer','watermark','pydarn','plasmapy']

    def test_imports(self):
        # Try to import all the packages
        for package in self.packages:
            print("Importing %s" % package)
            importlib.import_module(package)

        # if we get here, everything imported fine!
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

# Still need to do:
# import tables
# import pyglow
# import sgp4
# import pydarn
# import sympy
# import SQLAlchemy

# import bokeh
# import ipyparallel

# from Cython.Build import cythonize
# import sunpy
# import heliopy





