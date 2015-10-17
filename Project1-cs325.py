__author__ = 'Robert Jackson, michael Hoppes'
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
    #todo get rid of spaces
    print '[',
    for i in range(min_i, max_i + 1):
        print arry[i],
        if i != max_i:
            print ',' ,
    print ']'
    print biggest

#read a file
# convert each line to an array or integers
# returns an array of arrays of integers
#@params loc = location, name = file name

def read_to_array(loc, name):
    result = []
    f = open(loc+name, 'r')
    for line in f:
        # get rid of junk
        # for some reason makes me use equal...not sure that's right but works
        line=  line.replace('[', '')
        line = line.replace(']', '')
        line = line.replace('\n', '')
        line = line.split(',')

        #convert each element to an integer
        newline = []
        for i in line:
            v = int(i)
            newline.append(v)
        result.append(newline)

    return result



#array2_mm(some_array)
print readtoarray("", "testproblems1.txt")
#print sum(some_array, 0)