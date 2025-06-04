# Funcions
def say_hello():
    print("how")
    print("are")
    print('you')
say_hello()
#overring the function
def say_hello(name):
    print(f'Hello {name}')
say_hello('John')

# example return statement
def add_num(a,b):
    return(a+b)
print(add_num(11,12))
result=add_num(11,12)
print(result)

#
def even_check(number):
    return number %2 ==0
print(even_check(20))

#Return true if any number is even inside the list
def check_even_num(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
print(check_even_num([1,2,5]))