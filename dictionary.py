#Dictionary is a key - value pairs
table = {"name": "Table 1", "Height": "10cm", "width": 25, "Color": "red"}

"""
# dictionary = {"key": "value"}
# key is always a string 
# value is any valid data type

"""


Color = table.get("Color")
print(Color)

print("Before adding names")
print(table)
print("")
table["names"] = ["Name 1", "Name 2", "Name 3", "Name 4"]

print("")
print("After adding names")
print(table)



#task
person = {}

person["Name"] = input("Enter the name of the person: ")
person["Age"] = input("Enter the age of the person: ")
person["Height"] = input("Enter the height of the person: ")
person["Weight"] = input("Enter the weight of the person: ")

print(person)

print(f"the name of the person is: {person.get('Name')}")
print(f"the age of the person is: {person.get('Age')}")
print(f"the height of the person is: {person.get('Height')}")
print(f"the weight of the person is: {person.get('Weight')}")