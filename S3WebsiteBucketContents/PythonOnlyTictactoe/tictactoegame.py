import random

def tictactoe(board,playerinput,availablemoves):
    colum = getcolum(playerinput)
    row = getrow(playerinput)
    board[colum][row] = 'x'
    if True == checkverticalwin(board,row,'x'):
        print("Player one wins")
        return False
    if True == checkhorizontalwin(board,colum,'x'):
        print("Player one wins")
        return False
    if True == checkdiagnalwin(board,'x'):
        print("Player one wins")
        return False
    opponetwin = opponetmove(board,availablemoves)
    if opponetwin == False:
        return False
    else:
        return True
    
def getrow(number):
    return (int(number)-1)%3
    
def getcolum(number):
    return (int(number)-1)//3
    
def checkhorizontalwin(board,colum,player):
    if board[colum].count(player) == 3:
        return True
    else:
        return False
    
def checkverticalwin(board,row,player):
    counter = 0
    for x in range(len(board)):
        if player == board[x][row]:
            counter+=1
    if counter == len(board):
        return True
    else:
        return False
    
def checkdiagnalwin(board,player):
    counter = 0
    for x,y in enumerate(reversed(range(len(board)))):#checks 7,5,3 if there are all equal
        if board[x][y] == player:
            counter+=1
    if counter == len(board):
        return True
    counter = 0
    for x in range(len(board)):# checks 1,5,9 if they are all equal
        if board[x][x] == player:
            counter +=1
    if counter == len(board):
        return True
    else:
        return False
    
    
def opponetmove(board,availabemoves):
    if not availablemoves:
        print("tie")
        return False
    number = random.choice(availablemoves)
    row = getrow(number)
    colum =getcolum(number)
    board[colum][row]='o'
    availablemoves.remove(number)
    if True == checkverticalwin(board,row,'o'):
        print("Player two wins")
        return False
    if True == checkhorizontalwin(board,colum,'o'):
        print("Player two wins")
        return False
    if True == checkdiagnalwin(board,'o'):
        print("Player two wins")
        return False

def printboard(board):
    print(f"|{board[0][0]}|{board[0][1]}|{board[0][2]}|\n"
          f"|{board[1][0]}|{board[1][1]}|{board[1][2]}|\n"
          f"|{board[2][0]}|{board[2][1]}|{board[2][2]}|\n")
    
playing = True
board = [[1,2,3],[4,5,6],[7,8,9]]
availablemoves = [1,2,3,4,5,6,7,8,9]
while playing:
    playerinput = input()
    print(playing)
    if playerinput.isnumeric() and (int(playerinput) in availablemoves):
        availablemoves.remove(int(playerinput))
        playing = tictactoe(board,playerinput,availablemoves)
    else:  
        print("Please insert a valid value")
    printboard(board)