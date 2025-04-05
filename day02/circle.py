#Write a program called circle.py that will ask the user for the radius of the circle 
# and will print the area and the circumeference of the circle.

import math
print(math.pi)

radius = float(input("Hello! Please write down the radius of the circle: "))
area = round(math.pi * (radius**2),3)
circumeference= round(radius*2*math.pi, 3)
print(f"The area of your circle is: {area} and its circumeference is: {circumeference}")