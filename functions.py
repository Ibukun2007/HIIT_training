def greet(name):
    print(f"Hello, {name}!")

greet("Ibukun")
greet("Adejare")
greet("Odufua")

def add_multiply(a, b, c, d):
    print(a+b*c/d)

add_multiply(15, 4, 5, 5)
add_multiply(20, 6, 7, 2)

#return statement
def division(a, b):
    return a/b
    print('hello world')
#and statement or command after return is invalid, it'll not show when you run
result = division(20, 5)
print(result)

def add(a, b):
    return a+b

result = add(20, 5)
print(result)

#default parameter
def greet(name="Anon user"):
    print(f"Hello, {name}!")

greet()
greet("Ibk")

