#Write a program called circle.py that will ask the user for the radius of the circle 
# and will print the area and the circumeference of the circle.

# Copy the circle.py and rectangle.py from day02 to day03 and change both of them to
#  get the values one the command line (using sys.argv) intead of waiting for input.

import math
import sys

def main():
    if len(sys.argv) != 2: #Checking if there is enough arguments
        exit("You should enter the radius of the circle")
    #Converting the radius argument into float
    radius = float(sys.argv[1])
        
    #Making sure that the given value is not equal to 0 or negative
    if radius <= 0: 
        exit("Radius is not positive")
        
    # Calculate area and circumeference
    area = round(math.pi * (radius**2),3)
    circumeference= round(radius*2*math.pi, 3)
    print(f"The area of your circle is: {area} and its circumeference is: {circumeference}")

main()