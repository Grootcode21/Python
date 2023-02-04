from math import pi


def circum(r):
    circum = 2 * pi * r
    return circum


r = int(input("Enter the radius: "))
print("Circumference = ", circum(r))
