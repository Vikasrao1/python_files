# Accpting User Inputs
# A = [1,2,3]
# B = [4,5,6]
# C = [7,8,9]

# result= input("Please eneter a value: ") 
# print(type(result))

#  Accept number/convert into an input
# result_int=int(result)
# print(type(result_int))

# Validating the user input 

# def user_choice():
#     choice= input("Enter a number of your choice (0-10): ")
#     return int(choice)

# print(user_choice())

# Checks if choice is a digit
def user_choice():
    #Initial Varibles 

    choice ='WRONG'
    acceptable_range = range(0,10)
    within_range = False

    # TWO CONDITIONS TO CHEK
    # DIGIT OR WITHIN_RANGE == False
    while choice.isdigit() == False or within_range == False:

        choice= input("Enter a number of your choice (0-10): ")
        #DIGIT_CHECK
        if choice.isdigit()== False:
            print("sorry it's not a digit!")
        
        # RANGE_CHECK
        if choice.isdigit()== True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-10)")
                within_range= False
    return int(choice)
#Call the function 
print(user_choice())





