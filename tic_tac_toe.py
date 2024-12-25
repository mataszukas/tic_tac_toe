import random
import sys
from tabulate import tabulate

def computer_move(board, field, player, computer, size): #assign offensive moves for computer first, 
                                                         #then defensive moves if there is no winning move
    pass
    #check all rows for potential winning move (offensive)
    for i in range(size): #simply check every list(one list=one row) in the board list
        if board[i].count(computer) == size - 1 and board[i].count(None) == 1: #if there is only one empty cell in the row
                                                                               #and rest are computer's cells
            j = board[i].index(None)
            board[i][j] = computer  #place computer's "O" in the empty cell
            field.remove([i, j])
            return [i, j]
        
    #check all columns for potential winning move (offensive)
    for j in range(size):
        col = [board[i][j] for i in range(size)] #check every cell 'i' in column 'j'
        if col.count(computer) == size - 1 and col.count(None) == 1: #check if there is only one empty cell 
                                                                     #and the rest are computer's cells in column 'j'
            i = col.index(None) #get the index of the empty cell assign it to 'i'
            board[i][j] = computer #place computer's "O" in the empty cell
            field.remove([i, j]) #remove the empty cell from the list of available fields
            return [i, j] #return the coordinates of the new "O" cell
    
    #check all main diagonal for potential winning move (offensive)
    diagnol = [board[i][i] for i in range(size)] #board[0][0], board[1][1], board[2][2]
    if diagnol.count(computer) == size - 1 and diagnol.count(None) == 1: #same logic as with columns/rwos
        i = diagnol.index(None)
        board[i][i] = computer #place computer's "O" in the empty cell
        field.remove([i, i])
        return [i, i]
    
    #check counterdiagonal for potential winning move (offensive)
    counter_diag = [board[i][size - 1 - i] for i in range(size)] #board[0][2], board[1][1], board[2][0]
    if counter_diag.count(computer) == size - 1 and counter_diag.count(None) == 1:
        i = counter_diag.index(None)
        board[i][size - 1 - i] = computer #place computer's "O" in the empty cell
        field.remove([i, size - 1 - i])
        return [i, size - 1 - i]
    
    #check rows for potential blocking move (defensive)
    for i in range(size):
        if board[i].count(player) == size - 1 and board[i].count(None) == 1:
            j = board[i].index(None)
            board[i][j] = computer #place computer's "O" in the empty board cell
            field.remove([i, j])
            return [i, j]
        
    #check columns for potential blocking move (defensive) (same logic as offense, just checking player's cells)
    for j in range(size):
        col = [board[i][j] for i in range(size)] 
        if col.count(player) == size - 1 and col.count(None) == 1: 
            i = col.index(None) 
            board[i][j] = computer #place computer's "O" in the empty board cell
            field.remove([i, j]) 
            return [i, j] 
    
    #check diagonal for potential blocking move (defensive)
    diagnol = [board[i][i] for i in range(size)]
    if diagnol.count(player) == size - 1 and counter_diag.count(None) == 1:
        i = diagnol.index(None)
        board[i][i] = computer #place computer's "O" in the empty board cell
        field.remove([i, i])
        return [i, i]
    
    #check counterdiagnol for potential blocking move (defensive)
    counter_diag = [board[i][size - 1 - i] for i in range(size)]
    if counter_diag.count(player) == size - 1 and counter_diag.count(None) == 1:
        i = counter_diag.index(None)
        board[i][size - 1 - i] = computer #place computer's "O" in the empty cell
        field.remove([i, size - 1 - i])
        return [i, size - 1 - i]
    
    #if no winning or defensive move, choose a random field
    if field: #if field is not empty
        i, j = random.choice(field)
        board[i][j] = computer
        field.remove([i, j]) #place computer's "O" in a random empty cell
        return [i, j]



def check_winner(board, player, size):
    pass
    #check rows
    for row in board:
        if all(cell == player for cell in row): #if all cells in a row are filled with same symbol (x or o)
            return True
    
    #check columns
    for col in range(size):
        if all(board[row][col] == player for row in range(size)): #if all cells in a column are filled with 
                                                                  #same symbol (x or o)
            return True
    
    #check diagonal
    if all(board[i][i] == player for i in range(size)): #if all cells in the main diagonal are filled with
                                                        #same symbol (x or o)
        return True
    
    #check counterdiagonal
    if all(board[i][size - 1 - i] == player for i in range(size)): #if all cells in the counterdiagonal are filled 
                                                                   #with same symbol (x or o)
        return True
    
    return False



def main():
    pass
    while True:
        try:
            size = int(input("Enter the size of the board: (-1 to exit) "))
            if size == -1:
                sys.exit(1)
            break
        except:
            print("Invalid input, try again")
            continue
    board = [[None for _ in range(size)] for _ in range(size)] #create a 3x3 board with None values
    available_fields = [[x, y] for x in range(size) for y in range(size)] #create a list of all available cells on the board
    player = "X"
    computer = "O"
    
    while True:
        try:
            user_input = input("Enter coordinates [x, y]: (-1 to exit) ")
            if user_input == "-1":
                break
            user_input = user_input.split(",")
            if len(user_input) != 2:
                print("Invalid input, try again")
                continue
            user_input = [int(coord) for coord in user_input]
            
            if board[user_input[0]][user_input[1]] is not None:
                print("Field already taken")
                continue
            
            board[user_input[0]][user_input[1]] = player
            available_fields.remove(user_input)
            
            if check_winner(board, player, size):
                print(tabulate(board, tablefmt="fancy_grid"))
                print("You win!")
                break
            
            if not available_fields:
                print(tabulate(board, tablefmt="fancy_grid"))
                print("Draw!")
                break
            
            cm = computer_move(board, available_fields, player, computer, size)
            print(f"Computer's move: {cm}")
            
            if check_winner(board, computer, size):
                print(tabulate(board, tablefmt="fancy_grid"))
                print("Computer wins!")
                break
            
            print(tabulate(board, tablefmt="fancy_grid"))

        except EOFError:
            sys.exit(1)
        except:
            print("Invalid input, try again")
            continue
        


if __name__ == "__main__":
    main()

# Code logic: 
# 1. Assign 'size' value to board size with None values
# 2. Create a list of all available cells on the board
# 3. Assign player "X" and computer "O"
# 4. User enters coordinates [x, y]
# 5. Check if the field is already taken
# 6. Check if the player wins
# 7. Check if the game is a draw
# 8. Computer makes a move
# 9. Check if the computer wins (offensive and defensive moves on computer_move function)
# 10. Print the board
# 11. If the player wins, print "You win!"
# 12. If the computer wins, print "Computer wins!"
# 13. If the game is a draw, print "Draw!"
# 14. If game is not over, repeat steps 4-13