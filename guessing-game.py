#guessing-game.py
animal = 'dog'
end = 'quit'
while animal != 'guess':
    print('The program is thinking of an animal. Please try to guess the name of the animal')
    guess = input()
    if (guess.lower() != animal and guess.lower() != end) :
        print("Sorry that is the wrong animal, please try again. If you would like to give up type quit when it asks for the animal name.")
    elif guess.lower() == end:
        break
    else:
        print('Yes, that is the animal I was thinking of. Congratulations!')
        break

    

    

