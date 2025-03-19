x = 0
while x <5:
    print(f'the current value of x is {x}')
    x = x+1
else:
    print('x is not less than 5')
# continue example
mystring='Banana'
for letter in mystring:
    if letter=='n':
        continue
    print(letter)
# zip example
mylist=[1,2,3]
mylist2=['a','b','c']
mylist3=[100,200,300]
for item in zip(mylist,mylist2,mylist3):
    print(item)
# input example
output = input('Favourite number:')
print(output)
# Nested loops
mylist=[]
for x in [2,4,6]:
    for y in [50, 100, 150]:
        mylist.append(x*y)
        print(mylist)
