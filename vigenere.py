#Ariel Robinson
#vigenere.py
#Problem: creates an interface where the user can input a
#keyword and message and it will display the encoded message to user
#Certification of Authenticity:
# I certify that this lab is my own work, but I 
#discussed it with Marge in CSL

from graphics import *

def code(message,keyword):
    #changes the message and keyword to uppercase
    message=message.upper()
    keyword=keyword.upper()
    #removes the white space 
    message=message.replace(" ", "")
    keyword=keyword.replace(" ", "")
    messageResult=""

    #encodes the message and keyword
    #creates a loop for the length of the message
    for i in range(0,len(message)):
        messageCharacter=ord(message[i])-65
        keywordCharacter=ord(keyword[i%len(keyword)])-65
        messageCode=messageCharacter+keywordCharacter
        messageCode=messageCode%26
        messageCode=messageCode+65
        messageResult=messageResult+chr(messageCode)
    return (messageResult)
    

def main():
    #creates the interface that is displayed to user
    win=GraphWin("Vigenere",450,400)
    msgText=Text(Point(150,150),"Message to Code").draw(win)
    keywordsText=Text(Point(130,180),"Keywords").draw(win)
    messageInput=Entry(Point(270,150),20)
    keywordsInput=Entry(Point(270,180),20)
    messageInput.draw(win)
    keywordsInput.draw(win)

    #creates the encode button
    buttonText=Text(Point(220,220),"Encode")
    buttonText.draw(win)
    buttonRec=Rectangle(Point(190,210), Point(255,230))
    buttonRec.draw(win)
    win.getMouse()

    #gets the message from the entry box

    inputMessage=messageInput.getText()
    #gets the keyword from the entry box
    inputKeyword=keywordsInput.getText()

    #removes the button from the display 
    buttonText.undraw()
    buttonRec.undraw()
    
    resultMessage=Text(Point(220, 240),"Resulting Message")
    #shows the results of the encoded message from the function code 
    codedMessage=Text(Point(220, 260),code(inputMessage,inputKeyword))

    #displays the encoded message 
    resultMessage.draw(win)
    codedMessage.draw(win)
    #displays the close window message
    closeText=Text(Point(220,360),"Click anywhere to close")
    closeText.draw(win)
    win.getMouse()
    win.close()  
main()
