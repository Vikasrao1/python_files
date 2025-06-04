# Inheritance and Polymorphism 
# Inheritance- Way to form new classes using classes that have already been defined

class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
    
    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I'm eating")
    
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    
    # def who_am_i(self):     #BEFORE OVERRING 
    #     print("I'm a dog!")
    def eat(self):
        print("I'm A dog and eating")
    
    
#my_animal = Animal()
my_dog = Dog ()
my_dog.eat()
my_dog.who_am_i()

# Polymorphism ------------------(Optional/won't really use it until much later)
# It refers to the way in which different object classes can share the same method name and the methods can be called from same place!

class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak (self):
        return self.name + " says woof!"

class Cat():
    def __init__(self, name):
        self.name = name
    
    def speak (self):
        return self.name + " says meow!"
    
    
niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())
        
       