class Rectangle:
    length=0
    breadth=0
    def __init__(self,a,b):
        self.length = a
        self.breadth = b
    def Area(self):
        self.answer = self.length * self.breadth
        return self.answer
obj = Rectangle(8,9)
print(obj.Area())
