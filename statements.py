# if & elif else statements
hungry= True
if hungry:
    print('feed me')
else:
    print('I am not hungry')
# example
location="Bank"
if location == "Firestone auto shop":
 print("cars are cool")
elif location=="Bank":
 print("money is cool")

else:
   print("you're not in the right place")
 
# For loops (iterating through a list)
mylist=[1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)
#check for even numbers
for num in mylist:
   if num % 2==0:
      print(num)
   else:
      print(f'odd number: {num}')
#sum of numbers
list_sum=0
for num in mylist:
   list_sum=list_sum+num

print(list_sum)
# another example
tup=[(1,2),(3,4),(5,6)]
for a,b in tup:
   print(a)
   
