# keypad.py
from button import *

class Keypad:
    def __init__(self, win):
        self.buttons = [
            Button(win, Point(1,1), .75, .75, '-/+'),
            Button(win, Point(1.75,1), .75, .75, '0'),            
            Button(win, Point(2.5,1), .75, .75, '.'),
            Button(win, Point(3.25,1), .75, .75, '='),
            Button(win, Point(4,1), .75, .75, 'mr'),
            Button(win, Point(1,2), .75, .75, '1'),
            Button(win, Point(1.75,2), .75, .75, '2'),
            Button(win, Point(2.5,2), .75, .75, '3'),
            Button(win, Point(3.25,2), .75, .75, '+'),
            Button(win, Point(1,3), .75, .75, '4'),
            Button(win, Point(1.75,3), .75, .75, '5'),
            Button(win, Point(2.5,3), .75, .75, '6'),
            Button(win, Point(3.25,3), .75, .75, '-'),
            Button(win, Point(1,4), .75, .75, '7'),
            Button(win, Point(1.75,4), .75, .75, '8'),
            Button(win, Point(2.5,4), .75, .75, '9'),
            Button(win, Point(3.25,4), .75, .75, 'x'),
            Button(win, Point(1,5), .75, .75, 'del'),
            Button(win, Point(1.75,5), .75, .75, 'm+'),
            Button(win, Point(2.5,5), .75, .75, 'm-'),
            Button(win, Point(3.25,5), .75, .75, '/')]

     
    def getKey(self, p):
        for button in self.buttons:
            if button.clicked(p):
                return (button.getLabel())
