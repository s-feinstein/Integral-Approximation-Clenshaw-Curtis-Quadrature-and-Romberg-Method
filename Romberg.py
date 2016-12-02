# Python implementation of Romberg's Method
# Called by CCversusR.py on problem set 
# UO Math 351 Project by Samantha Mintzmyer
# Resources used: stackoverflow.com | wikipedia.org | wolframalpha.com | doc.sagemath.org

# Problem input: Function, integrand range [a, b], n
def Romberg(function, a, b, n):
    # call R(function,a,b,n,m)
    return R(function,a,b,n,n)

def R(function,a,b,n,m):
    h = h_n(a, b, n)

    # R(0,0) = h1(f(a)+f(b))
    if n == 0 and m == 0:
        return h*(function(a)+function(b))

    # R(n,0) = (1/2)R(n-1,0) + hn * FROM k=1 => k=2**(n-1) SUM f(a+(2k-1)*hn)
    elif n != 0 and m == 0:
        # Loop for sum
        sum = 0
        for k in range (1, 2**(int(n)-1)):
            sum += function(a+((2*k)-1)*h)
        sum = sum * h
        # Return with recursion
        return (1/2)*R(function,a,b,n-1,0)+sum

    # R(n,m) = (1/((4**m)-1))*(4**m)*R(n,m-1) - R(n-1,m-1)
    elif n != 0 and m != 0:
        # Return with recursion
        return ((1./((4.**m)-1.))*((4.**m)*R(function,a,b,n,m-1)-R(function,a,b,n-1,m-1)))

# hn = (1/(2**n))*(b-a)
def h_n(a, b, n):
    return ((1./(2.**n))*(b-a))
    
