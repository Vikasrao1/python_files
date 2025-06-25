# Try, except, Finally (idea behind these stmts even if error happens we're going to try to do that block of code/continue with somemore code)

try:
    f = open('testfile' ,'w')
    f.write("Write a first line")
except TypeError:
    print("There was a Type Error!")
except OSError:
    print("Hey you have an OS Error")
finally:
    print("I always Run!")

#Induce an error by changing file permissions (f = open('testfile' ,'r'))

#Example User providing a wrong input
def ask_for_int():
    while True:                          #Introducing while loop optional
        try:
            result = int(input("Please provide a number:  "))
        except:
            print("Whoops! that is not a number")
            continue
        else:
            print("Thank you for checking")
            break
        finally:
            print("End of try/except/finally")
            print("I always run at the end!")

ask_for_int()                        