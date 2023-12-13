import random
import json
import boto3
from htmltext import *


def lambda_handler(event, context):
    board = None
    availablemoves = None
    if len(event.get('queryStringParameters').get('password')) == 0 or len(event.get('queryStringParameters').get('user_id')) == 0:
        text = htmlnoinfo()
        return{
                'statusCode': 200,
                'body': text,
                "headers" : {
                'Content-Type': 'text/html',
              }
            }
    password = event.get('queryStringParameters').get('password')
    userinput = "doesn't exist"
    reset = "false"
    if "userinput" in event.get('queryStringParameters'):
        userinput = event.get('queryStringParameters').get('userinput')
    if "reset" in event.get('queryStringParameters'):
        reset = event.get('queryStringParameters').get('reset')
    user_id = event.get('queryStringParameters').get('user_id')
    dynamodb = boto3.resource("dynamodb")                 
    table = dynamodb.Table("tictactoe_info")  #gets dynamodb table
    response = table.get_item(Key={"user_name":user_id}) #gets user information
    if "Item" in response and reset == "false":   #checks if user exist if it does check if password matches and gets information. If no user it creates it in dynamodb
        if password != response["Item"]["password"]:
            html = htmlfile()
            return{
                'statusCode': 200,
                'body': html,
                "headers" : {
                'Content-Type': 'text/html',
              }
            }
        board = response["Item"]["board"]
        availablemoves = response["Item"]["availablemoves"]
    else:
        board = [[1,2,3],[4,5,6],[7,8,9]]
        availablemoves = [1,2,3,4,5,6,7,8,9]
        table.put_item(Item = {"user_name":user_id,"password":password,"board":board,"availablemoves":availablemoves})
    if userinput == "doesn't exist":
        text = returnboard(board)
        text = htmlinput(text,user_id,password)
        return  {
                'statusCode': 200,
                'body': text,
                "headers" : {
                'Content-Type': 'text/html',
              }
            }
    playerinput = userinput
    playing = 0
    if playerinput.isnumeric() and (int(playerinput) in availablemoves):
        availablemoves.remove(int(playerinput))
        playing = tictactoe(board,playerinput,availablemoves)
    else:  
        print("Please insert a valid value")
    printboard(board)
    table.update_item(Key={"user_name":user_id},UpdateExpression="SET board= :s",ExpressionAttributeValues={':s': board}) #updates boards and availablemoves taking from player and bot
    table.update_item(Key={"user_name":user_id},UpdateExpression="SET availablemoves= :a",ExpressionAttributeValues={':a': availablemoves})
    text = returnboard(board)
    if playing == 1 :
        text = htmlplayerwin(text,playing,user_id,password)
    elif playing == 2:
        text = htmlplayerwin(text,playing,user_id,password)
    elif playing == 3:
        text = htmlplayerwin(text,playing,user_id,password)
    else:
        text = htmlinput(text,user_id,password)
    return {
            'statusCode': 200,
            'body': text,
            "headers" : {
                'Content-Type': 'text/html',
                }
            }

def tictactoe(board,playerinput,availablemoves):
    colum = getcolum(playerinput)
    row = getrow(playerinput)
    board[colum][row] = 'x'
    if True == checkverticalwin(board,row,'x'):
        print("Player one wins")
        return 1
    if True == checkhorizontalwin(board,colum,'x'):
        print("Player one wins")
        return 1
    if True == checkdiagnalwin(board,'x'):
        print("Player one wins")
        return 1
    opponetwin = opponetmove(board,availablemoves)
    if opponetwin == 2 or opponetwin ==3:
        return opponetwin
    else:
        return 0
    
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
    
    
def opponetmove(board,availablemoves):#selects a random number from availabemoves then updates board and availablemoves and check if bot wins
    if not availablemoves:
        return 3
    number = random.choice(availablemoves)
    row = getrow(number)
    colum =getcolum(number)
    board[colum][row]='o'
    availablemoves.remove(number)
    if True == checkverticalwin(board,row,'o'):
        print("Player two wins")
        return 2
    if True == checkhorizontalwin(board,colum,'o'):
        print("Player two wins")
        return 2
    if True == checkdiagnalwin(board,'o'):
        print("Player two wins")
        return 2

def printboard(board):
    print(f"|{board[0][0]}|{board[0][1]}|{board[0][2]}|\n"
          f"|{board[1][0]}|{board[1][1]}|{board[1][2]}|\n"
          f"|{board[2][0]}|{board[2][1]}|{board[2][2]}|\n")
          
def returnboard(board):
    text = text = "|"+str(board[0][0])+"|"+str(board[0][1])+"|"+str(board[0][2])+"|</br>|"+str(board[1][0])+"|"+str(board[1][1])+"|"+str(board[1][2])+"|</br>|"+str(board[2][0])+"|"+str(board[2][1])+"|"+str(board[2][2])+"|"
    return text

    
