
import math

def sphere_volume(r):
    v = (4/3) * math.pi * r**3
    return v



radius = float(input("Enter the radius: "))
result = sphere_volume(radius)
print("Volume of the sphere: {:.2f}".format(radius, result))