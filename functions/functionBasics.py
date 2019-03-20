
def hello():
    print("Hello")

#hello()

#This function returns nothing like the first but still u can add return with nothing
def hello(name):
    print("Hello, "+name)
    return 
#hello("sumit")

#this function returns a string value
def hello(name):
    """This function says 'Hello' """  #this is a doc string.
    return "Hello, "+name

#print(hello.__doc__)  #this is how doc string is accessed.
#print(hello("Sumit"))

#This function returns a boolean value
def is_negative(num):
    if num < 0:
        return True
    else:
        return False

#print(is_negative(5))

#this function takes list of arguments
def hello(*names):
    for name in names:
        print("Hello",name)
    return
#hello("Sumit","Shantanu")

b = 2

def outside():
    global b  # to access global value of b, else it wont be accessible
    b = b+1
    a = 5

    def inside():
        nonlocal a  #to access the local variable value a defined in outside function
        a = a+1
        print("inside a",a)
        return

    print("outside a",a)
    inside()
    print("outside a after function",a)
    return

print("outside b",b)
outside()
print("outside b after function call", b)