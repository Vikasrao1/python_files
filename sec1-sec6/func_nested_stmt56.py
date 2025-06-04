# nested statement example
name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    # nested function
    def hello():
        print('Hello '+name)
    
    hello()

greet()