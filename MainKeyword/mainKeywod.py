"""Python is a scripting language hence every script or module run on its own scope
So, when we try to use another module, we should indicate the main module to avoid
executing directly."""

message = "Hello World"

def test():
    print("test from mainKeyword.py")

#test()

#If we import this module into another module and execute that module, then this module will get executed
#and would call method test(), even if the another module does not want it to be called
#To avoid this, we use __name__ == "__main__"

if __name__ == "__main__":
    print("Executing as main program")
    print("module __name__:",__name__)
    test()


# if this progam executes as a main program then the __name__ variables values is set to __main__,
#else the value is set to the name of the program i.e module