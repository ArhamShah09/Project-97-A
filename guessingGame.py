import random
number = random.randint(1,9)
chances = 5
print("Number guessing game")
print("Guess a number between 1 to 9:")

while(chances < 6 and chances > 0):
    guesses = int(input("Enter your guess : "))
    if(guesses < number):
        print("Your guess was too low ; Guess a number higher than ", guesses)
        guesses = int(input("Enter your guess : "))
        chances = chances-1
    if(guesses > number):
        print("Your guess was too high ; Guess a number lower than ", guesses)
        guesses = int(input("Enter your guess : "))
        chances = chances-1
    if(guesses == number):
        print("Congradulation You Won!!!")
        break
if(chances == 0):
    print("YOU LOSE!!! The number is ", number)

