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
    n = 0
    wordlist = text.split(' ')
    
    for i in range(len(wordlist)): #take each token from text in turn
        #print(i, wordlist[i]) #debugging

        if wordlist[i].lower() == word.lower(): #if w = word
            replacement = list(wordlist[i])
            
            for n in range(len(replacement)):
                replacement[n] = '*'
                n += 1
                
            wordlist[i] = ''.join(replacement) #rejoin the replacement list chars
    wordlist = ' '.join(wordlist) # recreate the sentence str       

    return wordlist #return the str


t = 'Once there was a man whose men were men and whose man was a men'
w = 'man'

print(censor(t, w))
