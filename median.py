# Write a function called median that takes a list as an
# input and returns the median value of the list.
# For example: median([1,1,2]) should return 1.
# The list can be of any size and the numbers are not
# guaranteed to be in any particular order.
# If the list contains an even number of elements, your
# function should return the average of the middle two.

import math
def median(listylist = []):
    #first sort the list
    listylist.sort()
    print("Your listy list has been sortificationalized:", listylist)
    #second get the length of the list
    lengthylength = len(listylist)
    print("Length o' th' list:", lengthylength)
    #third get the middle value
    #if the length is odd then the middle is floor(half) +  1
    #if the length is even then the middle is (half + (half+1)) / 2
    if lengthylength % 2 == 0: #even
        half = [((lengthylength / 2) - 1), (lengthylength / 2)]
        median = (listylist[int(half[0])] + listylist[int(half[1])]) / 2
    else: #odd
        half = int(math.floor(lengthylength / 2))
        median = listylist[half]    
    return median

#inputlist = [9,8,5,6,7,4,3,8,5,4,5,10,11,29,89,4,44,35,678,54,3,5,7,8,9,1,2,22,23,24,25] #median 8
#inputlist = [3,2,14,7,9,2,5,6,12] #median 6
#inputlist = [1,10,11,12] #median 10.5
#inputlist = [3,3.7,3.95,4.1001,5] #median 3.95
#inputlist = [4,5,5,4] #median 4.5
#inputlist = [1,34,1,6,8,0]
inputlist = [2,103]
print('Median:', median(inputlist))
