#Guess the number

import random

action = True #helps control the while loop

while action:
    user_num = input('Type a maximum number:')

    if user_num.isdigit():
        print("Let's get guessing!")
        user_num = int(num)
        action = False
    #Gets a user's input for a number
    #Ensures that user's input is a number
    #Converts to integer
    #Stops while loop

    else:
        print ('Please enter a valid number!')
+