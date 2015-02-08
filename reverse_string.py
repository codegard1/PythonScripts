# Define a function called reverse that takes a string
# text and returns that string in reverse.
# For example: reverse("abcd") should return "dcba".
# You may not use reversed or [::-1] to help you with
# this.
# You may get a string containing special characters
# (for example, !, @, or #).

def reverse(text):
    stringy_string = ''
    for i in range(len(text)):
        stringy_string += text[(len(text) - 1) - i]
    return stringy_string

#print(reverse('A man a plan a canal Panama'))

phrase = 'A man a plan a canal Panama'

def reverse2(text):
    listy_list = list(text)
    while listy_list: #empty list is False, so loop stops at that point!!
        result.append(listy_list.pop()) 
    return ''.join(result)

#print(reverse2(phrase))

def reverse3(text):
    listy_list = list(text) # make a list from the text
    n = len(listy_list)     # hold the length
    for i in range(int(n / 2)):  # iterate over half of the list
        temp = listy_list[i]
        listy_list[i] = listy_list[n - 1 - i]
        listy_list[n - 1 - i] = temp
    return ''.join(listy_list)

x = '''farting
is such
sweet
sorrow'''

print(reverse3(phrase))
