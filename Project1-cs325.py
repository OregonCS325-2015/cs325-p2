__author__ = 'Robert Jackson'
import functools

# ARRAY TWO
#@Params
#Array of numbers
#max the max indicie in the array
#min the minimum indicy in the array

def array2_mm(arry):
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
            print ',' ,
    print ']'
    print biggest




array2_mm(some_array)

#print sum(some_array, 0)