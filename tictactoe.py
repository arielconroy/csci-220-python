#Ariel Robinson
#tictactoe.py
#Problem: The user and a friend can play tic tac toe by entering
#an x or and o and choosing where they want to,
#a winner or tie is determined 
#Certification of Authenticity:
# I certify that this lab is my own work, but I 
#discussed it with Asa, Logan, and Marge in CSL

def buildBoard():
    #this function creates the boardList 
    boardList=[1,2,3,4,5,6,7,8,9]
    return boardList

def displayBoard(boardList):
    #this function displays the board 
    print(str(boardList[0]),end=" | " )
    print(str(boardList[1]) ,end=" | ")
    print(str(boardList[2]) )
    print(end="----------")
    print()
    print(str(boardList[3]) ,end=" | ")
    print(str(boardList[4]) ,end=" | ")
    print(str(boardList[5]) )
    print(end="----------")
    print()
    print(str(boardList[6]) ,end=" | ")
    print(str(boardList[7]),end=" | " )
    print(str(boardList[8]),end="")
  


def fillSpot(boardList, position ,character):
#this function will only allow an x or and o
#if there is not an x or o then the board will not display the
#wrong character
    if character=="x"or character=="o":
        boardList[position-1]=character
        return True
    else:
        print("Character not allowed")
    

    
def checkLegal(boardList, position):
#this functions checks if the spot is legal
# if the spot is legal than the character will
#appear on the board
    boardPosition=boardList[position-1]
    if boardPosition=="x" or boardPosition=="o":
        print("Spot not legal")
        return False
    else:
        return True
        
    
def checkWonX(boardList):
#this function indexes all the possible ways x can win
    boardPosition=boardList
    
    if (boardPosition[0]=="x"and boardPosition[1]=="x"
    and boardPosition[2]=="x"):
        return True
    elif (boardPosition[3]=="x"and boardPosition[4]=="x"
    and boardPosition[5]=="x"):
        return True
    elif (boardPosition[6]=="x"and boardPosition[7]=="x"
    and boardPosition[8]=="x"):
        return True
    elif (boardPosition[0]=="x"and boardPosition[4]=="x"
    and boardPosition[8]=="x"):
        return True
    elif (boardPosition[2]=="x"and boardPosition[4]=="x"
    and boardPosition[6]=="x"):
        return True
    elif (boardPosition[0]=="x"and boardPosition[3]=="x"
    and boardPosition[6]=="x"):
        return True
    elif (boardPosition[1]=="x"and boardPosition[4]=="x"
    and boardPosition[7]=="x"):
        return True
    elif (boardPosition[2]=="x"and boardPosition[5]=="x"
    and boardPosition[8]=="x"):
        return True
    else:
        return False
def checkWonO(boardList):
#this function indexes all the possible ways o can win

    boardPosition=boardList
    if (boardPosition[0]=="o"and boardPosition[1]=="o" 
    and boardPosition[2]=="o"):
        return True
    elif (boardPosition[3]=="o"and boardPosition[4]=="o"
    and boardPosition[5]=="o"):
        return True
    elif (boardPosition[6]=="o"and boardPosition[7]=="o"
    and boardPosition[8]=="o"):
        return True
    elif (boardPosition[0]=="o"and boardPosition[4]=="o"
    and boardPosition[8]=="o"):
        return True
    elif (boardPosition[2]=="o"and boardPosition[4]=="o"
    and boardPosition[6]=="o"):
        return True
    elif (boardPosition[0]=="o"and boardPosition[3]=="o"
    and boardPosition[6]=="o"):
        return True
    elif (boardPosition[1]=="o"and boardPosition[4]=="o"
    and boardPosition[7]=="o"):
        return True
    elif (boardPosition[2]=="o"and boardPosition[5]=="o"
    and boardPosition[8]=="o"):
        return True
    else:
        return False
def checkWon(boardList):
#this function checks to see if anyone won 
    if checkWonO(boardList)==True:
        return True
    elif checkWonX(boardList)==True:
        return True
    else:
        return False

def checkOver(boardList):
# this function keeps the game going if no one has won yet
#it also determines a tie 
    gameTied=True
    for i in range(9):
        if boardList[i]!="x"and boardList[i] !="o":
            gameTied=False 
    if checkWon(boardList)==True:
        return True
    elif gameTied==True :
        return True 
    else:
        return False 
    
def playGame():
# this function executes the game and will stop if someone one wins
#or if there is no places left on the board
    boardList=buildBoard()
    displayBoard(boardList)
    gameCheck=checkOver(boardList)
    while gameCheck==False:
        playerMove=input("\n Enter your move: ")
        playerSpot=eval(input("Where?: "))
        if checkLegal(boardList, playerSpot)==True:
            fillSpot(boardList, playerSpot,playerMove)
            gameCheck=checkOver(boardList)
            displayBoard(boardList)
        if gameCheck==True:
            if checkWonX(boardList)==True:
                print("\n Player 1 Won!")
            elif checkWonO(boardList)==True:
                print("\n Player 2 Won!")

            else:
                print("\n The Game is Tied")


def main():
#the game is executed through the main
    playGame()

main()


