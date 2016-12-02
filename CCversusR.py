# Clenshaw-Curtis vs Romberg comparison of approximation methods
# UO Math 351 Project by Samantha Mintzmyer
# Resources used: stackoverflow.com | wikipedia.org | wolframalpha.com | doc.sagemath.org

#include Clenshaw-Curtis.py and
#include Romberg.py to call their methods
from ClenshawCurtis import *
from Romberg import *
#include TestFunctions.py to for problem set input
from TestFunctions import *

#main method of project
#read in problem from TestFunctions
#call CC and Romberg
#Compare CC to expected value and Romberg to expected value
#Sum total errors.

print("\n\nIntegrate over [-1,1] using Clenshaw-Curtis quadrature and Romberg's method, compare to WolframAlpha\n\n")

#Round 1:
print("Function: 1/(1+x^4)")
outR = Romberg(f_1over1plusx4, -1.0, 1.0, 10.0)
print("Romberg:", outR)
outC = ClenshawCurtis(f_1over1plusx4, -1.0, 1.0, 1000.0)
print("Clenshaw-Curtis:", outC)
outW = 1.73395
print("Wolfram-Alpha:",outW)
Rerror = 0.0
Rerror += (outR-outW)/outW
Cerror = 0.0
Cerror += (outC-outW)/outW

#Round 2:
print("\nFunction: x^2/((1+x^2)^2)")
outR = Romberg(f_x2over1plusx2sq, -1.0, 1.0, 10.0)
print("Romberg:", outR)
outC = ClenshawCurtis(f_x2over1plusx2sq, -1.0, 1.0, 1000.0)
print("Clenshaw-Curtis:", outC)
outW = 0.28540
print("Wolfram-Alpha:",outW)
Rerror += (outR-outW)/outW
Cerror += (outC-outW)/outW

#Round 3:
print("\nFunction: x*e^x*cos(x)")
outR = Romberg(f_xexcosx, -1.0, 1.0, 10.0)
print("Romberg:", outR)
outC = ClenshawCurtis(f_xexcosx, -1.0, 1.0, 1000.0)
print("Clenshaw-Curtis:", outC)
outW = 0.52417
print("Wolfram-Alpha:",outW)
Rerror += (outR-outW)/outW
Cerror += (outC-outW)/outW

#Round 4:
print("\nFunction: e^x[ 1/(sqrt((x^2)+1)) + (1-2x^2)/(((x^2)+1)^2.5)]")
outR = Romberg(f_messy, -1.0, 1.0, 10.0)
print("Romberg:", outR)
outC = ClenshawCurtis(f_messy, -1.0, 1.0, 1000.0)
print("Clenshaw-Curtis:", outC)
outW = 2.75311
print("Wolfram-Alpha:",outW)
Rerror += (outR-outW)/outW
Cerror += (outC-outW)/outW

#Round 5:
print("\nFunction: cos(x)")
outR = Romberg(f_cosx, -1.0, 1.0, 10.0)
print("Romberg:", outR)
outC = ClenshawCurtis(f_cosx, -1.0, 1.0, 1000.0)
print("Clenshaw-Curtis:", outC)
outW = 1.6829
print("Wolfram-Alpha:",outW)
Rerror += (outR-outW)/outW
Cerror += (outC-outW)/outW

#Print summed relative error
print("\nAverage relative error for Romberg:", Rerror/5.0)
print("Average relative error for Clenshaw-Curtis:", Cerror/5.0)

print("\nAt first, I determined Romberg and Clenshaw-Curtis should receive the same number of partitions, \nto see which method performed better with the same number of divisions. \nAfter all, an approximation can always be improved with further sub-intervals.")
print("I believed my Clenshaw-Curtis method wasn't implemented properly-it's approximations were way off. \nRomberg's work increases exponentially with the number of partitions (summing over ~2^n datapoints) \nforcing me to keep n small for realistic runtime.")
print("However, Clenshaw-Curtis quadrature has no such problem. It's work increases linearly with the number of partitions (summing over ~N/2), \nallowing for far greater partitions of the interval. When I dramatically increased the partitions, \nthe approximations improved sufficiently that I believe my implementation is correct after all.")

#print("\nFunction: arcsin(x)")
#outR = Romberg(f_arcsinx, -1.0, 1.0, 10.0)
#print("Romberg:", outR)
#outC = ClenshawCurtis(f_arcsinx, -1.0, 1.0, 10.0)
#print("Clenshaw-Curtis:", outC)
#outW = 0.0
#print("Wolfram-Alpha:",outW)





#Consider other error meta-analysis that might be useful? Tracking problem 'types' and their average error?

