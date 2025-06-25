## Problem 1 Handle the exception thrown by the code below by using try and except blocks.

for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print(f"TypeError can't perform i**2 when i is {i}")

# problem 2 Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
x = 5
y = 0
try:
    z = x/y
except:
    print(f"Can't perform x/y when y is {y}")
finally:
    print("All Done.")

# problem 3 Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            result = int(input("Enter a integer "))
        except:
            print("that is not an integer/incorrect input")
            continue
        else:
            print(f"the square root of {result} is {result **2}")
            break
ask()