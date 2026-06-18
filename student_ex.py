class student:
    def __init__(self, first_name, last_name, middle_name, age, department):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.age = age
        self.department = department

    def fullname(self):
        print(f"fullname: {self.last_name} {self.first_name} {self.middle_name}")

Student1 = student(first_name="Ibukun", last_name="Osinuga", middle_name="Adejare", age="19", department="Python prog..")

print(Student1.first_name)
print(Student1.last_name)
print(Student1.middle_name)
print(Student1.age)
print(Student1.department)
print("")
Student1.fullname()