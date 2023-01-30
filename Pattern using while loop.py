n = 5

i = 1
j = 0

while i <= n:
    while j <= i - 1:
        print("* ", end="")
        j += 1
    print("\r")
    j = 0
    i += 1

m = 3
i = 0
while i <= m:
    print(" " * (m - 1) + "*" * i)
    i += 1
