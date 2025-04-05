#Write a program called rectangle.py that will ask the user for height and width 
# and calculate the area and the perimeter of the rectangle.

height_width = list(map(float,input("Enter the height and width of the rectangle separated by space: ").split()))
area = round(height_width[0] * height_width[1],3)
perimeter = round(2*height_width[0] + 2*height_width[1], 3)
print(f"The area of your rectangle is: {area} and its perimeter is: {perimeter}")