# calculatorapp.pyw
from graphics import *
from display import *
from keypad import *
from calculatorengine import *
from math import cos,sin,tan,acos,asin,atan

class CalculatorApp:

    def __init__(self):

        self.win = GraphWin("Calculator", 500, 600)
        self.win.setCoords(0,.5,4.5,5.5)

        self.display = Display(self.win)


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
            elif key == 'cos':
                if len(ineq)== 1 and float(ineq[0]):
                    ineq = [cos(float(ineq[0]))]
                    self.display.update(ineq[0])
                else:
                    break
            elif key == 'sin':
                if len(ineq)== 1 and float(ineq[0]):
                    ineq = [sin(float(ineq[0]))]
                    self.display.update(ineq[0])
                else:
                    break
            elif key == 'tan':
                if len(ineq)== 1 and float(ineq[0]):
                    ineq = [tan(float(ineq[0]))]
                    self.display.update(ineq[0])
                else:
                    break
            elif key == 'acos':
                if len(ineq)== 1 and float(ineq[0]):
                    if float(ineq[0])>-1 and float(ineq[0])<1:
                        ineq = [acos(float(ineq[0]))]
                        self.display.update(ineq[0])
                    else:
                        self.display.update("err domain")
                else:
                    break
            elif key == 'asin':
                if len(ineq)== 1 and float(ineq[0]):
                    if float(ineq[0])>-1 and float(ineq[0])<1:
                        ineq = [asin(float(ineq[0]))]
                        self.display.update(ineq[0])
                    else:
                        self.display.update("err domain")
                else:
                    break
            elif key == 'atan':
                if len(ineq)== 1 and float(ineq[0]):
                    ineq = [atan(float(ineq[0]))]
                    self.display.update(ineq[0])
                else:
                    break
            else:
                if len(ineq) == 0:
                    ineq.append(result)
                elif result in['+','-','x','/']:
                    if ineq[-1] not in ['+','-','x','/']:
                        ineq.append(result)
                    else:
                        pass
                elif result in['(',')']:
                    ineq.append(result)
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
