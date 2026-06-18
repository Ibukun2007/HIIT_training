class rectangle:
    color = "red" # creating an attribute inside a class itself
    def __init__(self, length, breadth):
        self.length = length


obj1 = rectangle(length=30, breadth=60)

print(obj1.length)
