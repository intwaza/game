print("Welcome to guessing game")

start = 1
while True:
    guessing = input("select(Easy,Normal,Difficult):")
    if guessing == 'easy' or guessing == 'Easy' or guessing == 'EASY':
        end = 10
        break
    elif guessing == 'normal' or guessing == 'Normal' or guessing == 'NORMAL':
        end = 20
        break
    elif guessing == 'difficult' or guessing == 'Difficult' or guessing == 'DIFFICULT':
        end = 50
        break
    else:
        print('wrong input')

import random

number = random.randint(start, end)
while True:
    print("number from", start, "to", end, "generated")
    guess = int(input("Guess the number: "))
    if guess == number:
        print("you did it")

    elif guess > end or guess < start:
        print("incorect number")
    elif guess < number:
        print("guess again")
    elif guess > number:
        print("guess again")
    else:
        print("Stop")
















