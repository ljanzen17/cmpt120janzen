#calculator.pyw
from graphics import *
win = GraphWin('Calculator', 500, 500)
rect = Rectangle(Point(20,20),Point(300,385))
rect.setFill('grey')
rect.draw(win)
eqbar = Rectangle(Point(60,50),Point(265,100))
eqbar.setFill('green')
eqbar.draw(win)

def drawRec(p1,p2,p3,p4,color):
    tempRec = Rectangle(Point(p1,p2),Point(p3,p4))
    tempRec.setFill(color)
    return(tempRec)

def drawPoint(p1,p2,text,color):
    tempPoint = Text(Point(p1,p2),text)
    tempPoint.setTextColor(color)
    return(tempPoint)

click7 = drawRec(65,110,110,155,'white')
click8 = drawRec(115,110,160,155,'white')
click9 = drawRec(165,110,210,155,'white')
clickdiv = drawRec(215,110,260,155,'white')
click4 = drawRec(65,160,110,205,'white')
click5 = drawRec(115,160,160,205,'white')
click6 = drawRec(165,160,210,205,'white')
clickmult = drawRec(215,160,260,205,'white')
click1 = drawRec(65,210,110,255,'white')
click2 = drawRec(115,210,160,255,'white')
click3 = drawRec(165,210,210,255,'white')
clickadd = drawRec(215,210,260,255,'white')
clickplusmin = drawRec(65,260,110,305,'white')
click0 = drawRec(115,260,160,305,'white')
clickdecimal = drawRec(165,260,210,305,'white')
clickminus = drawRec(215,260,260,305,'white')
clickdel = drawRec(165,310,210,355,'white')
clickeq = drawRec(215,310,260,355,'white')

click7.draw(win)
click8.draw(win)
click9.draw(win)
clickdiv.draw(win)
click4.draw(win)
click5.draw(win)
click6.draw(win)
clickmult.draw(win)
click1.draw(win)
click2.draw(win)
click3.draw(win)
clickadd.draw(win)
clickplusmin.draw(win)
click0.draw(win)
clickdecimal.draw(win)
clickminus.draw(win)
clickeq.draw(win)
clickdel.draw(win)

num7 = drawPoint(87.5,132.5,'7','black')
num8 = drawPoint(137.5,132.5,'8','black')
num9 = drawPoint(187.5,132.5,'9','black')
numdiv = drawPoint(237.5,132.5,'/','black')
num4 = drawPoint(87.5,182.5,'4','black')
num5 = drawPoint(137.5,182.5,'5','black')
num6 = drawPoint(187.5,182.5,'6','black')
nummult = drawPoint(237.5,182.5,'x','black')
num1 = drawPoint(87.5,232.5,'1','black')
num2 = drawPoint(137.5,232.5,'2','black')
num3 = drawPoint(187.5,232.5,'3','black')
numadd = drawPoint(237.5,232.5,'+','black')
numplusmin = drawPoint(87.5,282.5,'+/-','black')
num0 = drawPoint(137.5,282.5,'0','black')
numdecimal = drawPoint(187.5,282.5,'.','black')
numminus = drawPoint(237.5,282.5,'-','black')
numdel = drawPoint(187.5,332.5,'del','black')
numeq = drawPoint(237.5,332.5,'=','black')


num7.draw(win)
num8.draw(win)
num9.draw(win)
numdiv.draw(win)
num4.draw(win)
num5.draw(win)
num6.draw(win)
nummult.draw(win)
num1.draw(win)
num2.draw(win)
num3.draw(win)
numadd.draw(win)
numplusmin.draw(win)
num0.draw(win)
numdecimal.draw(win)
numminus.draw(win)
numdel.draw(win)
numeq.draw(win)













