
def printArray(array, start, stop):
    print len(array)
    if stop >= len(array):
        stop = len(array)
    print array[start:stop]

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