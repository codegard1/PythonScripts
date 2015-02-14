# 1. Define a function called count that has two arguments
# called sequence and item.
# 2. Return the number of times the item occurs in the list.
# For example: count([1,2,1,1], 1) should return 3 (because
# 1 appears 3 times in the list).
# There is a list method in Python that you can use for this,
# but you should do it the long way for practice.
# Your function should return an integer.
# The item you input may be an integer, string, float,
# or even another list!
# Be careful not to use list as a variable name in your
# code—it's a reserved word in Python!

def count(sequence, item):
    i = 0
    for n in sequence:
        if n == item:
            i +=1
    return i

s = [1,3,6,7,4,5,6,7,8,5,4,3,2,6,7,4,3,3,'a','p','a','p','q','p',9,5,6,7,8,9,4,3,5,'a','a','a','a']
print(str(count(s, 'a')))
