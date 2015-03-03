# Write a function remove_duplicates that takes in a list
# and removes elements of the list that are the same.
# For example: remove_duplicates([1,1,2,2]) 
# should return [1,2].
# Don't remove every occurrence, since you need to keep a
# single occurrence of a number.
# The order in which you present your output does not
# matter. So returning [1,2,3] is the same as
# returning [3,1,2].
# Do not modify the list you take as input! Instead,
# return a new list.

#method 1, version 2: iterate over the list and add what's not already in output
def remove_duplicates(listy_list = []):
    output = []
    for i in listy_list:
        if i not in output:
            output.append( i )
    return output

input1 = [1,2,3,3,4,4,5,6,1,2,6,8,9,10,10,1,2,3,4,5,6,7,8]
print("input:", input1)
print("\noutput:",remove_duplicates(input1))

#method 2: create a set from input and return
#this is the most efficient way to solve the problem
#because a set by definition has no duplicate items
def remmy_dupe(listy_q_listerson = []):
    return list(set(listy_q_listerson))

print("\noutput2:",remmy_dupe(input1))
