
import printArray
import time
import generateArray

  #todo  make this return the array, and the max...perhaps then it's easier to use the print functions separately?
# ARRAY TWO
#@Params
#Array of numbers
#max the max indicie in the array
#min the minimum indicy in the array

def array1_mm(array):
    biggest = 0     #value to store the largest sum
    max_i = 0         #minimum and maximum indices
    min_i = 0

    n = len(array)

    if n < 2:
        return 0

    #cycle though the array
    for i in range(0, n-1):
        for j in range (i+1, n):
            sum = 0;
            for k in range(i, j):
                sum += array[k]

            if sum > biggest:
                min_i = i   # reset the indicators
                max_i = j
                biggest = sum

    print array
    printArray.printArray(array, min_i, max_i)
    print biggest

def array2_mm(array):
    biggest = 0     #value to store the largest sum
    max_i = 0         #minimum and maximum indices
    min_i = 0

    n = len(array)

    if n < 2:
        return 0

    #cycle though the array
    for i in range(0, n-1):
        min_v = array[i]   # this is the start of the array

        for j in range(i+1, n):
            max_v = array[j] # this is the end

        ## swap our min and max indices if it's larger additively in value
            min_v += max_v  # add the max onto the min
            if min_v  > biggest:
                min_i = i   # reset the indicators
                max_i = j
                biggest =  min_v

    #todo get rid of spaces
    print array
    printArray.printArray(array, min_i, max_i)
    print biggest


def array4_mm(array):
    n = len(array)
    maxSum = -2999999999         #value to store the largest sum
    endingHereSum = -2999999999

    if n < 2:
        return 0

    for i in range(0, n):
        endingHereHigh = i
        if endingHereSum > 0:
            endingHereSum = endingHereSum + array[i]
        else:
            endingHereLow = i
            endingHereSum = array[i]

        if endingHereSum > maxSum:
            maxSum = endingHereSum
            low = endingHereLow
            high = endingHereHigh

    return [low, high, maxSum]

## using the read to array now located in printArray to get a file and push all the arrays through the functions
## printArray gets the function read_to_array, which generates arrays from arrays in the file
## loops over them and fires them into array_2
for fArrays in printArray.read_to_array("","testproblems1.txt"):
    #array1_mm(fArrays)
    #array2_mm(fArrays)

    #alg 3 goes here

    #low, high, maxSum = array4_mm(fArrays)
    #printArray.printArray(fArrays, low, high + 1)
    #print maxSum
    print ''


#This is for the experimental testing:
n = 10
sizeN = 10000
totalTime = 0
for i in range(n):
        A = generateArray.generateArray(sizeN)
        start = time.time()
        array4_mm(A)
        stop = time.time()
        totalTime += stop - start
print n,"in",sizeN,": ", totalTime/n