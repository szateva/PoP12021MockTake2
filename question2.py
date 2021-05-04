# 13021326

"""
 1) tuples are immutable, hence the operation changed[i] = -t[i] will cause an error
 it can be fixed by converting changed to a list, then adding the changed elements to this list
 and converting changed to a tuple and returning the tuple.
 2) since range(1, len(t)) starts at 1 the first element in the tuple will never be checked.
 To fix change to range(0, len(t)) """

""" Consider the function replace that, for a tuple t of numbers, returns a tuple of the
same size as t, where every negative number n is changed to the positive number -n
and preserves all the positive numbers as they are.
def replace(t):
changed = t
for i in range(1, len(t)):
if t[i]<0:
changed[i] = -t[i]
else:
changed[i] = t[i]
return changed
There are errors in this code that have the potential to either crash the program on
some valid input, or to return incorrect result.
 Find and describe up to three of such errors. In your description, not only state
the errors, but provide the explanation why they occur.
 Indicate how to correct them, without changing the interface to the function (i.e.
the datatypes passed as parameters and returned from the function should not be
changed).
Recommended answer length up to 70 words plus any code. """

def replace(t):
    changed = list(t)
    for i in range(0, len(t)):
        if t[i]<0:
            changed[i] = -t[i]
        else:
            changed[i] = t[i]
    result = tuple(changed)
    return result

t = (-2, -3, 1, -7)
print(replace(t))