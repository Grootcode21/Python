import time


# fxn to demonstrate printing pattern
def pypart(n):
    # outer loop to handle the no. of rows
    for i in range(0, n):

        # inner loop to handle the no. of columns
        for j in range(0, i + 1):
            # print stars
            print("*", end="")

            # 1-sec delay
            time.sleep(1)

        # end line after each row
        print("\r")


# driver code
n = 5
pypart(n)
