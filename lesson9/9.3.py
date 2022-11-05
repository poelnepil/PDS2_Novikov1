class Parallelogram(object):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def get_area(self):
        return self.length * self.width

class Square(Parallelogram):
    def get_area_s(self):
        if self.width == self.length:
            return self.width**2
        else:
            return 'square has equal sides'

p = Parallelogram(2,4)
print(p.get_area())

s = Square(7,7)
print(s.get_area_s())