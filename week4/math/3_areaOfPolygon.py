'''Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625'''

from math import tan, pi

sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

area = sides * (length ** 2) / (4 * tan(pi / sides))
res = round(area,4)

print("The area of the polygon is: ",res)