
# coding: utf-8

# # Tic Tac Toe Game!!

# ## First create all the functions: 
# Choosing Player Input
# Place where the player wants to place his input
# To Check Win
# To check the empty place in a specific Position
# Checking the full board to decide the result
# Asking to replay the game
# And then finally the game logic.
# 
# 
# This code below works only for two players and allows to play n number of times!.

# In[ ]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(' ' + ' | ' + ' ' + ' | ')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + ' | ' + ' ' + ' | ')
    print('-' + ' -' + ' -'+ ' -'+ ' -')
    print(' ' + ' | ' + ' ' + ' | ')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + ' | ' + ' ' + ' | ')
    print('-' + ' -' + ' -'+ ' -'+ ' -')
    print(' ' + ' | ' + ' ' + ' | ')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' ' + ' | ' + ' ' + ' | ')
    
    


# In[1]:


def player_input():
    
    marker = ''
    
    if marker != 'X' or marker != 'O':
        marker = input("Player 1: Please select X or O")
    if marker.upper() == 'X':
        return ('X','O')
    else:
        return ('O', 'X')
        


# In[2]:


def place_marker(board, marker, position):
    
    board[position] = marker


# In[3]:


def win_check(board, mark):
    
    return ((board[1] == board[2] == board[3]==mark)or
    (board[4] == board[5] == board[6]==mark)or
    (board[7] == board[8] == board[9]==mark)or
    (board[1] == board[4] == board[7]==mark)or
    (board[2] == board[5] == board[8]==mark)or
    (board[9] == board[6] == board[3]==mark)or
    (board[1] == board[5] == board[9]==mark)or
    (board[7] == board[5] == board[3]==mark))


# In[4]:


import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return ('Player 1')
    else:
        return ('Player 2')
        


# In[5]:


def space_check(board, position):
    
    return board[position] == ' '


# In[6]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    
    return True


# In[7]:


def player_choice(board):
    position = 0
    while position not  in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("please select your position on the board from 1 to 9"))
    return position


# In[8]:


def replay():
    
    choice = input("Do you want to play again ? , Yes or No")
    if choice == 'Yes':
        return True
    else:
        return False


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play = input("Are you Ready? , Y or N")
    if play == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations!, Player1 have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations!, Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break

