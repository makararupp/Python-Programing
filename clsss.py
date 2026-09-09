class Dog:
    def __init__(self, name, breed):
        self.name = name;  # instance attribute
        self.breed = breed;

    def bark(self):
        return f"{self.name} say Woof!"

# Creating objects (instance)
dog1 = Dog("Rex","Labo")
dog2 = Dog("Dara","Seyha")

print(dog1.bark())
print(dog2.name)
