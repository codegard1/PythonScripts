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

def censor(text, word):
    print(text, '/', word) #debugging
    i = 0 
    c = 0
    wordlist = text.split(' ')
    for i in range(len(wordlist)): #take each token from text in turn
        print(i, wordlist[i]) #debugging
        if wordlist[i].lower() == word.lower(): #if w = word
            for c in wordlist[i]:
                c = '*'
            print(wordlist[i])
    return ' '.join(wordlist)


t = 'This shit is whack'
w = 'shit'
print(censor(t, w))
