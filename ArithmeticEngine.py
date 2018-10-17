# ArithmeticEngine.py
# CMPT 120 - Lab #6
# Lucas Janzen
# 10-16-2018
###
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def getNumbs():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return(num1, num2)
    
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")        
        if cmd.lower() == "add":
            num1,num2 = getNumbs()
            result = num1 + num2
        elif cmd.lower() == "sub":
            num1,num2 = getNumbs()
            result = num1 - num2
        elif cmd.lower() == "mult":
            num1,num2 = getNumbs()
            result = num1 * num2
        elif cmd.lower() == "div":
            num1,num2 = getNumbs()
            try:
                result = num1 // num2 # will crash because of division by zero
            except:
                print("Unable to divide by zero!")
                continue
        elif cmd.lower() == "quit":
            break
        else:
            print("That is an invalid command!")
            continue
        print("The result is " + str(result) + ".\n")
        
def main():
    showIntro()
    doLoop()
    showOutro()
main()
