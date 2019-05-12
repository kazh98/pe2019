import math

class Vector(object):
    def __init__(self, arr):
        self.arr = arr

    def sub(self, vec):
        return Vector([self.arr[i] - vec.arr[i] for i in range(len(self.arr))])
    
    def p_norm(self, p):
        return sum([abs(e) ** p for e in self.arr]) ** (1 / p)
    
    def inf_norm(self):
        return max([abs(e) for e in self.arr])


n = int(input())
x = Vector([int(e) for e in input().split()])
y = Vector([int(e) for e in input().split()])
z = x.sub(y)

print(z.p_norm(1))
print(z.p_norm(2))
print(z.p_norm(3))
print(z.inf_norm())
