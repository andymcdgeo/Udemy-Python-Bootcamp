vowels = ['a','e','i','o','u']

x = input('Enter a sentence or word:  ')

v_count = 0
c_count = 0
space_count = 0
word_len = len(x)


for i in x:
    if i in vowels:
        v_count +=1
    else:
        if i != ' ':
            c_count += 1
        else:
            space_count +=1

character_count = word_len - space_count
print('\n')
print(f'Your chosen strings is:                              {x}')
print(f'The total number of spaces in your string is:        {space_count}')
print(f'The total number of characters in your string is:    {character_count}')
print(f'The total length of your string is:                  {word_len}')
print(f'The total number of vowels in your string is:        {v_count}')
print(f'The total number of consonants in your string is:    {c_count}')


