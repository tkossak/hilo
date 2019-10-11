import random


def func():
    print("Welcome to the HI - LO game")
    num = random.randint(1, 100)
    while True:
        guess = int(input('Guess a number between 1 & 100: '))

        if guess == num:
            print(f'Got it: The number is {num}')
            break
        elif guess < num:
            print('Too low!')
        elif guess > num:
            print('Too high!')


func()

