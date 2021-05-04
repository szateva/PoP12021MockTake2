# 13021326

"""  """

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
    changed = t
    for i in range(1, len(t)):
        if t[i]<0:
            changed[i] = -t[i]
        else:
            changed[i] = t[i]
    return changed