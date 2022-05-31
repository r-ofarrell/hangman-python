import random
import getpass

printed_word = []
lose_count = 0
guess_set = set()

def print_hangman_lines(word):
    '''Prints blank lines to represent the secret word in hangman'''
    for letter in word.word:

        if letter.isalnum():
            printed_word.append('_ ')

        elif letter == ' ':
            printed_word.append(' ')

    print(''.join(printed_word))
    print('\n')
    return ''.join(printed_word)


def update_hangman_lines(guess_word, hangman_word):
    '''
    Adds letters to blank hangman lines to represent the secret hangman_word in
    hangman
    '''
    global lose_count

    for letter in range(len(hangman_word.word)):
        if guess_word == hangman_word.word[letter]:
            printed_word[letter] = guess_word

        else:
            pass

    if guess_word in hangman_word.word_set:
        guess_set.add(guess_word)

    else:
        guess_set.add(guess_word)
        lose_count += 1


    print(''.join(printed_word))
    return ''.join(printed_word)


def player_guess():
    while True:
        guess =input('Enter a letter that you think is in the secret hangman word: ')

        if len(guess) > 1:
            print('Please enter only one letter')
            continue

        elif not guess.isalpha():
            print('Please enter a letter from A-Z')

        elif guess in guess_set:
            print('You have already guessed that letter. Please pick another letter')
            continue

        else:
            break

    return guess


def create_hangman_figure(number):
    if number == 1:
        print('''
            ----
            |  |
            O  |
               |
               |
               |
            ___|
            '''
            )

    elif number == 2:
        print('''
            ----
            |  |
            O  |
            |  |
               |
               |
            ___|
            '''
            )

    elif number == 3:
        print('''
            ----
            |  |
            O  |
           \|  |
               |
               |
            ___|
            '''
            )


    elif number == 4:
        print('''
            ----
            |  |
            O  |
           \|/ |
               |
               |
            ___|
            '''
            )

    elif number == 5:
        print('''
            ----
            |  |
            O  |
           \|/ |
           /   |
               |
            ___|
            '''
            )

    elif number == 6:
        print('''
            ----
            |  |
            O  |
           \|/ |
           / \ |
               |
            ___|
            '''
            )

    else:
        pass

class Hangman():

    def __init__(self, word):
        self.word = word
        self.word_set = set(word)

    def print_word(self):
        print_hangman_lines(self)
        

# START OF GAME
game_word = getpass.getpass('Enter your word or phrase for a game of hangman! ')

game1 = Hangman(game_word.lower())

game1.print_word()

if ' ' in game1.word_set:
    game1.word_set.remove(' ')

while True:
    guess = player_guess()  

    update_hangman_lines(guess, game1)
    create_hangman_figure(lose_count)
    print(f'Here are the letters you have guessed so far {guess_set}')

    # ADD WIN CONDITIONS HERE.

    if lose_count == 6:
        print('Player1 loses!')
        print(f'The word/phrase was: {game1.word}')
        break

    elif game1.word_set.issubset(guess_set):
        print('Player1 wins!')
        break

    else:
        continue
