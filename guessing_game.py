
import random

high_score = []
def start_game():
    print("Welcome to the Number Guessing Game!")
    try:
        print("Current High Score: {}".format(min(high_score)))
    except ValueError:
        print("No current high score.")
    number = []
    correct = random.randint(1,10)
    guess = input("Guess a number between 1 and 10: ")
    while guess == True:
        try:
            guess = int(guess)
            continue
        except:
            guess = input("Please enter a number between 1 and 10: ")
    while guess != correct:
        try:
            guess = int(guess)
            if guess > 10:
                guess = input("Please enter a number between 1 and 10: ")
                guess = int(guess)
            elif guess < correct:
                print("It's higher.")
                number.append(guess)
                guess = input("Try again: ")
                guess = int(guess)
            elif guess > correct:
                print("It's lower.")
                guess = input("Try again: ")
                number.append(guess)
                guess = int(guess)
        except:
            guess = input("Please enter a number between 1 and 10: ")
    guesses = len(number)
    guesses = int(guesses)
    guesses += 1
    high_score.append(guesses)
    print("Got it!")
    print("It took you {} tries to guess this answer.".format(guesses))
    replay = input("Would you like to play again?(Y/N): ")
    if replay == "Y":
        # I tried "if replay == "Y" or "y": and it restarted the game regardless of what value I entered. Not sure why as the value "n" would create
        # 2 False and the code should have moved to the else.
        start_game()
    elif replay == "y":
        start_game()
    else:
        print("Thank you for playing the Number Guessing Game!")
        exit = input("Press Enter to exit.")
start_game()