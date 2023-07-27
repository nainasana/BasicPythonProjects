# #Tic-Tac-Toe


# #Create the game board
# board = [' ' for _ in range(9)]

# #Function to display the game board
# def display_board():
#     print('-------------')
#     print('| '+ board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
#     print('-------------')
#     print('| '+ board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
#     print('-------------')
#     print('| '+ board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
#     print('-------------')


# #Function to check if any player has won
# def check_win(player):
#     #check rows
#     for i in range(0,9,3):
#         if board[i] == board[i+1] == board[i+2] == player:
#             return True
#     #check columns
#     for i in range(3):
#         if board[i] == board[i+3] == board[i+6] == player:
#             return True
#     #check diagonals
#     if board[0] == board[4] == board[8] == player:
#         return True
#     if board[2] == board[4] == board[6] == player:
#         return True
#     return False
    
# #Function to check if the game is a draw
# def check_draw():
#     return " " not in board 

# #Function to play the game
# def play_game():
#     current_player = 'X'
    
#     while True:
#         display_board()
#         position = int(input("Player " + current_player + ", choose a position (1-9): ")) - 1
        
#         if board[position] == ' ': #checking the vacant spots
#             board[position] = current_player 
#             if check_win(current_player):
#                 display_board()
#                 print("Player " + current_player + " wins!")
#                 break
#             else:
#                 check_draw()
#                 display_board()
#                 print("It's a draw!")
#                 break
#             # else:
#             #     if current_player == 'X':
#             #         current_player = 'O'
#             #     else:
#             #         current_player = 'X'
                
#         else:
#             print("The postion is already filled. Choose another position. ")   
            
# play_game()