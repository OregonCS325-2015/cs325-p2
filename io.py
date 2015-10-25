from itertools import islice # used in file reading
import sys, getopt

# Prints array from start to stop
def printArray(array, start, stop):
    if stop >= len(array):
        stop = len(array)
    print array[start:stop]

# read a file
# convert each line to an array or integers
# returns an array of arrays of integers
# @params  name = file name
# returns an array of arrays, and a value
def read_file( name):
    denom = [] #the denominations from the file
    vals = [] # the values
    f = open( name, 'r')

    #iterate through the file
    count  =0
    for line in f:
        count +=1
        # get rid of junk
        # first lines are suppsed to be arrays of numbers
        if count % 2 != 0:
            line = line.replace('[', '')
            line = line.replace(']', '')
            line = line.replace('\n', '')
            line = line.replace(' ', '')
            line = line.split(',')

            # convert each element to an integer
            #put it in an array
            newline = []
            for i in line:
                v = int(i)
                newline.append(v)

            denom.append(newline)

        else:# every other line is a value, remove junk

            line = line.replace('\n', '')
            line = line.replace(' ', '')
            vals.append(line) #put every other line into the values

    #if there is bad data in the file
    if len(vals) != len(denom):
        print "failed to read file correctly, uneven number of values to arrays"
        return 0, 0

    return denom, vals

# Output to a file, the contents specified, defaulting to appending
def writeFile(loc, name, contents, method='a'):
    try:
        f = open(loc + name, method)
    except:
        print "The file could not be opened: ", sys.exc_info()[0]

    f.write(contents)
    f.write('\n')
    f.close()

# adapted from http://www.tutorialspoint.com/python/python_command_line_arguments.htm
def cmd_line_io(argv):
    inputfile = ''
    outputfile = ''
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
    for opt, arg in opts:
       #help
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()

         #input file
      elif opt in ("-i", "--ifile"):
         inputfile = arg
         read_file(inputfile)

         #outputfile
      elif opt in ("-o", "--ofile"):
         outputfile = arg
          #todo we need a function here to just establish the file I think: and based on the inputfiles name so [inputFile]Change.txt
    print 'Input file is "', inputfile
    print 'Output file is "', outputfile

## vip  this function only fires if io.py is run directly but not when imported!!!
# used to test the reading of a file from cmd line
if __name__ == "__main__":
   cmd_line_io(sys.argv[1:])
