'''
This is a simple pig latin translator
'''

def pig_latin():
    translate = True

    while translate is True:

        vowels = ['a','e','i','o','u']
        word = input("Please enter a word for translation:  ")

        # first check to see if first letter of word is a consonant
        # if it is, take the first letter and move it to the end of the word
        # then add ay to the end
        # e.g. cheers = heerscay

        if word[0] not in vowels:
            out_word_cons = word[1:] + word[0] + 'ay'

        # if the first letter is a vowel, then just add ay to the end of the word
        else:
            out_word_cons = word + 'ay'

        print(out_word_cons.lower())

        # Check to see if the user wants to enter another word
        x = input('Would you like to translate another word? (y/n)  ')

        if x[0].lower() == 'y':
            translate = True
        else:
            translate = False

pig_latin()
