# def myfunc(a,b):
#     #return 5 % of the sum of a & b
#     return sum(a,b) * 0.05
# print(myfunc(80,100))

# *args example

def myfunc(*args):
    return sum(args) * 0.05
print(myfunc(20,40,50,60,70))

# **kwargs example

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit of choice is{}'.format(kwargs['fruit']))
    else:
        print('I did not get any fruit here')

myfunc(fruit='apple')