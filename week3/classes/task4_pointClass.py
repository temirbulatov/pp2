#task4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coords: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

p1 = Point(1, 2)
p1.show()
p1.move(5, 6)
p1.show()


#task4
'''
Point Class
Show() - should represent current location of the point on 2d plane. Coordinates x and y should represent it, can be displayed through the use of 
array of arrays that are limited by 'i' and 'j', then x coordinate location of the point limited by "0 <= x <=i", and y accordingly "0 <= y <=j" .  

Move() - should represent the change of the location of the point along two axises. + or - 1 (or more) but limited by 0 and 'i' (maximum value) for x coordinate; 
+ or - 1 (or more) but limited by 0 and 'j' (maximum value) for y coordinate. Only use of substraction and addition is suitable, not multiplying or division.

Dist() - done through separate calculation of the change in x1 and x2, y1 and y2. Then, trough the use of algebraic formula of Pythagoras Theorem:
Distance = ((x2-x1)^2+(y2-y1)^2)^(1/2). (where x2 and y2 are the highest coordinates among two points, and x1 and x2 vice versa, the smallest ones).
'''