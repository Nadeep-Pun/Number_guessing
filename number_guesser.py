import random

print("Welcome to the Number Guesser game!!!")
print("You will only get 7 tries.")


while True:
    play = input("\nDo you want to play? Type 'Y' for yes and 'N' for no. \n").lower()
    if play == 'y':
        rangeNumber = int(input("Enter a range: "))
        randomNumber = random.randint(0, rangeNumber)
        for i in range(0, 7):
            guess = int(input("Make a guess: "))
            if guess == randomNumber:
                print("You are correct!!!!")
                break
            elif guess < randomNumber:
                print("Your guess was less than the number.")
            else:
                print("Your guess was greater than the number.")
            
            if i == 6:
                print(f"You failed to guess the number correctly.\nThe correct answer is {randomNumber}.")
    elif play == 'n':
        quit()
    else:
        print("Please enter 'Y' or 'N'.")
