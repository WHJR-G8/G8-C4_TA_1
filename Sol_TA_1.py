import turtle

length = int(input("Enter the value for length: "))
breadth = int(input("Enter the value for breadth: "))

for i in range(2):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(breadth)
    turtle.left(90)
