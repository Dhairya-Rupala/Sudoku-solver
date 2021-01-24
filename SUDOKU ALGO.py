sudoku_board = [
    [6,0,0,3,0,0,0,0,0],
    [3,1,5,2,0,8,0,0,6],
    [0,9,0,0,6,0,0,3,0],
    [0,0,0,0,8,0,6,0,0],
    [9,0,0,0,0,0,0,0,2],
    [0,0,1,0,4,0,0,0,0],
    [0,6,0,0,2,0,0,8,0],
    [2,0,0,9,0,6,5,4,1],
    [0,0,0,0,0,4,0,0,3]]




def Solve(sudoku_board):
    empty_box=findEmpty(sudoku_board)

    if not(empty_box):
        return True
    else:
        e_row,e_col=empty_box

    for i in range(1,10):
        if isvalid(sudoku_board,i,(e_row,e_col)):
            sudoku_board[e_row][e_col]=i
            if Solve(sudoku_board):
                return True
            sudoku_board[e_row][e_col]=0
    return False

def findEmpty(sudoku_board):
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board[0])):
            if sudoku_board[i][j]==0:
                return (i,j)
    return None

def isvalid(sudoku_board,num,pos):

    for i in range(len(sudoku_board[0])):
        if sudoku_board[pos[0]][i]==num and pos[1]!=i:
            return False

    for i in range(len(sudoku_board[0])):
        if sudoku_board[i][pos[1]]==num and pos[0]!=i:
            return False

    box_x=pos[0]//3
    box_y=pos[1]//3

    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y*3,box_y*3+3):
            if sudoku_board[i][j]==num and (i,j)!=pos:
                return False
    return True


def printboard(sudoku_board):

    for i in range(len(sudoku_board)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - -")
        for j in range(len(sudoku_board[0])):
            if j%3==0 and j!=0:
                print(" | ",end=" ")
            if j==8:
                print(sudoku_board[i][j])
            else:
                print(str(sudoku_board[i][j]) + " ",end=" ")




print("Welcome to my sudoku game.......")
print()
printboard(sudoku_board)
print()
print("Solving the sudoku.............")
Solve(sudoku_board)
printboard(sudoku_board)