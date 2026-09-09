class Animal:
    name = ''

    def eat(self):
        print('I can eat')
# inherit from Animal
class Dog(Animal):
     # new method in subclass
     def display(self):
         print('My name is', self.name)

# create an object of the subclass
labrador = Dog();

labrador.name='KIKI'
labrador.eat()

#call subclass method
labrador.display();