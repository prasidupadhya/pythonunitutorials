import random

hidden = random.randint(1,20)

guess = int(input("Guess the number between 1 and 20:"))
#print(hidden)

while guess != hidden:
    if guess > hidden:
        print("The number is too high, guess again between 1 and 20.")
    elif guess < hidden:
        print("The number is too low, guess again between 1 and 20.")

    guess =  int(input("Guess the number between 1 and 20:"))

print("Correct, you've guessed it")
