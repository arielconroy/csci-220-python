#Ariel Robinson
#valentineGreeting.py
#Problem:
#Create a heart and have an arrow shooting towards it before closing
#Certification of Authenticity:
# I certify that this lab is my own work, but I 
#discussed it with Marge in CSL

from graphics import *
from time import sleep

def valentineGreeting():
    #changes the window name to Valentine's Day Greeting
    win=GraphWin("Valentine's Day Greeting",400,500)
    winWidth=win.getWidth()
    winHeight=win.getHeight()
    win.setBackground("white")
    
    #creates heart
    heart=Polygon(Point(185,162),Point(203,134),Point(248,102),
                      Point(282,102),
                      Point(319,122),
                      Point(338,155),Point(341,201),Point(336,223),
                      Point(311,280),Point(289,315),
                      Point(256,352),Point(223,382),
                      Point(193,405),Point(181,414),Point(158,400),
                      Point(137,383),Point(117,362),Point(87,332),
                      Point(63,304),
                      Point(44,272),Point(28,236),Point(20,205),
                      Point(21,162),Point(39,125),Point(65,107),
                      Point(86,98),Point(119,102),
                      Point(143,116),Point(156,131),
                      Point(165,145),Point(174,161),Point(180,172))
    #changes the heart color and outline
    heart.setFill("red")
    heart.setOutline("red")
    time.sleep(0.4)
    #draw the heart
    heart.draw(win)
    time.sleep(0.4)
    #sets the message to be at the bottom center and color changes
    msgPoint=Point(win.getWidth()/2, win.getHeight()-10)
    msg=Text(msgPoint,"Happy Valentine's Day")
    msg.setFace("arial")
    msg.setSize(20)
    msg.setTextColor("red")
    msg.draw(win)
    
    time.sleep(0.9)
    #changes text to "click to shoot arrow"
    msg.setText("Click to shoot arrow")
    


    #click to change 
    win.getMouse()
    msg.undraw()
    arrow=Line(Point(500,600), Point(300,400))
    #creates the arrow and moves it to shoot into heart
    arrow.setArrow("last")
    #draws the arrow
    arrow.draw(win)
    #makes the arrow move to the center
    for i in range(20):
        arrow.move(-10,-15)
        time.sleep(0.3)
    arrow.setArrow("none")
    msg.draw(win)
    #sets text to close the window
    msg.setText("Click window to close")
    win.getMouse()
    #closes window
    win.close()

valentineGreeting()

   
