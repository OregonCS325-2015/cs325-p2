import random

def generateArray(n):
    array = []
    for x in range(n):
      array.append(random.randint(-10000,10000))
    return array

