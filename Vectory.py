class Vector():

    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self,v):
        x = self.x + v.x
        y = self.y + v.y
        return Vector(x,y)
    
    def __repr__(self):
        return 'Vector: [{},{}]'.format(self.x,self.y)

a =Vector(1,2)
b = Vector(10,12)
c = Vector(11,2)
d = Vector(1,12)

z = a + b + c + d
print(z.x,z.y)
