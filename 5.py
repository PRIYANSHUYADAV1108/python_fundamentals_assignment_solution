class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        print("BRAND = ",self.brand)
        print("MODEL = ",self.model)

class car(vehicle):
    def __init__(self,brand,model,seat):
        super().__init__(brand,model)
        self.seat = seat
    def display(self):
        super().display()
        print("SEAT = ",self.seat)


class bike(vehicle):
    def __init__(self,brand,model,engine):
        super().__init__(brand,model)
        self.engine = engine
    def display(self):
        super().display()
        print("ENGINE = ",self.engine)
car1 = car("Toyota", "Innova", 7)
bike1 = bike("Royal Enfield", "Classic 350", 350)

print("CAR DETAILS")
car1.display()

print("\n BIKE DETAILS")
bike1.display()

