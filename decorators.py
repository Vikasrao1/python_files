#Decorators - Allows us to decorate a function
def hello(name='James'):
    print("The hello() function has been executed")

    def greet():
        return '\t this is a greet function inside hello!'
    
    def welcome():
        return '\t this is a welcome function inside hello!'
    
    print("I'm going to return a function")

    if name == 'James':
        return greet
    else:
        return welcome

my_new_func = hello('James')
print(my_new_func()) #prints results of greet

# defining the func that contains another func inside it & returns that inner func

def new_decorator(original_func):
    def wrap_func():
        print('some extra code, before the original function')

        original_func()
        print('Some extra code, after the original function!')
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated!')

func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)

decorated_func()

#we get same result with this func/key_word
@new_decorator
def func_needs_decorator():
    print('I want to be decorated!')

func_needs_decorator()




    