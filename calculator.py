#calculator.py
def get_user_input():
    userinput = list(input("Please enter an expression"))
    parts = []
    pointer1 = 0
    pointer2 = 0

    #checks to find location of operator and takes number before it
    for a in userinput:
        if a in ['*','/','+','-']:
            parts.append(''.join(userinput[pointer1:userinput.index(a)]))
            parts.append(a)
            pointer1 = userinput.index(a)+1

        #increments pointer 2 if operator isnt in rest of string
        for i in userinput[pointer1:]:
            if i in ['1','2','3','4','5','6','7','8','9','0']:
                pointer2 =1 + pointer2

                if pointer2 == len(userinput):
                    pass
    parts.append(''.join(userinput[pointer1:]))

    return(parts)

#
def main():
    exp_parts = get_user_input()
    result = 0
    while exp_parts:
        #if there is only a number and an operator handle accordingly
        if len(exp_parts) == 2:
            if '-' in exp_parts:
                if exp_parts.index('-') > 0:
                    result = float(exp_parts[0]) - result
                else:
                    result = result - float(exp_parts[0])

            elif '/' in exp_parts:
                if exp_parts.index('/') > 0:
                    result = float(exp_parts[0]) / result
                else:
                    result = result / float(exp_parts[0])

            elif '+' in exp_parts:
                del exp_parts[exp_parts.index('+')]
                result = result + float(exp_parts[0])

            elif '*' in exp_parts:
                del exp_parts[exp_parts.index('*')]
                result = result + float(exp_parts[0])

            exp_parts = []
        #checks to see if there are any * left
        if '*' in exp_parts:
            num1 = float(exp_parts[exp_parts.index('*')-1])
            num2 = float(exp_parts[exp_parts.index('*')+1])
            result = num1 * num2
            del exp_parts[exp_parts.index('*')-1:exp_parts.index('*')+2]
        #checks to see if there are any / left
        elif '/' in exp_parts:
            num1 = float(exp_parts[exp_parts.index('/')-1])
            num2 = float(exp_parts[exp_parts.index('/')+1])
            result = num1 / num2
            del exp_parts[exp_parts.index('/')-1:exp_parts.index('.')+2]
        #checks to see if there are any + left
        elif '/' in exp_parts:
            print(exp_parts)
            num1 = float(exp_parts[exp_parts.index('+')-1])
            num2 = float(exp_parts[exp_parts.index('+')+1])
            result = num1 + num2

            del exp_parts[exp_parts.index('+')-1:exp_parts.index('+')+2]
        #checks to see if there are any - left
        elif '-' in exp_parts:
            num1 = float(exp_parts[exp_parts.index('-')-1])
            num2 = float(exp_parts[exp_parts.index('-')+1])
            result = num1 - num2
            del exp_parts[exp_parts.index('-')-1:exp_parts.index('-')+2]

        print(exp_parts)

    print(result)

main()


