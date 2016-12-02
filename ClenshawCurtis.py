# Python implementation of Clenshaw-Curtis quadrature
# Called by CCversusR.py on problem set
# UO Math 351 Project by Samantha Mintzmyer
# Resources used: stackoverflow.com | wikipedia.org | wolframalpha.com | doc.sagemath.org

# import math library for pi and cosine
from math import pi, cos

# Problem input: Function, integrand range [a, b] (also n?)
# Model input to function

def ClenshawCurtis(function, a, b, N):
    return CC(function,N)

# Generate quadrature weights a2k = (2/N)[(f(1)+f(-1))/2 + f(0)*(-1**k) + 
# FROM n = 1 => (N/2)-1 SUM {f(cos[n*pi/N]) + f(-cos[n*pi/N])} cos(n*k*pi/(N/2)]
def a2k(function,k, N):
    sum = 0
    for n in range (1, (int(N)//2)-1):
        sum += (function(cos((n*pi)/N))+function(-cos((n*pi/N))))*(cos(n*k*pi/(N/2.)))
#        print("a2k sum:",sum)
    return (2/N)*((function(1.)+function(-1.))/2.+function(0)*(-1.**k)+sum) # COV for -1,0,1?

# CC = a0 + FROM k=1 => (N/2)-1 SUM 2*a(2k)/(1-(2k)**2) + aN/(1-N**2)
def CC(function,N):
    sum = 0
    for k in range (1, (int(N)//2)-1):
        sum += (2.*a2k(function,k, N)/(1.-((2.*k)**2.)))
#        print("CC sum:",sum)
#    print (a2k(function,0, N))
    return a2k(function,0, N)+sum+(a2k(function,N/2,N)/(1-(N**2)))


# Change of variable from [-1, 1] to [a, b] 
def COVorigin(o):
    #return (2*x)/(b-a)+(-b-a)/(b-a)
    return o*(b-a)/2.+(a+b)/2.
# Change of variable from [0, pi] to [-1, 1]
def COVtheta(t):
    #return (((pi/2)*COVorigin(x))+pi/2)
    return (((2./pi)*t)-1.)
# Change of variable from [0, pi] to [-1, 1] to [a, b] 
def COV(t):
    return COVorigin(COVtheta(t))
