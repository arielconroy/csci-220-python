#Ariel Robinson
#hangman.py
#Problem: A random word is picked from the wordlist
# if the player can correctly guess the word they win
#hangman but if they can not they lose, they have
#7 guesses 
#Certification of Authenticity:
# I certify that this lab is my own work, but I 
#discussed it with Professor Stavley, and Marge in CSL

from graphics import *
def wordFile():
    #gets the words from the wordlist 
    file=open("wordlist.txt","r")
    wordList=[]
    for line in file:
        lineInfo=line.split()
        for i in range(len(lineInfo)):
            #print(lineInfo)
            wordList.append(lineInfo)
    #print(wordList)
    return wordList

def wordPick():
    #this function randomly chooses a word from the wordlist
    import random
    wordList=wordFile()
    randomWords=random.randint(0, len(wordList)-1)
    wordChoice=wordList[randomWords]
    finalword=""
    return wordChoice

def wordToString(wordChoice):
    #changes the chosen word into a string
    word=""
    for i in range(len(wordChoice)):
        word+=wordChoice[i]
    return word

def buildBlanks(word):
    #build blanks
    #this builds the guess by adding in underscores 
    wordChoice=wordPick()
    return ["_"] * len(word)


def checkBlank(blanks,guess,word):
# this function substitutes underscores for
#letters if they guess the right letter
    foundLetter = False
    for i in range(len(word)):
       if word[i]==guess:
           blanks[i]=word[i]
           foundLetter=True
    return foundLetter

def filledInBlanks(blanks,guess,word):
#returns blanks
    for i in range(len(word)):
       if word[i]==guess:
           blanks[i]=word[i]
   
    return blanks
        

def secretWordCheck(word,blanks):
## this function checks to see if the player win,
#checks to see if guess equals the secret word
#returns a boolean
# if there are still blanks in word then it remains False
    if "_" in  blanks:
        return False
    else:
        return True

def display(letterList):
    letters=""
    for ch in letterList:
        letters+=ch+" "

    return letters

def didGuess(lettersGuessed, guess):
#this function returns the user's guess
#this function checks to see if they already guess a letter or not
    if  guess not in lettersGuessed:
        lettersGuessed.append(guess)
        return False
    else:
        return True
def playGame():
    
    word=wordPick()
    #print(word)
    word=wordToString(word)
    print(word)
    blanks=buildBlanks(word)
    #blanks=filledInBlanks(blanks,guess,word)
    numTries=0
    counter=7
    lettersGuessed=[]
    

#the player have 7 tries to guess the word or
#if they guess right the game is over
    while numTries<=7 and secretWordCheck(word,blanks)==False:
        showGame=display(blanks)
        guess=input("Make a guess: ")
        found=checkBlank(blanks,guess,word)
        alreadyGuess = didGuess(lettersGuessed, guess)
        #print("guessed",lettersGuessed)
        if found==True:
            print("You got a letter")

        elif alreadyGuess==True:
            print("Already guessed, Try Again")
            numTries+=1
        elif numTries==7:
            print("You Lost")
            
        else:
            numTries+=1
            counter-=1
            print("Keep Trying you have "+ str(counter)+ " tries left.")
    if secretWordCheck(word,blanks)==True: 
        print("You Won")


def main():
    win=GraphWin("HangMan",600,400)

#picks word
    word=wordPick()
    word=wordToString(word)
    blanks=buildBlanks(word)
    checkWin=secretWordCheck(word,blanks)
    guessedLetters=[]

    #draws the entry
    letterEntry=Entry(Point(100,150),5)
    letterEntry.draw(win)

    #display how many blanks in the word
    letterDisplay=Text(Point(100,200),display(blanks))
    letterDisplay.draw(win)

#creates the hangman
    hang=Line(Point(400,70),Point(400,300))
    topPiece=Line(Point(400,70),Point(300,70))
    bottomhang=Line(Point(350,300),Point(450,300))
    bottomhang.draw(win)
    hang.draw(win)
    head=Circle(Point(300,100),25)
    body=Line(Point(300,120),Point(300,270))
    leftArm=Line(Point(250,120),Point(300,200))
    rightArm=Line(Point(350,120),Point(300,200))
    rightLeg=Line(Point(300,270),Point(320,330))
    leftLeg=Line(Point(299,270),Point(290,330))

#creates enter button
    enterButton=Rectangle(Point(85,265),Point(120,285))
    enterButton.draw(win)
    #displays the guessed letters

    lettersGuessed=Text(Point(100,250),"Letters Guessed")
    lettersGuessed.draw(win)
    #gets player guess
    enterButtonText=Text(Point(100,275),"Enter")
    enterButtonText.draw(win)
    # displays the guesses left
    numGuessesDisplay=Text(Point(100,320),"Guesses Left")
    numGuessesDisplay.draw(win)
    numTries=0
    counter=7
    #hangman pieces in a list
    #if number of guesses go down then the hangman pieces will draw

    hangManPieces=[topPiece,head,body,rightArm,leftArm, rightLeg,
    leftLeg]


    while checkWin==False and numTries<7:
        win.getMouse()
        guess=letterEntry.getText()
        blanksFill=filledInBlanks(blanks,guess,word)
        wordCheck=checkBlank(blanks,guess,word)
        found=checkBlank(blanks,guess,word)
        lettersGuessed.setText(guessedLetters)
        

# if found is true then the letter is display
        if found==True:
            letterDisplay.setText(blanksFill)
#if the guess is wrong then the number of tries decreases
#and a piece of the hangman is drawn 
        else:
            numTries+=1
            counter-=1
            hangManPieces[numTries-1].draw(win)
            guessedLetters.append(guess)
            numGuessesDisplay.setText(counter)
        #checks to see if player guessed word
        checkWin=secretWordCheck(word,blanks)
#if player wins the game ends and displays they win
    if checkWin==True:
        lettersGuessed.setText("You Win!")
        gameOverDisplay=Text(Point(200,350),"Do you want to play again")
        gameOverDisplay.draw(win)
        noButton=Rectangle(Point(340,340),Point(360,360)).draw(win)
        yesButton=Rectangle(Point(310,340),Point(330,360)).draw(win)
        yesbuttonText=Text(Point(320,350),"Yes")
        nobuttonText=Text(Point(350,350),"No")
        nobuttonText.draw(win)
        yesbuttonText.draw(win)
        #gets the user clicks
        click=win.getMouse()
        clickX=click.getX()
        clickY=click.getY()

# if player loses then the game ends and displays they loss
    elif checkWin==False and numTries==7:
        win.getMouse()
        lettersGuessed.setText("You Lose!")
        gameOverDisplay=Text(Point(200,350),"Do you want to play again")
        gameOverDisplay.draw(win)
        noButton=Rectangle(Point(340,340),Point(360,360)).draw(win)
        yesButton=Rectangle(Point(310,340),Point(330,360)).draw(win)
        yesbuttonText=Text(Point(320,350),"Yes")
        nobuttonText=Text(Point(350,350),"No")
        nobuttonText.draw(win)
        yesbuttonText.draw(win)
        #gets the user's click
        click=win.getMouse()
        clickX=click.getX()
        clickY=click.getY()

        #if user clicks yes then the game will start over
        #if user clicks no then the game will end and close
    
    if clickX>=340 and clickY>=360 or clickX<=340 and clickY<=360:
        win.close()
        main()

    
    elif clickX >=310 or clickX<=330 and clickY>=340 or clickY<=360:


        win.close()

main()
    



