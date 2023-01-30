n = int(input("Enter a number: "))
if n < 60:
    ast = "*"
    for i in range(1, n + 1):
        print(ast * i)
else:
    print("Wrong number")
