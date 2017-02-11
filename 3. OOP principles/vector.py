class vector():
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return 'Vector<%0.3f, %0.3f, %0.3f>'%(self.x, self.y, self.z)

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        if isinstance(other, vector):
            return vector(self.x+other.x,
                          self.y+other.y,
                          self.z+other.z)
        else:
            raise Exception("Not supported type %s" % type(other))

    def __sub__(self, other):
        if isinstance(other, vector):
            return vector(self.x-other.x,
                          self.y-other.y,
                          self.z-other.z)
        else:
            raise Exception("Not supported type %s" % type(other))

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return vector(self.x * other, self.y * other, self.z * other)
        elif isinstance( other, vector):
            return vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __call__(self):
        return (self.x, self.y, self.z)

    def __getitem__(self, item):
        if isinstance(item, int):
            if 0 <= item <=2:
                if item == 0:
                    return self.x
                elif item == 1:
                    return self.y
                elif item == 2:
                    return self.z
            else:
                raise Exception('Value out of range, use 0, 1 or 2')
        else:
            raise Exception('Index value mast be int')

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if key in [0,1,2]:
                if key == 0:
                    self.x = value
                elif key == 1:
                    self.y = value
                elif key == 2:
                    self.z = value
            else:
                raise Exception('Value out of range, use 0, 1 or 2')
        else:
            raise Exception('Index value mast be int')

    def __len__(self):
        return int(self.mag())

    def cross(self, other):
        if isinstance(other, vector):
            return vector(self.y*other.z - self.z*other.y,
                 self.z*other.x - self.x*other.z,
                 self.x*other.y - self.y*other.x)
        raise Exception("Not supported type %s" % type(other))

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def mag(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5



        
v1 = vector(9, -14, 13.14)
v2 = vector(0, 0, 10)

print v1    # __str__
print v1()    # __call__
print v1 + v2    # __add__
print v1 - v2    # __sub__
print v1 * 10    # __mul__
print v1 * v2    # __mul__
print v1[0]    # __getitem__
v2[0] = 999    # __setitem__
print v2
print len(v1)    # __len__ (int, not float)
print v1.mag()    # Exact length, as float
