number =  int(input("Guess the number between 1 and 20:"))

while number != 6:
    print("The number is incorrect, try again between 1 and 20")
    number =  int(input("Guess the number between 1 and 20:"))

if number == 6:
        print("Correct, you've guessed it")
