import random

no = random.randrange(1,100)
guess = int(input("Guess a no between 1 and 100 : "))

while(guess!=no):
    if(guess<no):
        print("You need to guess higher..Try again")
        guess = int(input("\nGuess a no between 1 and 100 : "))

    else:
        print("You need to guess lower..Try again")
        guess = int(input("\nGuess a no between 1 and 100 : "))


print("You guessed the number correcttly!")
