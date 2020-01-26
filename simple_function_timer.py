import time

def time_it(fn,*args,**kwargs):
    print(args,kwargs)

time_it(print,)