#methods are functions inside classes or behaviours that can have
class car:
 
    def __init__(self, color, brand, max_speed, year):
        self.color = color
        self.brand = brand
        self.max_speed = max_speed
        self.year = year

    def print_properties(self):
        print(f"color: {self.color}")
        print(f"Brand: {self.brand}")
        print(f"Max_speed: {self.max_speed}")
        print(f"year: {self.year}")

    def get_color(self):
        print(f"color: {self.color}")


my_car1 =car(color="yellow", brand="Mazda", max_speed="500km/hr", year="1970")
my_car1.print_properties()
print("")
my_car1.get_color()