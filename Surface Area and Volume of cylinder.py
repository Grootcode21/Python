from math import pi

h = int(input("Enter a height: "))
r = int(input("Enter a radius: "))
s_area = 2 * pi * r ** 2 + 2 * pi * r * h
volume = pi * r ** 2 * h
print("Surface Area =", s_area, " & Volume =", volume)
