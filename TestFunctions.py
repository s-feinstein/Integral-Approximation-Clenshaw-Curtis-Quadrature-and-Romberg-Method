from math import e, cos, sqrt, log
from numpy import arcsin

# Difficult integration problems: http://www.artofproblemsolving.com/community/c7h515012

def f_1over1plusx4(x):
    x = 1.0/(1.0+(x**4.))
    return x

def f_x2over1plusx2sq(x):
    x = (x**2.0)/((1.0+(x**2))**2)
    return x

def f_xexcosx(x):
    x = x*(e**x)*cos(x)
    return x

def f_arcsinx(x):
    x = arcsin(x)
    return x

def f_messy(x):
    x = (e**x)*(1/(sqrt((x**2)+1)) + (1-(2*(x**2)))/(sqrt((x**2)+1)**5))
    return x

def f_cosx(x):
    x = cos(x)
    return x

