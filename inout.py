from itertools import islice # used in file reading
import sys, getopt


#some globals from the cmd line
inputfile = ''
outputfile = ''
algo = ''


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
            vals.append(int(line)) #put every other line into the values

    #if there is bad data in the file
    if len(vals) != len(denom):
        print "failed to read file correctly, uneven number of values to arrays"
        return 0, 0

    return denom, vals

# Output to a file, the contents specified, defaulting to appending
def writeFile( name, contents, method='a'):
    try:
        f = open(name, method)
    except:
        print "The file could not be opened: ", sys.exc_info()[0]

    f.write(str(contents[0])+'\n' )
    f.write(str(contents[1]))
    f.write('\n')
    f.close()

# adapted from http://www.tutorialspoint.com/python/python_command_line_arguments.htm
def cmd_line_io(argv):
    inputfile = ''
    outputfile = ''
    algo = ''
    try:
      opts, args = getopt.getopt(argv,"hi:a:",["ifile=", "algorithm="])
    except getopt.GetoptError:
      print 'cs325_p2.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
    for opt, arg in opts:
       #help
      if opt == '-h':
         print 'cs325_p2.py -i <inputfile> '
         sys.exit()

         #input file
      elif opt in ("-i", "--ifile"):
         inputfile = arg
         temp = inputfile.replace('.txt', '')
         outputfile = temp +'Change.txt'

        #Algorithm
      elif opt in ("-a","--algorithm"):
         algo = arg

    return inputfile, algo, outputfile

    print 'Input file is "', inputfile
    print 'Output file is "', outputfile
    print 'Algorithm is "', algo

## vip  this function only fires if inout.py is run directly but not when imported!!!
# used to test the reading of a file from cmd line
if __name__ == "__main__":
   cmd_line_io(sys.argv[1:])
