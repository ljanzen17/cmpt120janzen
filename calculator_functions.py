# calculator_functions.py
def main():
    equation = input("Please enter an equation (use spaces):")
    listEquation = equation.split()
    result = solveEquation(listEquation)
    print(result)

def modifyEquation(idx, eq, value):
    # remove the two operands and the operqator
    del eq[idx - 1:idx + 2]
    # insert the result
    eq.insert(idx - 1, value)
    # move the index back one place
    idx = idx - 1
    return idx, eq

def solve(eq):
    equation = eq.split()
    return solveEquation(equation)
    
def solveEquation(eq):
    opIdx = 1
    while 'x' in eq or '/' in eq:
        if eq[opIdx] == 'x':
            # calculate the operation
            result = float(eq[opIdx - 1]) * float(eq[opIdx + 1])
            # update the equation list
            opIdx, eq = modifyEquation(opIdx, eq, result)
        elif eq[opIdx] == '/':
            result = float(eq[opIdx - 1]) / float(eq[opIdx + 1])
            opIdx, eq = modifyEquation(opIdx, eq, result)
        else:
            opIdx = opIdx + 1    
        if opIdx >= len(eq):
            break
    opIdx = 1 
    while '+' in eq or '-' in eq:
        if eq[opIdx] == '+':
            result = float(eq[opIdx - 1]) + float(eq[opIdx + 1])
            opIdx, eq = modifyEquation(opIdx, eq, result)
        elif eq[opIdx] == '-':
            result = float(eq[opIdx - 1]) - float(eq[opIdx + 1])
            opIdx, eq = modifyEquation(opIdx, eq, result)
        else:
            opIdx = opIdx + 1
        if opIdx >= len(eq):
            break
    return eq[0]
            
#main()
