square = lambda arg1 : arg1 ** 2
#print(square(4))

add = lambda arg1,arg2 : arg1 + arg2
#print(add(3,4))

def make_power(n):
    return lambda x:x ** n

f = make_power(2)

print(f(3))