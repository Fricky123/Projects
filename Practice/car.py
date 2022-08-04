

class car:
    def __init__(self, name, brand, manufacturer, model, year, type):
        self.name = name
        self.brand = brand
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.type = type

    def start(self):
        print(f"{self.name}'s engine has started")

    def go(self):
        print(f"{self.name} is now in forward motion...")

    def stop(self):
        print(f"{self.name} has now stopped...")
