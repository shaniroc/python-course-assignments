"Second lesson"
# greeting= "Hello, World again!"
# print(greeting)

# height = 1.75
# weight = 68.0
# bmi = weight / (height**2)
# print("bmi:", bmi)

#name = "John Lee"
# name = input("Enter your name: ")
# print(f"Hello, {name}!") #f tells to python to put inside the curly {} to input the name

# a = 2
# print(a)
# print(type(a))
# print("a+1.5")
# print(type(a+1.5))


# def main():
#     expected_answer = "42"
#     inp = input('What is the answer? ')

#     if inp == expected_answer:
#         print("Welcome to the cabal!")
#         print("Still here")

#     print("This always happens")

# main()

# def main():
#     expected_answer = "42"
#     inp = input('What is the answer? ')

#     if inp == expected_answer:
#         print("Welcome to the cabal!")
#     else:
#         print("Read the Hitchhiker's guide to the galaxy!")

#     print("This always happens")

# main()

# def main():
#     a = input('First number: ')
#     b = input('Second number: ')

#     if int(b) == 0:
#         print("Cannot divide by 0")
#     else:
#         print("Dividing", a, "by",  b)
#         print(int(a) / int(b))

#     print("Still running")


# main()

# import sys

# def main():
#     if len(sys.argv) != 3:
#         exit("Needs 2 arguments:  width length")

#     width  = int( sys.argv[1] )
#     length = int( sys.argv[2] )

    

#     if length <= 0:
#         exit("length is not positive")

#     if width <= 0:
#         exit("width is not positive")

#     area = length * width
#     print("The area is ",  area)

# main()


import random

print( 1 + int( 6 * random.random() ))

print(random.randrange(1, 7))

# One of the following: 1, 2, 3, 4, 5, 6
