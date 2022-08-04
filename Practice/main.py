from car import car

# Name, Brand, Manufacturer, Model, Year, Type

car1 = car("Itali GTO", "Itali", "Itali Auto Manufacturers", "3000", 2022, "Sports Car")
car2 = car("Bravado Gallivanter", "Bravado", "Someone's garage", "GTR", 1930, "Rocketship")


print(car1.year)

car1.stop()
car2.go()