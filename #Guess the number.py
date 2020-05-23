#Guess the number

import random

action = True #helps control the while loop
print("Welcome to the Guessing Game!")
print("You only get 8 tries.")
while action:
    user_num = input('The computer will generate a random number, ranging from 1 to X. What would you like to set X as?')

    if user_num.isdigit():
        print("Let's get guessing!")
        user_num = int(user_num)
        action = False
    #Gets a user's input for a number
    #Ensures that user's input is a number
    #Converts to integer
    #Stops while loop
    else:
        print ('Please enter a valid number!')

random_num = random.randint(1, user_num) #generates random number
user_guess = None #for users guess input
count = 0 #to count how many guesses
max_count = 8 #max guesses
my_list = [] #to store guesses