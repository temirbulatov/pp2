#task3
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

x = int(input())
y = int(input())

randomsq = Square(x)
squarea = randomsq.area()
print(f"Area of the square: {squarea}")

randomsh = Shape()
sharea = randomsh.area()
print(f"Area of the shape: {sharea}")

randomrec = Rectangle(x, y)
recarea = randomrec.area()
print(f"Area of the rectangle: {recarea}")