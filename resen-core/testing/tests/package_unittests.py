# package_unittests.py
# script to automatically run unit tests of all packages installed in resen-core

import sys
import inspect

    
def apexpy_test():
    pass

def bokeh_test():
    pass

def bsddb3_test():
    pass

def cartopy_test():
    pass

def cryptography_test():
    pass

def cython_test():
    pass

def davitpy_test():
    pass

def h5py_test():
    pass

def ipython_test():
    pass

def mangopy_test():
    pass

def matplotlib_test():
    pass

def mechanize_test():
    pass

def nbformat_test():
    pass

def netCDF4_test():
    pass

def numpy_test():
    import numpy
    numpy.test()

def pandas_test():
    pass

def paramiko_test():
    pass

def pyglow_test():
    pass

def pymongo_test():
    pass

def pytest_test():
    pass

def pytz_test():
    pass

def scipy_test():
    pass

def sciunit2_test():
    pass

def sgp4_test():
    pass

def spacepy_test():
    pass

def sqlalchemy_test():
    pass

def sympy_test():
    pass

def tables_test():
    pass

def yaml_test():
    pass

    
if __name__=='__main__':
    test_functions = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    for name, test in test_functions:
        test()