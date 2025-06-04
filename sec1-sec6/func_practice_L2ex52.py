# FIND 33 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# ex: has_33([1, 3, 3]) → True

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==3 and nums [i+1]==3:
            return True
    return False
print(has_33([1, 3, 3]))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    result= ''
    for char in text:
        result += char * 3
    return result
    
print(paper_doll('Hello'))


