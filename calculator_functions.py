# calculator_functions.py
def main():
    equation = input("Please enter an equation (use spaces):")
    listEquation = equation.split()
    result = solveEquation(listEquation)
    print(result)

def modifyEquation(idx, eq, value,cParen = 0):
    # remove the two operands and the operqator

    if cParen:
        # remove everything in between the parentheses including the parentheses
        del eq[idx+1:cParen+1]
        print(eq)
        # insert the result
        eq.insert(idx+1,value)
        print(eq)
        idx = idx -1
        return idx,eq

    else:
        del eq[idx:idx + 2]
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
    if '(' in eq:
        if ')' not in eq:
            print("")
            result = "ERROR NO CLOSE PARENTHESES"
            print("No close p")
            # ADD MODIFYEQUATION PART HERE
        else:
            print("IN ELSE")
            result = solveEquation(eq[eq.index('(')+1:eq.index(')')])
            print("RESULT", result)
            opIdx, eq = modifyEquation(opIdx, eq, result, cParen = eq.index(')'))


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
