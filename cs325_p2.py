# CS 325 PROJECT 2
# Martha Gebremariam
# Michael Hoppes
# Robert Jackson
# Group Number - 11
# PROJECT 2
# CS 325 - Fall 2015

# DESCRIPTION
# todo enter description

import sys, getopt
import math
import inout
import time
import gc


# Testing array
# using these should return C=[1,1,1,1] and M = 4 ie c[3] = 4
# A = 12
# V = [1,2,3,4,8,19]


# @params A = target value to return min coins
# returns the minimum number, and the array of lowest coins
# verified on test Array
def changeSlow(A, V):
    s = len(V)
    c = [0] * s

    for i in range(0, s):
        if V[i] == A:
            c[i] = 1
            return (c, 1)

    minResult = A

    for i in range(1, A):
        c1, result1 = changeSlow(i, V)
        c2, result2 = changeSlow(A - i, V)
        result = result1 + result2
        if result < minResult:
            minResult = result
            for j in range(s):
                c[j] = c1[j] + c2[j]

    return c, minResult


def changegreedy(A, V):
    change = A
    coinage = V
    coins = []
    while change > 0:
        coins.insert(0, int(change / max(coinage)))
        change = change % max(coinage)
        coinage.pop()

    # if we still have coinage, then they are zero
    while len(coinage) > 0:
        coins.insert(0, 0)
        coinage.pop()

    return coins, sum(coins)


#
# #C,m = changegreedy(A, V)
#
# #  TODO Why does this print only [1] for V?
# #print 'changegreedy for A:',A,', V:',V,': C=',C,' m =',m
#
# #A=29
# #V=[1,3,7,12]
# #C,m = changegreedy(A, V)
# #print 'changegreedy for A:',A,', V:',V,': C=',C,' m =',m
# #A=31
# #V=[1,3,7,12]
# #C,m = changegreedy(A, V)
# #print 'changegreedy for A:',A,', V:',V,': C=',C,' m =',m


# #@params a integer, v an array of increasing integers
# #DP Algorithm for the coin problem
# # titled changedp as per project instructions
# # returns 4 for testing array- verified
def changedp(A, V):
    a = [[0] * (A + 1) for x in xrange(len(V))]

    for j in range(1, A + 1):
        a[0][j] = j

    for i in range(1, len(V)):
        for j in range(1, A + 1):
            if (j >= V[i]):
                a[i][j] = min(a[i - 1][j], 1 + a[i][j - V[i]])
            else:
                a[i][j] = a[i - 1][j]


    minChange = a[len(V)-1][A]

    # the following code to trace back and find
    # values of c[i]
    m = [-1] * len(V)
    x = len(V) - 1
    m[x] = 0
    y = A
    # print a[x][y]
    value = 1
    while (value > 0):
        if (A < V[x]):
            x = x - 1
            m[x] = m[x] + 1
        else:
            if ((a[x - 1][A]) < (a[x][A - V[x]] + 1)):
                x = x - 1
                m[x] = m[x] + 1
            else:
                A = A - V[x]
                m[x] = m[x] + 1
                value = a[x][A]
    for i in range(len(m)):
        if (m[i] == -1):
            m[i] = 0

    return (m, minChange)

def changedp_Alt(A, V):

    r=[100000]*A
    C= [0]*len(V)
    for i in range (0,A):
        r.append (0)

    #start a first coin
    for j in range (0,len(V)):

        for i in range (V[j], A):
            if V[j] == i:
                r[i-1]= 1

            if V[j] <= i:

                r[i] = r[i-V[j]]+1  #subtract
            else:
                r[i] = min ( r[i-1]+1, r[i-V[j]]+1 ) # add the min of the previous save+1 (start0) or the save of current coin-current value +1

#now to fill C:

    bucket = A
    for k in range (len(V)-1, -1, -1): # start at highest position decrement to 0

        test = bucket/V[k]
        if (test >= 1):  # this means we used that value at postion v[k] otherwise move down
            test = test*V[k] #it just so happens this corresponds to a certain position in r
            #bucket = bucket-test #remove this sum from the bucket
            used = r[test-1] # add the value at the position to our c
            if used>0:
                bucket = bucket-test

            C[k] = used

    return r[A-1], C

if __name__ == "__main__":
    (ifile, algo, ofile) = inout.cmd_line_io(sys.argv[1:])

    if algo  == 'changedp':
        (denom, val) = inout.read_file(ifile)

        for i in range (0, len(denom)):
            inout.writeFile(ofile, changedp(val[i], denom[i]))

    elif algo  == 'changeslow':
        (denom, val) = inout.read_file(ifile)

        for i in range (0, len(denom)):
            inout.writeFile(ofile, changeSlow(val[i], denom[i]) )
    elif algo  == 'changegreedy':
        (denom, val) = inout.read_file(ifile)

        for i in range (0, len(denom)):
            inout.writeFile(ofile, changegreedy(val[i], denom[i]) )

    else:
        print 'Incorrect parameters provided try cs325_py -h'

# print 'this is changeDP:', changedp(A, V)
# print 'this is changeDP_1:', changedp_1(A, V)
# print 'this is changeSlow:', changeSlow(A, V)
# print 'this is changeGreedy:', changegreedy(A, V)
