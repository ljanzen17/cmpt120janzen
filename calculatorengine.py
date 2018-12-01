# calculatorengine.py
from calculator_functions import *
class CalculatorEngine:
    def __init__(self):
        pass

    def process(self, key,ineq,mem):
        print(mem)
        if key == "=":
            #return(solveEquation(ineq))
            return False
        elif key == "m+":
            mem = ineq[-1]
            print(mem)
            return False
        elif key == "mr":
            return(mem)
        elif key == "m-":
            mem = ""
            return False
        elif key == "del":
            ineq = ineq[-1]
            return "del"
            
        
        
        else:
            print(key)
            return key

