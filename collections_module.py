# collection module - built-in module that proves specialized conatiner data types.
# Counter - Is a dict subclass which helps count hashable objects.

from collections import Counter
#Counter with lists

lst = [1,2,2,2,2,3,3,3,3,1,12,3,2,32,132]
print(Counter(lst))

#Counter with strings
string =('aabsbsbhshhbbsbs')
print(Counter(string))

# Counter with a word in a sentense 
sentence = 'How many times does each word show up in this sentence word times each word'
words = sentence.split()
print(Counter(words))

#namedtuple - quick way of creating a new object or class with some attoibute fields.

from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=3, breed='Lab', name='sams')
frankie = Dog(age=3, breed='Shepard', name="Frankieee")

print(sammy)
print(sammy.age)
print(sammy.breed)