# CS 325 PROJECT 2
# Martha Gebremariam
# Michael Hoppes
# Robert Jackson
# Group Number - 11
# PROJECT 2
# CS 325 - Fall 2015

# DESCRIPTION
# todo enter description


import math
import inout
import time
import gc
import sys

sys.setrecursionlimit(10000)


# Testing array
# using these should return C=[1,1,1,1] and M = 4 ie c[3] = 4
A = 6
V = [1, 3, 4]


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


# #@params a integer, v an array of increasing integers
# #DP Algorithm for the coin problem
# # titled changedp as per project instructions
# # returns 4 for testing array- verified
def changedp_1(A, V):
    a = [[0] * (A + 1) for x in xrange(len(V))]

    for j in range(1, A + 1):
        a[0][j] = j

    for i in range(1, len(V)):
        for j in range(1, A + 1):
            if (j >= V[i]):
                a[i][j] = min(a[i - 1][j], 1 + a[i][j - V[i]])
            else:
                a[i][j] = a[i - 1][j]

    minChange = a

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


def changedp(A, V):
    r = []
    C = [0] * len(V)
    for i in range(0, A):
        r.append(0)

    # start a first coin
    for j in range(0, len(V)):

        for i in range(V[j] - 1, A):
            if V[j] == i:
                r[i - 1] = 1

            if V[j] <= i:

                r[i] = r[i - V[j]] + 1  # subtract
            else:
                r[i] = min(r[i - 1] + 1, r[i - V[
                    j]] + 1)  # add the min of the previous save+1 (start0) or the save of current coin-current value +1

                # now to fill C:

    bucket = A
    for k in range(len(V) - 1, -1, -1):  # start at highest position decrement to 0

        test = bucket / V[k]
        if (test >= 1):  # this means we used that value at postion v[k] otherwise move down
            test = test * V[k]  # it just so happens this corresponds to a certain position in r
            bucket = bucket - test  # remove this sum from the bucket
            used = r[test - 1]  # add the value at the position to our c

            C[k] = used

    return r[A - 1], C






    # #start a first coin
    # for i in range (0,len(V)):
    #
    #     for j in range (V[i], A):
    #         # j is the same size a the coin either append, or update
    #         if (V[i]==j):
    #              if len(r) <= 1:
    #                  r.append(1)
    #              else:
    #                  r[len(r)-1]= 1




    # if (V[i]==j):
    #     if len(r) <= 1:
    #         r.append(1)
    #     else:
    #         r[len(r)-1]= 1
    #
    # elif(j < V[i]):
    #     r[len(r)-1] = min ( r[i-1]+1, r[V[i]-j]+1 )
    #
    # else:   #if our coin is
    #     if len(r) <= 1:
    #         r.append ( r[V[i]-1]+1) # add the min of the previous save+1 (start0) or the save of current coin-current value +1
    #
    #     else:
    #         r[len(r)-1]= (r[V[i]-1]+1)

    # else: # our A is greater than the coin
    #     r[i] = r[i-V[i]]+1  #subtract the coin from the A to get the save index to use add one



    # return r

# print 'this is changeDP:', changedp(A, V)
# print 'this is changeDP_1:', changedp(A, V)
# print 'this is changeSlow:', changeSlow(A, V)
# print 'this is changeGreedy:', changegreedy(A, V)
