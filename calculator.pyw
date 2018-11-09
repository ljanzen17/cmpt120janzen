# calculator.pyw
# This program builds a graphical calculator keypad
from graphics import *
from calculator_functions import *
def createButton(values):
    p1 = Point(values[0], values[1])
    p2 = Point(values[0] + .9, values[1] + .9)
    button = Rectangle(p1, p2)
    button.setFill("lightblue")
    label = Text(Point(values[0] + .5, values[1] + .5), values[2])
    label.setStyle("bold")
    return button, label
def createKeypad(lst):
    keys = []
    for key in lst:
        button, label = createButton(key)
        keys.append([button, label])
    return keys
def renderKeys(keys, win):
    for key in keys:
        key[0].draw(win)
        key[1].draw(win)
# return the value of the button to append to the equation
def getButton(click, keyList):
    x = click.getX()
    y = click.getY()
    for i in range(len(keyList)):
        if keyList[i][1] == int(y):
            for j in range(i,len(keyList)):
                if keyList[j][0] == int(x):        
                    if keyList[j][2] in ['x','/','+','-']:
                        return " " + keyList[j][2] + " "
                    elif keyList[j][2] == "+/-":
                        return " x -1 "
                    
                    else:
                        return keyList[j][2]      
        
def main():
    keyList = [[0,0,'+/-'], [1,0,'0'],  [2,0,'.'],  [3,0,'='],
               [0,1,'1'],   [1,1,'2'],  [2,1,'3'],  [3,1,'+'],
               [0,2,'4'],   [1,2,'5'],  [2,2,'6'],  [3,2,'-'],
               [0,3,'7'],   [1,3,'8'],  [2,3,'9'],  [3,3,'x'],       
               [0,4,'del'],    [1,4,'m+'],   [2,4,'m-'],   [3,4,'/'], [4,4,'MR']]
    
    keys = createKeypad(keyList)
    win = GraphWin("Key Pad")
    win.setCoords(0.0, 0.0, 5.2, 6.0)
    win.setBackground("navy")
    display = Rectangle(Point(0,6),Point(4,5))
    display.setFill("white")
    display.draw(win)
    text = Text(Point(2,5.5),"")
    text.draw(win)
    renderKeys(keys, win)
    mem =[]
    equation = "";
    while True:
        click = win.getMouse()
        print(click.getX(),click.getY())
        buttonText = getButton(click, keyList)
        print(buttonText)
        if buttonText == "=":
            result = solve(equation)
            equation = str(result)
        elif buttonText == "del":
            equation = equation[:-1]
        elif buttonText == "m+":
            if len(mem) >0:
                mem = []
            mem.append(equation)
        elif buttonText == "MR":
            if len(mem) == 0:
                pass
            else:
                equation += mem[0]
        elif buttonText == "m-":
            mem=mem[:-1]
        else:
            equation = equation + buttonText
        text.setText(equation.rjust(35))
main()
        
    
           
