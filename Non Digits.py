n = input("n: ")
while any(c.isdigit() for c in n):
    n = input("enter a non-digit: ")
    print(n)
