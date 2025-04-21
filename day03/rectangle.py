#Write a program called rectangle.py that will ask the user for height and width 
# and calculate the area and the perimeter of the rectangle.

# Copy the circle.py and rectangle.py from day02 to day03 and change both of them to
#  get the values one the command line (using sys.argv) intead of waiting for input.

import sys

def main():
    if len(sys.argv) != 3: #Checking if there is enough arguments
        exit("You should enter two values; Height; Width")
    #Converting the arguments into float
    height = float(sys.argv[1])
    width = float(sys.argv[2])
    
    #Making sure that the values ​​are not equal to 0 or negative
    if height <= 0: 
        exit("Height is not positive")

    if width <= 0:
        exit("Width is not positive")
        
    # Calculate area and perimeter
    area = round(height * width, 3)
    perimeter = round(2 * height + 2 * width, 3)
    print(f"The area of your rectangle is: {area} and its perimeter is: {perimeter}")

main()

#When using sys.argv, the numbers come from the command line arguments 
# (the name of the file + two values)