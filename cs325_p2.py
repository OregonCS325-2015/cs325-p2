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
import inout
import time
import gc


# Testing array
# using these should return C=[1,1,1,1] and M = 4 ie c[3] = 4
A = 40
V= [1,3,4,10,25, 50]

#@params A = target value to return min coins
#returns the minimum number, and the array of lowest coins
#verified on test Array
def changeSlow (A, V):
    s=len(V)
    c=[0]*s

    for i in range (0,s):
        if (V[i]==A):
            c[i]=1
            return (c,1)

    minResult = A

    for i in range (1, A):
        c1,result1 = changeSlow(i, V)
        c2,result2 = changeSlow(A-i,V)
        result=result1+result2
        if (result<minResult):
            minResult=result
            for j in range (s):
                c[j]=c1[j]+c2[j]

    return c,minResult


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
def changedp(A,V):

    r=[]
    for i in range (0,A+1):
         r.append (0)

    #start a first coin
    for j in range (0,len(V)):

        for i in range (V[j], A+1):
            if V[j] >= i:   #if our coin is less that the A
                r[i] = min ( r[i-1]+1, r[V[j]-i]+1 ) # add the min of the previous save+1 (start0) or the save of current coin-current value +1

            else: # our A is greater than the coin
                r[i] = r[i-V[j]]+1  #subtract the coin from the A to get the save index to use add one
    return r, r[A]


print 'this is changeDP:', changedp(A,V)


print 'this is changeSlow:', changeSlow(A, V)
print 'this is changeGreedy:', changegreedy(A,V)
