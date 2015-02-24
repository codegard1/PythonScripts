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

def remove_duplicates(listy_list = []):
    output = []
    n = 0 #number of items added to list
    n2 = 1 #number of comparisons done
    
    for i in listy_list: #check if item is in output already
        print('output:', output)
        print(str(n)+'.'+str(n2))
        for m in output:
            print("\tcomparing", m, '&', i) #debug
            n2 += 1
            if m == i:
                print("\t", m, 'equals', i, 'so break')
                break
            else:
                print("\t", m, 'does not equal', i)
        else:
            output.append( i )
            n += 1
    return output

input1 = [1,2,3,3,4,4,5,6,1,2,6,8,9,10,10,1,2,3,4,5,6,7,8]
print('input: ', input1)
print(remove_duplicates(input1))
