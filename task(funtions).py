def add(a, b):
    return a+b

def minus(a, b):
     return a-b

def divide(a, b):
     return a/b

def multiply(a, b):
     return a*b

a= int(input("enter a number: "))
b= int(input("enter another number: "))


add_result = add(a,b)
minus_result = minus(a,b)
divide_result = divide(a,b)
multiply_result = multiply(a,b)

print(f"the result is: {add_result}")
print(f"the result is: {minus_result}")
print(f"the result is: {divide_result}")
print(f"the result is: {multiply_result}")


try:
    x = float(a)
    y= float(b)


    add_result = add(x,y)
    rounded = round(add_result, 2)
    #print(f"the result is: {add_result:.3f}")
    #print(f"rounded {rounded}")

    print(f"the sum is: {add(x,y)}")
    print(f"the subtraction is: {minus(x,y)}")
    print(f"the division is: {divide(x,y)}")
    print(f"the product is: {multiply(x,y)}")
except:
    print("An error occured")

