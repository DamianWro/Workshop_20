import random

def guess_number():
    """this function will guess the number between 1 and 100"""
    number = random.randint(1,100)
    while True:
        try:
            guess = input('Guess the number: ')
            guess = int(guess)
            if guess == number:
                print("You win!")
            elif guess < number:
                print("Too small!")
            elif guess > number:
                print("Too big!")
        except ValueError:
            print("It's not a number!")
    return number


print(guess_number())