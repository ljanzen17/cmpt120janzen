#guessing-game.py
animal = 'dog'
end = 'quit'
while animal != 'guess':
    print('The program is thinking of an animal. Please try to guess the name of the animal')
    guess = input()
    if (guess.lower() != animal and guess.lower()[0] != end[0]) :
        print("Sorry that is the wrong animal, please try again. If you would like to give up type quit when it asks for the animal name.")
    elif guess.lower()[0] == end[0]:
        print('Thanks for playing!')
        break
    else:
        print('Yes, that is the animal I was thinking of. Congratulations!')
        print('If you like this animal type y if you do not type n')
        like = input()
        if like =='y':
                print("I agree, that is a great animal!")

        else:
                print("I don't like that animal either.")
        break
    break

     

    

