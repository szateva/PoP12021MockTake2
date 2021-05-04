# 13021326

""" The function takes two numeric lists of equal size and returns a new list of the same size
consisting of the larger element of the two lists index by index. """


""" Consider the following recursive function:
def fun(L1, L2):
if L1==[] and L2==[]:
return []
else:
if L1[0] > L2[0]:
return [L1[0]]+fun(L1[1:], L2[1:])
else:
return [L2[0]]+fun(L1[1:], L2[1:])
Assume that the function is only called on a pair of lists of equal size containing
numbers.
Find the best English description of the main purpose of this function. The use of code
in your description should be minimal, this is important in marking. Recommended
answer length up to 40 words. """

def fun(L1, L2):
    if L1==[] and L2==[]:
        return []
    else:
        if L1[0] > L2[0]:
            return [L1[0]]+fun(L1[1:], L2[1:])
        else:
            return [L2[0]]+fun(L1[1:], L2[1:])

L1 = [1, 2, 3, 4]
L2 = [2, 3, 4, 5]

print(fun(L1, L2))