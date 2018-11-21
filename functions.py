def func (x):
    return x

print (func('a'))

def func2 (x):
    def add (a):
        return x + a
    return add

test = func (100)
print (test (200))

def func3 ():
    x = 34
    y = 45
    pass # end of function
print (func3())

def funcI (*param):
    return param
print (funcI('sd', 5, 5, 5))

add = lambda x, y: x + y
print (add (3, 5))
