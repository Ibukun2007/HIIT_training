for i in range(1,201):
    if i % 5 ==0:
        print(i)

"""
word example of for loop
"""


class_list = ["David", "Samuel", "Israel"]
for person in class_list:
    print(person)


"""
while loop
"""

number = 1
while number < 10:
    print(number)
    increment= number + 1
    number = increment

# or we can do it as

number = 1
end = 10
while number < end +1:
    print(number)
    increment= number + 1
    number = increment

#using while loop to go through a word list
class_length = len(class_list)
start=0
while start < class_length:
     print(class_list[start])


#task
print("Odd numbers:")
for i in range(1,101,2):
        print(i)
