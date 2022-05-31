import random

def guess(n):
    guess = 0
    random_number = random.randint(1, n)

    while guess != random_number:
        guess = int(input("Enter your guess number: "))
        if guess > random_number:
            print("your are above the number")
        elif guess < random_number:
            print("your are below the number")
    
    print("****** Congrats! you guess the number ********")

guess(100)