#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
choice=random.randint(1,10)
no_of_guesses=3
wanna_play=input("If you want to play the game ? Type (yes/no)  ").lower()
if wanna_play=='yes':
    while no_of_guesses>=1:
        guess=int(input("Enter the number  "))
        if 10>=guess>=1:
            if guess==choice:
                print(f"Congratulations , you have guesses the answer in {4-no_of_guesses} guesses)") 
                break
            else:
                no_of_guesses-=1
                print(f'Oops thats wrong , you have {no_of_guesses} gueses left')
        else:
            print("Number must be entered in between 1 and 6")
            continue
    else:
        print("The correct answer is {}".format(choice))
else:
    print("Okay , lets try again some other time")
