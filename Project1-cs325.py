
import io
import time
import generateArray

#Output filename setup
location = ""
filename = "MSS_Results.txt"

# Clear and/or initialize the output file
io.writeFile(location, filename, "CS325 Project 1", "w")

  #todo  make this return the array, and the max...perhaps then it's easier to use the print functions separately?
# ARRAY TWO
#@Params
#Array of numbers
#max the max indices in the array
#min the minimum indices in the array

def algo1_mm(array):
    biggest = -220000     #value to store the largest sum
    max_i = 0         #minimum and maximum indices
    min_i = 0

    n = len(array)

    if n < 2:
        return 0

    #cycle though the array
    for i in range(0, n-1):
        for j in range (i+1, n):
            sum = 0;
            for k in range(i, j+1):
                sum += array[k]

            if sum > biggest:
                min_i = i   # reset the indicators
                max_i = j
                biggest = sum

    #todo write to file
    io.writeFile(location, filename, "Algo1 Max Subarray:" + str(array[min_i:(max_i+1)]) + ' Sum: ' + str(biggest))

def algo2_mm(array):
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

    io.writeFile(location, filename, "Algo2 Max Subarray: " + str(array[min_i:(max_i+1)]) + ' Sum: ' + str(biggest))

#Description: This program uses divide and conquer algorithm to
#take as an input an array and output the subbarray with maximum
#sum along with the sum.
#@params an array, the begin, and the length of the array -1
def maxSubarray3 (Array, low, high):
#base case (if only one element)
    if (high == low):
        return (low, high, Array[low])

    else:
        mid = (low+high)/2
        leftLow, leftHigh, leftSum = maxSubarray3 (Array, low, mid)
        rightLow, rightHigh, rightSum = maxSubarray3 (Array, mid+1, high)
        crossLow, crossHigh, crossSum = maxCrossingSubarray(Array, low, mid, high)

    if (leftSum>=rightSum and leftSum>=crossSum):
        low = leftLow
        high = leftHigh+1
        sum = leftSum
        return (leftLow, leftHigh, leftSum)

    elif (rightSum >= leftSum and rightSum>= crossSum):
        low = rightLow
        high = rightHigh+1
        sum = rightSum
        return (rightLow, rightHigh, rightSum)
    else:
        low = crossLow
        high = crossHigh+1
        sum = crossSum
        return (crossLow, crossHigh, crossSum)

    io.writeFile(location, filename, "Algo3 Max Subarray: " + str(Array[low:(high+1)]) + ' Sum: ' + str(sum))

def maxCrossingSubarray(Array, low, mid, high):
   leftSum=-2000000000
   sum=0
   for i in range (mid, low-1, -1):
    sum = sum+Array[i]
    if (sum>leftSum):
       leftSum=sum
       maxLeft=i
   rightSum=-2000000000
   sum=0
   for j in range (mid+1, high+1):
    sum = sum+Array[j]
    if (sum>rightSum):
       rightSum=sum
       maxRight=j
   return (maxLeft, maxRight, leftSum+rightSum)

def algo4_mm(array):
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

    io.writeFile(location, filename, "Algo 3 Max Subarray:" + str(array[low:(high+1)]) + ' Sum: ' + str(maxSum))
    return [low, high, maxSum]

## using the read to array now located in printArray to get a file and push all the arrays through the functions
## printArray gets the function read_to_array, which generates arrays from arrays in the file
## loops over them and fires them into array_2
for fArrays in io.read_to_array("","MSS_Problems.txt"):
    algo1_mm(fArrays)

for fArrays in io.read_to_array("","MSS_Problems.txt"):
    algo2_mm(fArrays)

for fArrays in io.read_to_array("","MSS_Problems.txt"):
    maxSubarray3(fArrays,0,len(fArrays)-1)

for fArrays in io.read_to_array("","MSS_Problems.txt"):
    algo4_mm(fArrays)


#
# #This is for the experimental testing:
# n = 10
# sizeN = 10000
# totalTime = 0
# for i in range(n):
#         A = generateArray.generateArray(sizeN)
#         start = time.time()
#         algo4_mm(A)
#         stop = time.time()
#         totalTime += stop - start
# print n,"in",sizeN,": ", totalTime/n
