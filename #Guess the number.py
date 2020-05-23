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

while 0 < max_count: 
    user_guess =  int(input(f'What is your guess? You have {max_count} attempts left. '))
    max_count -= 1
    #will keep a count of attempts

    if user_guess in my_list:
        print("You have already guessed " + str(user_guess))
        continue
    my_list.append(user_guess)
    #will keep track of guesses 

    count += 1

    if user_guess > user_num:
        print(f"Please keep number under {user_num}!")
    elif user_guess > random_num:
        print("Guess lower")
    elif user_guess < random_num:
        print("Guess higher")
    elif user_guess == random_num:
        print(f"Woohoo! You got it right in {count} attempts!")
        break
    #to check if user sent in correct #
else:
    if count == 8:
        print("You have failed to guess within 8 tries, you lose.")