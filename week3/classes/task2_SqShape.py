#task2
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

x = int(input())
y = int(input())

randomsq = Square(x)
squarea = randomsq.area()
print(f"Area of the square: {squarea}")

