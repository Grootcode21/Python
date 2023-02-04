from array import *

arr = array('i', [-1, 2, 2, 3, 4, 5])
print(arr[4])
print(arr.index(2))

arr_1 = array("i", [])
x = int(input("enter size of array: "))
print("enter %d elements: " % x)
for i in range(x):
    n = int(input())
    arr.append(n)
print(arr_1)
