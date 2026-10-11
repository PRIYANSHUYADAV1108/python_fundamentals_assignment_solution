class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)


# 1. Name only
p1 = Person("Rahul")

# 2. Name + Age
p2 = Person("Amit", 20)

# 3. Name + Age + Address
p3 = Person("Priyanshu", 20, "Patna")


# Display details
print("Person 1:")
p1.display()

print("\nPerson 2:")
p2.display()

print("\nPerson 3:")
p3.display()
