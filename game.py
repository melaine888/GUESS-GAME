import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        
        if guess < random_number:
            print("Sorry! Guess again. Too low.")
        elif guess > random_number:
            print("Sorry! Guess again. Too high.")
            
    print(f"Yaay! You guessed the {random_number} correctly!!") 


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"is {guess} too high(H),too low(L) or correct(C)???").lower()
        if guess == "h":
            high = guess - 1
            
        elif guess == "l":
            low = guess + 1
            
    print(f"Yaaay! The computer guessed the number, {guess} correctly!")
    
guess(1000)
            