#code for square by using map()
l=[1,5,6,8]
a=list(map(lambda x:x**2,l))
print(a)

def sq(x):
    return x**2
print(list(map(sq,l)))



#code for even number by using filter()
b=list(filter(lambda x:x%2==0,l))
print(b)

def even(x):
    return x%2==0
print(list(filter(even,l)))



#code for additiin if all nu numbers by using reduce()
from functools import reduce
c=reduce(lambda x,y:x+y,l)
print(c)


def add(x,y):
    return x+y
print(reduce(add,l))