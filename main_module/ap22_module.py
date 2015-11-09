###### Python3.*
###### this is a module to be used in experiment 253, AP2.2, Uni Heidelberg, 2015
###### all the imports take place in the notebooks

###### Defining functions in this section

## load data from files
def load_data(filename):

    """
    filename is the name of the data files
    it is assumed, that the description in the data file is just one row
    returns a list of the columns as numpy arrays
    """
    ## import pylab inside the function so that it doesn't appear as a function for the module
    import pylab as py

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

    ## import numpy inside the function so it doesn't appear as a function for the module
    import numpy as np

    x = np.array(x)
    y = np.array(y)

    ## p is an array of the polynomial coefficients
    p = np.polyfit(x, y, deg = deg)

    ## pass the coefficients to the poly1d function to get the desired function
    fitted_curve = np.poly1d(p)

    ## use extrapolate values if given
    if(len(extrapolate)): x = np.array(extrapolate)

    return fitted_curve(x), p

## linear regression
def lin_reg(x, y, sigma=None):
    """
    x, y should be numpy arrays (floats)
    returns a linear fit to the data and the optimal values for the parameters and the estimated
        covariance of the optimal parameters
    """

    ## import numpy inside the function so it doesn't appear as a function for the module
    import numpy as np
    from scipy.optimize import curve_fit

    x = np.array(x)
    y = np.array(y)

    def lin_func(x, k, b):
        return k * k + b

    popt, pcov = curve_fit(lin_func, x, y, sigma=sigma)

    fitted_y = popt[0]*x + popt[1]

    return fitted_y, popt, pcov
