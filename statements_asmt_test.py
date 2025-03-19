# print only the words that start with 's', Use for , split() and if 
st= 'Print only the words that start with s in this s sentence'
for word in st.split():
    if word[0]=='s':
        print(word)
 # Use range() to print all the even numbers from 0 to 10.
#mylist=[0,1,2,3,4,5,6,7,8,9,10]
#for range in mylist:
#        if range %2 ==0:
#            print(range)
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# for i in range(0,50):
#     if i % 3 ==0:
#         print(i)

# Go through the string below and if the length of a word is even print "even!"
stmt = 'Print every word in this sentence that has an even number of letters'
for word in stmt.split():
    if len(word)%2==0:
        print("even!")

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,101):
    if num % 3 ==0 and num %5==0:
        print("FizzBuzz")
    elif num % 3 ==0:
        print("Fizz")
    elif num % 5 ==0:
        print("Buzz")
    else:
        print(num)


#
st= 'Use List Comprehension to create a list of the first letters of every word in the string below:'
for word in st.split():
    print(word[0])
    
              

