# Shuffle function
example = [1,4,6,7,8,10]
from random import shuffle
shuffle(example)
print(example)

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list
result=shuffle_list(example)
print(result)
