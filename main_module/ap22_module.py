###### Python3.*
###### this is a module to be used in experiment 253, AP2.2, Uni Heidelberg, 2015

## Imports
import numpy as np
import matplotlib.pyplot as plt
import pylab as py

###### Defining functions in this section

## load data from files
def load_data(filename):

    """
    filename is the name of the data files
    it is assumed, that the description in the data file is just one row
    returns a list of the columns as numpy arrays
    """

    filename = './' + str(filename)
    ## returns every items in the data array as a list of items
    return [i for i in py.loadtxt(filename, unpack=True, skiprows=1)]

## fitting / extrapolating a curve
def polynom_fit(x, y, deg=1, extrapolate=[]):

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
    if(len(extrapolate)): x = np.array(extrapolate)

    return fitted_curve(x), p
