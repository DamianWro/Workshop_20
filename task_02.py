import random

def random_numbers(num):
    """this functions randomly generate numbers from 1 to 49"""
    x = []
    for i in range(num):
        secret_number = random.randint(1,49)
        x.append(secret_number)
    return sorted(x)


def get_user_numbers():
    """this is a input function for guess list"""
    while True:
        try:
            user_choice = input("guess the 6 numbers between 1 and 49: ")
            user_numbers = set()
            for i in user_choice.split(','):
                num = int(i)
                if 1 <= num <= 49:
                    user_numbers.add(num)
                else:
                    print("give me a number between 1 and 49!!!")



            if len(set(user_numbers)) == 6:
                return sorted(user_numbers)

            else:
                print('Provide exactly 6 valid unique numbers between 1 and 49!')

        except ValueError:
            print("Please enter ONLY an integer")


def lotto():
    guess_try = get_user_numbers()
    print("Your numbers:", guess_try)

    lucky_numbers = random_numbers(6)
    print("lucky numbers:", lucky_numbers)

    hits = 0
    for element in lucky_numbers:
        if element in guess_try:
            hits += 1
    print("you have:", hits, 'hits!')

    if guess_try == lucky_numbers:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")



lotto()
