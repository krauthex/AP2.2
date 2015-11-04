###### don't be an idiot, use Python3!
###### this is a module to be used in experiment 253, AP2.2, Uni Heidelberg, 2015

## Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
import pylab as py

###### Defining functions in this section

## load data from files
def load_data(filename, value_number):

    """
    filename is the name of the data files
    value_number is the amount of data columns in the data file (up to 4)
    it is assumed, that the description in the data file is just one row
    """

    filename = './' + str(filename)

    ## initialize the values
    value1, value2, value3, value4 = 0,0,0,0

    if(value_number == 2):
        value1, value2 = py.loadtxt(filename, unpack=True, skiprows=1)

    if(value_number == 3):
        value1, value2, value3 = py.loadtxt(filename, unpack=True, skiprows=1)

    if(value_number == 4):
        value1, value2, value3, value4 = py.loadtxt(filename, unpack=True, skiprows=1)

    else: print("!! wrong value input")

    return value1, value2, value3, value4

## fitting / extrapolating a curve
def polynom_fit(x, y, deg=1, extrapolate=False):

    """
    x, y should be numpy arrays (floats)
    deg is the degree of the polynomial fit ( p(x) = p[0] * x**deg + p[1] * x**(deg-1) + ... + p[deg] )
    extrapolate: specify an array of x values at which the fitted_curve shall be evaluated.
    returns the the fitted_curve and the polynomial coefficients: p[0]...p[n]
    """

    x = np.array(x)
    y = np.array(y)

    ## p is an array of the polynomial coefficients
    p = np.polyfit(x, y, deg = deg)

    ## pass the coefficients to the poly1d function to get the desired function
    fitted_curve = np.poly1d(p)

    ## use extrapolate values if given
    if(extrapolate): x = np.array(extrapolate)

    return fitted_curve(x), p
