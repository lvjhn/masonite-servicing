from masonite_servicing import * 

def add(a, b): 
    c = a + b  
    return relay(ok("ADDED", c))

def subtract(a, b): 
    c = a - b 
    return relay(ok("SUBTRACTED", c)) 

def multiply(a, b):     
    c = a 
    for a in range(b): 
        c = add(c, a).get() 
    return relay(ok("MULTIPLIED", c))

def divide(a, b):     
    c = a 
    for a in range(b): 
        c = subtract(c, a).get() 
        if c < 0: 
            c = 0
            break 
    return relay(ok("MULTIPLIED", c))
