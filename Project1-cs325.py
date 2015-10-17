__author__ = 'Robert Jackson'
import functools

#@Params
#Array of numbers
#max the max indicie in the array
#min the minimum indicy in the array

some_array = [-10,21,44,23,-16,213,4,9,-10,1,16,3]

def readtoarray(loc, name):

    file = open(loc+name, 'r')
    result = ( file.readline())
    return result



def iter_mm(arry):
    biggest = 0     #value to store the largest sum
    max_i=0         #minimum and maximum indices
    min_i =0

    if len(arry) == 1:
        return 0

    if len(arry) >= 2:

    #cycle though the array
        for i in range (0, len(arry)-1):
            min_v = arry[i]   # this is the start of the array

            for n in range (i+1, len(arry)):
                max_v = arry[n] # this is the end

            ## swap our min and max indices if it's larger additively in value
                min_v += max_v  # add the max onto the min
                if min_v  > biggest:
                    min_i = i   # reset the indicators
                    max_i = n
                    biggest =  min_v

    print '[',
    for i in range(min_i, max_i + 1):
        print arry[i],
        if i != max_i:
            print ',' "",
    print ']'
    print biggest




iter_mm(some_array)

#print sum(some_array, 0)