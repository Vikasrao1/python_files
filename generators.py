# Allow us to generate sequence of values over time
# Problem 1 Create a generator that generates the squares of numbers up to some number N.
def gensquares(N):
    for num in range(N):
        yield num **2
    
for x in gensquares(10):
    print(x)

#problem 2 Create a generator that yields "n" random numbers between a low and high number (that are inputs).
import random

def get_random(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for num in get_random(1,9, 5):
    print(num)

# problem 3 : Use the iter() function to convert the string below into an iterator

s = 'hello'
s = iter(s)
print(next(s))
