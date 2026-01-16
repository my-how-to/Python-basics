# ============================================================
#           EXERCISE 010 — TIC-TAC-TOE (PCEP)
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Exercise (PCEP course task):
#   Build a console Tic-Tac-Toe game.
#
#   Rules and requirements:
#   - The computer plays with 'X' and always starts by placing its first 'X' in the center.
#   - The user plays with 'O'.
#   - The board squares are numbered row by row starting from 1.
#   - The user enters a move by typing a square number that is an integer from 1 to 9
#     and not already occupied.
#   - After each move, the program checks for one of four states: continue, tie,
#     user wins, or computer wins.
#   - The computer then makes a move and the check repeats.
#   - No AI required; a random free square is enough.
#
# Goal:
#   Complete the task by filling in the functions below.
#   Do not implement any extra functions.
# ============================================================

def display_board(board):   
    for row in board:
        print("+","-" * 13, "+")
        for cell in row:
            print("| ", cell, end=" ")
        print(" | ")
    print("+","-" * 13, "+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    try:
        move = int(input("make your move :"))
        if move > 1 or move < 9:
            pass
        else:
            raise ValueError ("use only numbers from 1 to 9")

    except:
        pass


               


#def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


#def draw_move(board):
    # The function draws the computer's move and updates the board.

board = [
    ["1","2","3"],
    ["4","X","6"],
    ["7","8","9"],
]

#while True:
#    display_board(board)
#    enter_move(board)

    
# print("ABCDE"[-2:1:-2])
#why DC?
# The slice starts at index -2 (which is 'D'), 
# goes up to index 1 (which is 'B', exclusive), 
# and steps backwards by 2, resulting in '
# DC
#print("ABCDE"[-2:1:-4]) # "D"

#print("ABCDE"[-2:1]) # "D"
#why D?
# The slice starts at index -2 (which is 'D'),
# goes up to index 1 (which is 'B', exclusive),
# and uses the default step of 1, resulting in 'D' only.

d = {"a": 1, "b": 2}
v = d.get("c", 3) # if "c" not found, return 3
d["c"] = 4 # add "c" with value 4 to the dictionary
print(v + d["c"]) # 7
# Explanation:
# d.get("c", 3) looks for key "c" in the dictionary d
# Since "c" is not found, it returns the default value 3
# Then, d["c"] = 4 adds the key "c" with value
# Finally, v + d["c"] computes 3 + 4, resulting in 7
