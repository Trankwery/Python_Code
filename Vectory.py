class Vector():

    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return 'Vector: [{},{},{}]'.format(self.x,self.y,self.z)

    def __add__(self,b):
        if type(b) == Vector:
            return Vector(self.x+b.x, self.y+b.y, self.z+b.z)

a=Vector(12,3,-7)
b =Vector(2,3,-5)
