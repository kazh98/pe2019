import math


class Triangle(object):
    def __init__(self, a, b, C):
        self.a = a
        self.b = b
        self.C = C * math.pi / 180

    def getHeight(self):
        return self.b * math.sin(self.C)

    def getArea(self):
        return (self.a * self.getHeight()) / 2
    
    def getPerimeter(self):
        return self.a + self.b + math.sqrt(self.a ** 2 + self.b ** 2 - 2 * self.a * self.b * math.cos(self.C))


a = [int(e) for e in input().split()]
tri = Triangle(a[0], a[1], a[2])
print(tri.getArea())
print(tri.getPerimeter())
print(tri.getHeight())
