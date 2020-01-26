a = 10
a = int(5)  #another way to create number object
print(type(a))

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

def select_function(fun_id):
    if fun_id == 1:
        return square
    else:
        return cube


f = select_function(1)
print(f(2))
print(select_function(2)(3)) #here select funtion will first evaluate the first parameter and then return of that evaluation will evalutate the second parameter




