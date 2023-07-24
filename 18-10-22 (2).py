import random

hidden = random.randint(1,20)

guess = int(input("Guess the number between 1 and 20:"))
#print(hidden)

while guess != hidden:
    print("The number is incorrect, try again between 1 and 20")
    guess =  int(input("Guess the number between 1 and 20:"))


print("Correct, you've guessed it")
