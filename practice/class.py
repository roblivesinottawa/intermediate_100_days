class Vehicle:
    def __init__(self):
        self.fuel = "gas"
        self.color = "black"

    
    def terrain(self):
        print("all terrain vehicle")

    def tire_type(self):
        print("all Season tires")



class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.can_be_financed = True

    def terrain(self):
        super().terrain()
        # print("runs smoothly on all terrains")
        super().tire_type()


car = Truck()
car.terrain()