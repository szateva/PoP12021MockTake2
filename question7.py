# 13021326

""" Implement a class My_integer that fulfils the following specification:
class My_integer:
def __init__(self, x):
#method creates My_integer object that represents
#a usual Python integer x
def increase(self, o):
#method increases the value of this object by the
#value represented by another My_integer object o;
#method returns nothing
def plus(self, o):
#method returns the My_integer object representing
#the sum of the value represented by this object and
#the value represented by My_integer object o
Moreover, implement the overloading of == operator on My_integer objects. That is,
for two My_integer objects o1 and o2, o1 == o2 must return True, if the integers rep-
resented by o1 and o2 are equal, otherwise it must return False. Your implementation
must be able to run with the following code and provide the results as in comments:
a = My_integer(20)
b = My_integer(364)
c = a.plus(b)
d = My_integer(182)
a.increase(d)
assert not a==c #must be True
a.increase(d)
assert a==c #must be True """

class My_integer:
    def __init__(self, x):
        self.x = x

    def increase(self, o):
        self.x += o.x

    def plus(self, o):
        new = My_integer(self.x + o.x)
        return new

    def __eq__(self, o):
        if self.x == o.x:
            return True
        else:
            return False


a = My_integer(20)
b = My_integer(364)
c = a.plus(b)
d = My_integer(182)
a.increase(d)
assert not a==c #must be True
a.increase(d)
assert a==c #must be True