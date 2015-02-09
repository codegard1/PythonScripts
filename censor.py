# Write a function called censor that takes two strings,
# text and word, as input. It should return the text with
# the word you chose replaced with asterisks.

# For example:

# censor("this hack is wack hack", "hack") 
# should return

# "this **** is wack ****"
# Assume your input strings won't contain punctuation or
# upper case letters.
# The number of asterisks you put should correspond to
# the number of letters in the censored word.

def censor(text, censor_word):
    print(text, '/', censor_word) #debugging
    words = text.split()
    i = 0
    for word in words:
        if word.lower() == censor_word.lower():
            words[i] = '*' * len(word)
        i += 1
    return ' '.join(words)

t = 'Once there was a man whose men were men and whose man was a men'
w = 'man'

print(censor(t, w))
