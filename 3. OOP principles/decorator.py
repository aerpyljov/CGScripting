# The idea of decorators without specific syntax

def decorator(f1):
    def wrapper(arg):
        print 'before'
        f1(arg)
        print 'after'
    return wrapper
    

def f1(arg):
    print arg
    
    
print '...Call a function without decorators...'
   
f1(12)

print '...Decorators without specific syntax...'

f1 = decorator(f1)
f1(17)



# Specific syntax for decorators

print '...Decorators with specific syntax...'

@decorator
def f2(x):
    print 'function', x

f2(22)

