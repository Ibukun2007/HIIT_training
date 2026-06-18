class car:
    color = "red"
    brand = "Lexus"
    max_speed = "200km/hr"
    year = "1970"

    def __init__(self, color, brand, max_speed, year):
        self.color = color
        self.brand = brand
        self.max_speed = max_speed
        self.year = year

my_car1 =car(color="yellow", brand="Mazda", max_speed="500km/hr", year="1970")
my_car2 =car(color="pink", brand="maruwa", max_speed="400km/hr", year="1930" )
my_car3 =car(color="indigoe", brand="korope", max_speed="300km/hr", year="1999" )

print(my_car1.color)
print(my_car1.brand)
print(my_car1.max_speed)
print(my_car1.year)
print("")
print(my_car2.color)
print(my_car2.brand)
print(my_car2.max_speed)
print(my_car2.year)
print("")
print(my_car3.color)
print(my_car3.brand)
print(my_car3.max_speed)
print(my_car3.year)