board = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
        ]

def soduko_solver(board):

    # Iterating through each cell in the grid to find the first empty spot.   
    for r in range(len(board)):
        for c in range(len(board[r])):
            
            # When I find an empty cell I know I can place digits from 1 to 9 inside
            # of it but i also need to make sure that the digit that im trying to place
            # isnt already inside of the row, column and the 3x3 grid within which
            # the cell lies inside of.

            if board[r][c] == 0:
                for num in range(1,10):
                    if isValid(num,board,r,c):
                        # If the number is not found in the row, column and thr 3x3 grid.
                        # Then i replace the zero in the empty spot with that valid number    
                        board[r][c] = num

                        # After that I make recursive call to fill out the next empty cell
                        if soduko_solver(board):

                            # If im successfully able to find a valid solution to the 
                            # board by filling up all the empty cells i return that
                            # filled up board
                            return board

                        else:
                            # If the choice i made led me to not get a valid solution
                            # then I backtrack and test out a different valid number
                            # and try to solve the board by using that.
                            board[r][c] = 0
                
                # If there is no valid number that i can place inside of an empty cell
                # then that means i made wrong choice while filling up one of the previous
                # cells therefore I return false so then I can backtrack and choose a 
                # different number from that cell.
                return False

    # If I traverse through the whole grid without finding any empty spots then that
    # means i have filled up the entire board then i can return True     
    return True

# Going to check weather the number that im trying to place in a particular cell
# is unique which means its not in the row, column and grid where that cell exists 
# inside of.

def isValid(num,board,r,c):

    # Going to iterate through from number zero to eight cause there are 9 rows, 9
    # and 9 cells in a 3x3 grid.

    for i in range(9):

        # Going to check if the number is in any of the cells within the row where the
        # cells lies in.

        if board[r][i] == num:
            return False

        # Going to check weather the number is in any of the cells within the column
        # where the cell where im going to place the number exists inside of.

        if board[i][c] == num:
            return False

        # Going to check weather if the 3x3 grid where the cell in which im going to
        # place the number exists inside of already has that number in any of its 
        # other cells or not
        
        if board[3 * (r//3) + (i//3)][3 * (c//3) + (i % 3)] == num:
            return False
    
    # If none of the conditions meet then that means the number is unique to the row,
    # column and the 3x3 grid within which the cell where im going to place number
    # inside of exists.
    return True

print(soduko_solver(board))