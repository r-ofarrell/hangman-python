# from ~/Documents/python/hangman_game/word_list.py import wordlist
# import random
# import string


def get_valid_word(words):
    word = random.choice(words)   
    return word
    # while '_' in word or ' ' in word:
    #     word = random.choice(words)

print(word)
x = ['banana']

# Code to successively iterate over every letter for every word in a list.
for word in range(len(x)):
    for letter in range(len(x[word])):
        if input() == x[word][letter]:
            print(x[word][letter])
        else:
            print("That letter is not in the word")
