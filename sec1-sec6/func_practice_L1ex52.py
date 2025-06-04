#'OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# def old_macdonald(name):
# #convert the string into list of characters
#     name_list=list(name)

# # capitalized 1st and 4th letter.

#     if len(name_list) >=1:
#         name_list[0]= name_list[0].upper()
#     if len(name_list) >=4:
#         name_list[4]= name_list[4].upper()

#     new_name=''.join(name_list)
#     print(new_name)
# old_macdonald('old_macdonald')

# Second Method

def old_macdonald(name):
    first_letter = name[0]
    in_between= name[1:3]
    fourth_letter= name[3]
    rest=name[4:]
    return first_letter. upper()+ in_between + fourth_letter.upper() + rest
print(old_macdonald('macdonald'))
