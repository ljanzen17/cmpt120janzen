#guessing-game.py
animal = 'dog'
while animal != 'animal':
    print('The program is thinking of an animal. Please try to guess the name of the animal')
    animal = input()
    if animal != 'dog':
        print("Sorry that is the wrong animal, please try again")
    else:
        print('Yes, that is the animal I was thinking of. Congratulations!')
        break
    

    

