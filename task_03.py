def user_input():

    games_word_list = ['too small', 'too big', 'you won']

    while True:
        user = input("write down result: ")
        user = user.lower()
        if user in games_word_list:
            break
        print("your input not correct, try again")
    return user



def guess_computer_figures():
    print("welcome in my games!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print("""In this game computer will guess figures in range 0 - 1000.
If your figures will be the same like computer,
please write down 'you won'. if figures will be lower,
please write down 'too small'. If figures will be
bigger please write down 'too big' """)
    print("--------------------------------")
    print('image figures in range 0 - 1000')
    print("--------------------------------")
    input("please enter to continue: ")


    min_number = 0
    max_number = 1000



    while True:
        guess = int((max_number - min_number)/2)+min_number
        print('I guess... this is: ', guess)
        user_feedback = user_input()

        if user_feedback == 'too small':
            min_number = guess + 1
        elif user_feedback == 'too big':
            max_number = guess - 1
        elif user_feedback == 'you won':
            print('You won!!!')
            break



print(guess_computer_figures())

