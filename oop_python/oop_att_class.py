# OOP python

# class Sample():
#     pass
# my_sample = Sample() #creating instance of class
# print(type(my_sample)) 

class Dog():
   
    def __init__(self, breed, name, spots):
        # we take in a argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        #Expect boolean TRUE/FALSE
        self.spots = spots

my_dog = Dog(breed= 'Huskie',name='Sammy', spots=False)
type(my_dog)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)