# Displaying Info
row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]

def display_board(r1, r2, r3):
    print(r1)
    print(r2)
    print(r3)

display_board(row1,row2, row3)

#switching values
row2[1] = 'X'
display_board(row1,row2, row3)
    
