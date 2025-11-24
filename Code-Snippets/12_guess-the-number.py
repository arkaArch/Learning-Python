import random

upper_limit = int(input("Choose an upper limit: "))
lower_limit = int(input("Choose an lower limit: "))

random_number = random.randint(lower_limit, upper_limit + 1)

guesses = 1
guess_limit = 3

while guesses <= guess_limit:
    guess_number = int(input("Guess the number: "))
    if guess_number == random_number:
        break
    elif guess_number < random_number:
        print("Actual number is higher than you guessed.")
    else:
        print("Actual number is lower than you guessed.")
    guesses += 1

if guesses <= guess_limit:
    print("\nYou have guessed the correct number.")
else:
    print("\nYou have failed to guess the correct number.\n"
          "The number was: ", random_number)
