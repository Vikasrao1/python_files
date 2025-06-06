# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.
# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, 
# so you get a 3 by 3 board representation.

test_board=['#', 'X', 'O', 'X', 'O', 'X', '0', 'X', 'O', 'X']
def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board [3])
    print('-- + -- + --')
    print(board[4] + '|' + board[5] + '|' + board [6])
    print('-- + -- + --')
    print(board[7] + '|' + board[8] + '|' + board [9])

display_board(test_board)
#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
# Think about using while loops to continually ask until you get a correct answer. 
def get_player_input():
    while True:
        choice = input("please enter X or O: ").upper()
        if choice in ['X', 'O']:
            return choice
        else:
            print("Invalid input, please enter X or O ")
player_input=get_player_input()
print(player_input)

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), 
# and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker

place_marker(test_board,'$',8)
display_board(test_board)

# Step 4 Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3]== mark )or #across the top
    (board[4] == mark and board[5] == mark and board[6]== mark) or #middle
    (board[7]== mark and board[8]== mark and board[9]==mark) or #bottom
    (board[1] == mark and board[4] == mark and board[7] == mark) or # down the middle
    (board[2] == mark and board[5] == mark and board[8] == mark) or # down the middle
    (board[3] == mark and board[6] == mark and board[9] == mark) or # down the right side
    (board[1] == mark and board[5] == mark and board[9] == mark) or # diagonal
    (board[3] == mark and board[5] == mark and board[7] == mark)) # diagonal
print(win_check(test_board,'X'))

# Step 5: Write a function that uses the random module to randomly decide which player goes first. 
# You may want to lookup random.randint() Return a string of which player went first.
import random
def choose_first():
    if random.ranint(0,1) == 0:
        return 'player 2'
    else:
        return 'player 1'
# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    if board[position] == '':
        return True
    else:
        return False
# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    for space in board:
        if space == ' ':
            return False
    return True
# Step 8: Write a function that asks for a player's next position (as a number 1-9) and 
# then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.


def player_choice(board):
    while True:
        try:
            choice = int(input("Enter the next position (1-9) : "))
            
            if 1 <= choice <= 9:
                if space_check(board, choice): #check if space is free
                    return choice
                else:
                    print("This position is already taken, please choose another one")
            else:
                 print("Invalid input, please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input, please enter a number between 1 and 9.")

#Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again

def replay(choice):
    if choice.lower()== "yes":
        return True
    elif choice.lower()=="false":
        return False







     




    

