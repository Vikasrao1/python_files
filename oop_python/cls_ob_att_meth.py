# Class, Object, Attributes and Methods

class Dog():

    # CLASS OBJECT ATRIBUTE
    # SAME FOR ANY KEYWORD OF CLASS

    species ='Mammal'
    def __init__(self, breed, name):
        # we take in a argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        # Operations/Actions --> Methods
    def bark(self,number):
            print("WOOF! My name is {} and the is {}".format(self.name,number))

my_dog = Dog('Lab', 'Frankie')
type(my_dog)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)

my_dog.bark(10)

# NEW CLASS

class Circle():
     # class object attibute
     pi = 3.14

     def __init__(self, radius=1):
          self.radius = radius
    
     def get_circumference(self):
          return self.radius * self.pi * 2
my_circle = Circle(30)

print(my_circle.radius)

print(my_circle.get_circumference())
