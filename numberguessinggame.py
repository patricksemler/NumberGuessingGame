import random

in_game = True

while (in_game):
    defaults = input("Do you want to use the default range of 1 to 1000? (y/n): ").strip().lower() == "y"

    min_bound = int(input("Minimum: ")) if not defaults else 1
    max_bound = int(input("Maximum: ")) if not defaults else 1000

    chosen_number = random.randint(min_bound, max_bound)
    guess = None

    while (guess != chosen_number):
        guess = int(input("Guess the number: "))

        if (guess < chosen_number):
            print("Too low!")
        elif (guess > chosen_number):
            print("Too high!")

    print("Congratulations! You guessed the number: " + str(chosen_number))

    in_game = input("Do you want to play again? (y/n): ").strip().lower() == "y"

print("Thanks for playing!")