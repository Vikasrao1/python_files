# map function - applying sqare
def square(num):
    return num **2 
my_nums=[1,2,3,4,5]
for item in map(square,my_nums):
    print(item)

# another example for map
def splicer(mystring):
    if len(mystring)%2 ==0:
        return 'Even'
    else:
        return mystring[0]
names=['John', 'Sam','Alyssa']
print(list(map(splicer, names)))

# Filter function
def check_even(num):
    return num %2 ==0
my_nums=[1,2,3,4,5]
for n in filter(check_even,my_nums):
    print(n)

# Lambda function (Lambda's are anonymos function typically we don't name them

names2=['Raj', 'Sally', 'James']
result=map(lambda x:x[0],names2)
print(list(result))
