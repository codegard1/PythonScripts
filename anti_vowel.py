# Define a function called anti_vowel that takes one
# string, text, as input and returns the text with
# all of the vowels removed.
# For example: anti_vowel("Hey You!") should return
# "Hy Y!".
# Don't count Y as a vowel.
# Make sure to remove lowercase and uppercase vowels.

passage = '''We hold these truths to be self evident,
that all men are created equal!'''


def anti_vowel(text):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    text = list(text)
    i = 0 
    while i < len(text):
        if text[i] in vowels:
            del(text[i])
            print(i)
            i = i
        else:
            print(text[i])
            i += 1
            
    s = ''.join(text)
    return s

print(anti_vowel(passage))
