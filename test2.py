# String properties and methods
names = "Pam"
last_letters = names[1:]  # Get all letters except the first one
print('P' + last_letters)  # Concatenate 'P' with the remaining part

#multiplication
letter = 'z'
print(letter * 10)  # Multiply the letter 10 times

#converting string to upper case
x = "Hello World"
print(x.upper())

# to split before i
print(x.split('e'))
# string formatting
print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick')) #other way

#Coding exercise
#Write an expression using any of the string formatting methods we have learned (except f-strings, see note below) to return the phrase 'Python rules!' 
print('Python {r}'.format(r='rules!'))

#Lists
my_list =['a','e','b','d','o']
my_numbers=[4,3,2,2,0]
#print(my_list.sort()) #sorts the list
#print(my_list)
print(my_list.pop())  #removes the last element
print(my_list)