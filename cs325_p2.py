# CS 325 PROJECT 2
# Martha Gebremariam
# Michael Hoppes
# Robert Jackson
# Group Number - 11
# PROJECT 2
# CS 325 - Fall 2015

#DESCRIPTION
#todo enter description

import math
import io
import time


# Testing array
# using these should return C=[1,1,1,1] and M = 4 ie c[3] = 4
A = 15
V= [1,2,4,8]

def changeslow(A, K):

    return


def changegreedy(A, V):
    change = A
    coinage = V
    coins = []
    while change > 0:
        coins.insert(0, int(math.floor(change / max(coinage))))
        change = change % max(coinage)
        coinage.pop()

    # if we still have coinage, then they are zero
    while len(coinage) > 0:
        coins.insert(0, 0)
        coinage.pop()

    return coins, sum(coins)

#C,m = changegreedy(A, V)
#A = 15
#V= [1,2,4,8]
#  TODO Why does this print only [1] for V?
#print 'changegreedy for A:',A,', V:',V,': C=',C,' m =',m

#A=29
#V=[1,3,7,12]
#C,m = changegreedy(A, V)
#print 'changegreedy for A:',A,', V:',V,': C=',C,' m =',m
#A=31
#V=[1,3,7,12]
#C,m = changegreedy(A, V)
#print 'changegreedy for A:',A,', V:',V,': C=',C,' m =',m

#@params a integer, v an array of increasing integers
#DP Algorithm for the coin problem
# titled changedp as per project instructions
# returns 4 for testing array- verified
#todo may need to instead return the entire array, not just r[somevalue]
def changedp(a,v):

    r=[]
    for i in range (0,a+1):
         r.append (0)

    #start a first coin
    for j in range (0,len(v)):

        for i in range (v[j], a+1):
            if v[j] >= i:   #if our coin is less that the A
                r[i] = min ( r[i-1]+1,r[v[j]-i]+1 ) # add the min of the previous save+1 (start0) or the save of current coin-current value +1

            else: # our A is greater than the coin
                r[i] = r[i-v[j]]+1  #subtract the coin from the A to get the save index to use add one
    return r[a]


#A = 15
#V= [1,2,4,8]
#print changedp(A,V)