"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.

# Create the start_game function.
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.



# Imports the random module
import random
# Constants
RANGE_START = 1
RANGE_END = 10
# Stores high_score as a global variable to maintain it outside of each loop of the game
high_score = 10

# Defining a start_game() function
def start_game(name, current_high_score):
    #Produces random number
    answer = random.randint(1, 10)
    player_guess = 0
    # Keep track of score in game
    number_of_attempts = 1
    while player_guess != answer:
        #Handle errors
        try:
            player_guess = int(input("{}, guess a number from {} to {}:  ".format(name, RANGE_START, RANGE_END)))
            # Error hnadling for number out of range
            if player_guess < RANGE_START or player_guess > RANGE_END:
                raise ValueError("Your guess is out of range.")
        except ValueError as err:
            # Manage the error message provided depnding on the type of error
            err = err
            if "base 10" in str(err):
                err = "Try again."
            print("{} Enter a number between {} and {}:  ".format(err, RANGE_START, RANGE_END))
        else:
            if player_guess > answer:
                print("It's lower  ")
                number_of_attempts += 1
            elif player_guess < answer:
                print("It's higher  ")
                number_of_attempts += 1
            else:
                print("Well done {}, you got it. The number was {} and you took {} attempts. ".format(name, answer, number_of_attempts))
                print("Game Over")
                # if the number of attemps is less than the current high score, store a new high score in the global variable high_score 
                if number_of_attempts < current_high_score:
                    global high_score
                    high_score = number_of_attempts

# Defining a function to manage the game
def play_game():
    # Print the welcome message
    print("----------------------------\nTHE GUESSING GAME\n----------------------------")
    # Provide a elcome  message and ask the player's name
    user_name = input("Welcome, what is your name?  ")
    play_again = "y"
    while play_again.lower() == "y":
        print("{}, the current high score (least amounnt of guesses) is {}".format(user_name, high_score))
        # Call the start_game function 
        start_game(user_name, high_score)
        # Ask the user if the want to play again which will continue or end the while loop
        play_again = input("{}, would you like to play again Y/N ".format(user_name))
    # Goodbye message
    print("Goodbye")

# Call a function to manage te game        
play_game()