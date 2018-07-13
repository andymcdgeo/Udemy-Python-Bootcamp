'''
Hangman
'''

import random

word = ['test', 'dog', 'cat']
guesses = 0
turns = 10

guessed_letters= ''

playing = True


def word_picker():
    word_position = random.randint(0, len(word)-1)
    return word[word_position]

print(word_picker())






