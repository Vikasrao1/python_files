# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a % 2 ==0 and b % 2 ==0:
        # BOTH NUMBERS ARE EVEN
        if a < b:
            result= a                          #min/max function result =min(a,b)
        else:
            result= b
        # if one or both are odd
    else:
        if a > b:
            result=a
        else:
            result=b
    return result

#CHECK

print(lesser_of_two_evens(11,13))
        
# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(string):
    s1, s2 = string.split(' ')
    return(s1[0].upper()== s2[0].upper())
print(animal_crackers('Level Two'))

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1,n2):
    if n1 + n2 == 20 or n1== 20 or n2 == 20:
        return True
    else:
        return False
print(makes_twenty(10,10))
