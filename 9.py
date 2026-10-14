class herbivore:
    def eat_plant(self):
        print("this animal eat only plant")

class carnivore:
    def eat_meat(self):
        print("This animal eat meat")

class omnivore:
    def eat_both(self):
        print("this animal eat both plant and meat")

class bear(herbivore,carnivore,omnivore):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Bear Name",self.name)
        print("Bear Age",self.age)

b1 = bear("gogo",21)

b1.display()
b1.eat_plant()
b1.eat_meat()
b1.eat_both()
