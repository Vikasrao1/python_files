# Problem 2

class Cylinder:
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi * (self. radius ** 2) * self.height # formula pi * r * 2 * h
    
    def surface_area(self):
        #return self.radius * self.pi ** 2 * self.height 
        return((2* self.pi *self.radius) * self.height) + ((self.pi*self.radius**2)*2)

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
  
# Problem 1 Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return((x2 - x1 ** 2 + (y2 - y1) ** 2)) ** 0.5
        #((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1) / (x2-x1)
coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

# OOP Challenge - create a bank account class that has two attributes: Owner, balance
# and two methods deposit, withdraw
# withdrawls may not exceeds the available balance

class Account:
    def __init__(self, owner, balance):
         self.owner = owner
         self.balance = balance

    def deposit(self,dp_amt):
        self.balance = self.balance + dp_amt
        print("Deposit Accepted")

    def withdrawl(self,wdl_amt):
        if self.balance >= wdl_amt:
           self.balance-=wdl_amt
           print("Withdrawl Accepted")
        else:
           print("Funds Unavailable!")

    def __str__(self):
         return f"Account owner: {self.owner}\nAccount balance ${ self.balance:}"
    
   
#print the object
acct1 = Account('Jose',100)
print(acct1)

# show the account owner attribute
print(acct1.owner)

# show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdrawl(75)

#6 Make a withdraw that exceeds available balance

acct1.withdrawl(500)




        
