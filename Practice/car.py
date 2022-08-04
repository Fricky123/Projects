class Car:
    def __init__(self, Brand, Manufacturer, Model, Year, Type):
        self.Brand = Brand
        self.Manufacturer = Manufacturer
        self.Model = Model
        self.Year = Year
        self.Type = Type

    def Start(self):
        print("Car engine has started")

    def Go(self):
        print("Car is now in forward motion...")

    def Stop(self):
        print("Car has now stopped...")