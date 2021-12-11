"""
Класс двумерного метода


>>> v1 = Vector2d(3, 4)
>>> print(v1)
(3.0, 4.0)
>>> v1
Vector2d(3.0, 4.0)

>>> v1_clone = eval(repr(v1))
>>> v1 == v1_clone
True

Test of frombytes method

>>> octets = bytes(v1)
>>> v1_clone = Vector2d.frombytes(octets)
>>> v1_clone == v1
True

>>> abs(v1)
5.0

>>> bool(v1), bool(Vector2d(0,0))
(True, False)

Test of the angle Method

>>> Vector2d(0, 0).angle()
0.0
>>> Vector2d(1, 0).angle()
0.0

Tests of hashing
>>> v1 = Vector2d(3, 4)
>>> v2 = Vector2d(3.1, 4.1)
>>> hash(v1), hash(v2)
(7, 6175)
>>> len({v1,v2})
2


"""

from array import array
import math

class Vector2d:
    
    @classmethod
    def frombytes(cls, octets):
        typecode  =chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    
    typecode = 'd'
    
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)
        
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
        
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)])+
                bytes(array(self.typecode,self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    def angle(self):
        return math.atan2(self.y, self.x)
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
        
if __name__ == "__main__":
    import doctest
    v = Vector2d(1,2)
    doctest.testmod()
