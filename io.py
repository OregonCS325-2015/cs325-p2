# Prints array from start to stop
def printArray(array, start, stop):
    if stop >= len(array):
        stop = len(array)
    print array[start:stop]

# read a file
# convert each line to an array or integers
# returns an array of arrays of integers
# @params loc = location, name = file name

def read_to_array(loc, name):
    result = []
    f = open(loc + name, 'r')
    for line in f:
        # get rid of junk
        # for some reason makes me use equal...not sure that's right but works
        line = line.replace('[', '')
        line = line.replace(']', '')
        line = line.replace('\n', '')
        line = line.split(',')

        # convert each element to an integer
        newline = []
        for i in line:
            v = int(i)
            newline.append(v)
        result.append(newline)

    return result

# Output to a file, the contents specified, defaulting to appending
def writeFile(loc, name, contents, method='a'):
    try:
        f = open(loc + name, method)
    except:
        print "The file could not be opened: ", sys.exc_info()[0]

    f.write(contents)
    f.write('\n')
    f.close()

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