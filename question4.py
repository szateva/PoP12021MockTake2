# 13021326

""" Assume f(x) and g(x) are functions that are defined for numbers x and their return
value is also a number. Implement a higher-order function:
apply_functions(f,g,L)
that takes as parameters functions f and g as above, and a list of numbers L. It returns
a list of numbers M, such that each element M[i] is equal to f(L[i]), if L[i] is not
negative, and to g(L[i]) if L[i] is negative.
Indicative test cases:
def double(x):
return 2*x
def square(x):
return x*x
assert apply_functions(double, square, [1,-6,-3,5]) == [2,36,9,10]
#must be True
#abs is the standard function returning absolute value
assert apply_functions(double, abs, [1,-6,-3,5]) == [2,6,3,10]
#must be True """

def apply_functions(f,g,L):
    M = L
    for i in range(len(L)):
        if L[i] >= 0:
            M[i] = f(L[i])
        else:
            M[i] = g(L[i])
    return M

# Indicative test cases:
def double(x):
    return 2*x
def square(x):
    return x*x
assert apply_functions(double, square, [1,-6,-3,5]) == [2,36,9,10]
#must be True
#abs is the standard function returning absolute value
assert apply_functions(double, abs, [1,-6,-3,5]) == [2,6,3,10]
#must be True