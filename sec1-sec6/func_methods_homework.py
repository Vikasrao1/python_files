# Write a function that computes the volume of a sphere given its radius.
# volume of the spehre given as V = 4/3 pi r * r * r

# def vol(rad):
#     #define the value of the pi
#     pi=3.14159
#     #define the radius of the sphere
#     rad=6.0
#     # Calculate the volume of the sphere using the formula
#     vol= 4.0/3.0 * pi * rad **3

# print(f"The volume of the sphere is, vol{2}")

#Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):
    # 5,2,7
   
    if low <=num <=high:
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is NOT in the range between {low} and {high}')
ran_check(12,2,7)

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    s='Hello Mr. Rogers, how are you this fine Tuesday?'
    lower_count= sum(map(str.islower, s))
    upper_count=sum(map(str.isupper, s))
    up_low(s)


    
    
