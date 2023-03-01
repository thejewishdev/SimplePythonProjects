# Hello and welcome to The Number Guessing Game tutorial!

# Here we r going to create a simple game in which we r gonna need to guess a number randomly picked by our computer
# Some requirements : 1- give player 6 attempts to guess ( 6  incorrect guesses = GameOver )
# 2- Every time player makes incorrect guess , we will display the amount of attempts left
# 3- Every time player makes incorrect guess , we will give a hint (try greater or lesser numbers)

# Let's dive into the thing now.


# Import random features
import random

# Create a list to store all possible numbers for our computer to randomly chose
numbers = []

# Create numbers from 1 to 100 and add them to out list we created above
for x in range(1, 101):
    numbers.append(x)

# Randomly pick a number we are gonna need to guess
number_to_guess = random.choice(numbers)

# Set attempts 0 for while loop check ( for bg )
attempt = 0

# Set attempts to display for the player
attempts_left = 6

# Execute the code inside the while block , while our player has some attempts left
while attempt < 6:

    # Take the user's guess
    user_input = input(f"Guess the number (1 - 100) (ATTEMPTS LEFT : {attempts_left}) > ")

    # Check the user's answer to the actual number to guess
    if int(user_input) == number_to_guess:
        print("Well Done!")
        break
    elif int(user_input) < number_to_guess and int(user_input) > 0 and int(user_input) < 100:
        if attempts_left != 1:
            print(F"TRY GREATER NUMBER")
            attempt += 1
            attempts_left -= 1
        else:
            attempt += 1
            attempts_left -= 1
    elif int(user_input) > number_to_guess and int(user_input) > 0 and int(user_input) < 100:
        if attempts_left != 1:
            print(F"TRY LESSER NUMBER")
            attempt += 1
            attempts_left -= 1
        else:
            attempt += 1
            attempts_left -= 1
    else:
        print("ONLY RANGE OF 1-100!")

# If our user is out of attempts ( which means he no longer will see the input part ) we r gonna say 'sorry u r out of attmepts'
else:
    print("Game Over! Out of attempts!")
    print(f"The number was : {number_to_guess}")
