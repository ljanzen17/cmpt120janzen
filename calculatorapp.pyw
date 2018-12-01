# calculatorapp.pyw
from graphics import *
from display import *
from keypad import *
from calculatorengine import *


class CalculatorApp:
    def __init__(self):

        self.win = GraphWin("Calculator", 400, 600)
        self.win.setCoords(0,0,5,7)
        self.display = Display(self.win)
        self.display.update("10")

        self.keypad = Keypad(self.win)
        
        self.calcEngine = CalculatorEngine()        

    def run(self):
        ineq = []
        mem = ""
        while True:
            click = self.win.getMouse()
            # Get the key that was pressed
            key = self.keypad.getKey(click)
           
            # Process the key and get the result
            result = self.calcEngine.process(key,ineq,mem)
            # Display the result
            print("result = ", result)
            if not result and key not in['+','-','/','x','-/+',"del"]:
                if key == "m+":
                    mem = ineq[-1]
                elif key == "m-":
                    mem = ""
                elif key == "mr":
                    ineq.append(result)
                elif key == "=":
                    self.display.update(solveEquation(ineq))
                    ineq = [solveEquation(ineq)]

                    
            elif result == "del":
                ineq = []
                self.display.update("")
            elif result == "-/+":
                if ineq[-1] not in ['+','-','/','*','=','-/+']:
                    ineq[-1] = str(float(ineq[-1])*-1)
                    self.display.update(ineq[-1])
                else:
                    pass
            else:
                if len(ineq) == 0:
                    ineq.append(result)
                elif result in['+','-','x','/']:
                    if ineq[-1] not in ['+','-','x','/']:
                        ineq.append(result)
                    else:
                        pass
                else:
                    if str(ineq[-1])[0] in ['1','2','3','4','5','6','7','8','9','0']:
                        ineq[-1] = str(ineq[-1]+result)
                        self.display.update(ineq[-1])
                    else:
                        ineq.append(result)

                        

            print(ineq)
        

def main():
    calc = CalculatorApp()

    calc.display.update("0")
    calc.run()

main()
