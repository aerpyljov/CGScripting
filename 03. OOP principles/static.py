class someClass(object):
    x = 123    # static value
    
    def __init__(self, z):
        self.y = 321
        self.z = z
    
    @staticmethod
    def someMethod():
        pass

        
obj1 = someClass(8)
obj2 = someClass(0)      
        
print obj1.x, obj1.y, obj1.z
print obj2.x, obj2.y, obj2.z


print 'Changing x, y, z for obj1...'

obj1.x = 100    # Makes new variable, doesn't change the class variable
obj1.y = 200
obj1.z = 300

print obj1.x, obj1.y, obj1.z
print obj2.x, obj2.y, obj2.z

print 'Changing x by __class__ for obj1...'

obj1.__class__.x = 50

print obj1.x, obj1.y, obj1.z   # Variable x is not static, because redefined earlier
print obj2.x, obj2.y, obj2.z   # Variable x is static

print 'Changing x by someClass.x...'

someClass.x = 99

print obj1.x, obj1.y, obj1.z   # Variable x is not static, because redefined earlier
print obj2.x, obj2.y, obj2.z   # Variable x is static
        




class countClass(object):
    count = 0
    
    def __init__(self):
        self.__class__.count += 1
        

a = countClass()
b = countClass()
c = countClass()

print 'Number of countClass instances: {0}'.format(countClass.count)



"""        
v = someClass.someMethod()    # Useful if the method returns the class instance in a specific state
x = someClass.staticValue    # Useful if there is no instances of the ckass
"""
