
from arithmetic import add, minus, divide, multiply, name

try:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))

    print (f"The sum is: {add(a,b)}")
    print (f"The sum is: {minus(a,b)}")
    print (f"The sum is: {divide(a,b)}")
    print (f"The sum is: {multiply(a,b)}")
except ValueError:
    print("An error occured")



print(name)