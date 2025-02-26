import random
import os

os.system("clear")
while True:
    print("-----------TRY YOUR LOCK HERE-----------------")
    count = 0
    numberToGuess = int(random.random()*100)+1
    while True:
        gussedNumber = int(input("Guess a Number: "))
        count+=1
        if numberToGuess == gussedNumber:
            print("----------------------------------------------------")
            print("Congratulation, You guessed the number",numberToGuess)
            print("You guessed the number in",count,"Attempts.")
            break
        elif numberToGuess>gussedNumber:
            print("Higher number Please")
        elif numberToGuess<gussedNumber:
            print("Lower Number Please")
        else:
            print("Invalid Input!")
    print("Press enter to continue (n to end)? ")
    resume = input("")
    os.system("clear")
    if resume == 'n':
        break