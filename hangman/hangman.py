"""Hangman"""

import random

def play_game():
    """
    Initiate the game
    :return:None
    """
    print("let the game start")
    tries = 8
    guessed_character = []
    answer = chose_word()
    secret = list("-" * (len(answer) - len(guessed_character)))
    print(secret)
    while tries > 0:

        guess = input("Guess the word: ")
        if check_valid(guess): #check if user input is valid
            print("Please enter a single letter in english and lowercase.")
            continue

        if guess in answer and not guess in secret:
            update_secret(answer, secret, guess)
            print("you are right")
            print(secret)
        elif guess in guessed_character:
            print("You've already guessed this letter.")
        else:
            print("That letter doesn't appear in the word")
            guessed_character.append(guess)
            tries -= 1
        if check_result(secret, answer, tries):
            break

def start_game():
    """
    starts game in waits user input
    :return:none
    """
    while True:
        print('Type "play" to play the game, "exit" to quit:')
        start = input()
        if start == 'exit':
            print("thanks for playing")
            break
        elif start == 'play':
            play_game()
        else:
            print("sorry can't understand you")
            continue

def update_secret(answer, secret, guess):
    """
    update secret if user was right
    :param answer: what user needs to guess
    :param secret: what user already guessed
    :param guess: user's input
    :return: none
    """
    for i in range(len(secret)):
        if guess == answer[i]:
            secret[i] = guess

def chose_word():
    """
    randomly choses word
    :return: string
    """
    avail_words = ['python', "java", "javascript", "php"]
    return random.choice(avail_words)

def check_valid(guess):
    """
    check`s if user's input is valid, returns True if not
    :param guess: user's input
    :return: True or False
    """
    return len(guess) != 1 or not guess.islower() or not ('a' <= guess <= 'z')

def check_result(secret, answer, tries):
    """
    checks if user guessed the secret, if False game continues
    :param secret: what user needs to guess
    :param answer: what must be guessed
    :param tries: user's tries left
    :return: True or False
    """
    if secret == list(answer):
        print("you survived")
        return True
    elif tries <= 0:
        print(loss)
        return True
    return False





print("HANGMAN")

loss = r'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
you dead lol
'''

start_game()
