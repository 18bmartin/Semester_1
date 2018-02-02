import math

y = input("trigonometry or pythagoras? (T or P): ")
if y == "P":
    x = input("finding hypotenuse or a side? (H or S): ")
    if x == "H":
        a = int(input("first side of the triangle length: "))
        b = int(input("second side of the triangle length: "))
        c = math.sqrt(a ** 2 + b ** 2)
        print("the hypotenuse length is:", c)
    elif x == "S":
        a = int(input("Hypotenuse length: "))
        b = int(input("second side of the triangle length: "))
        c = math.sqrt(a ** 2 - b ** 2)
        print("the side length is:", c)
elif y == "T":
    x = x
else:
    exit(0)

