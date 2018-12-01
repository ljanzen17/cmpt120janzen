# display.py
from graphics import *

class Display:
    def __init__(self, win):
        self.rect = Rectangle(Point(.5,6.75),Point(4.5,5.75))
        self.rect.setFill("white")
        self.rect.draw(win)
        self.text = Text(Point(3,6),"")
        self.text.setSize(25)
        self.text.draw(win)
        
        
    def update(self, text):
        print("update called, text = ",text)
        self.text.setText(text)
        
