printed_word = ['_','_','_',' ','_','_','_','_',' ','_','_',' ','_','_','_','_','_']

def update_hangman_lines(player_guess, word):
    '''Adds letters to blank hangman lines to represent the secret word in hangman'''
    for letter in range(len(word)):
        if player_guess == word[letter]:
            printed_word[letter] = player_guess

        
        else:
            pass

    print(''.join(printed_word))
    return ''.join(printed_word)

update_hangman_lines('i', 'The King is alive')
