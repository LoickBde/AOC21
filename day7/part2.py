import numpy as np
from numpy.lib.function_base import median

# lecture fic et recuperation data
crabsPos = []
with open('input/data.txt') as f:
    crabsPos = [int(i) for i in f.readline().strip().split(',')] 

# somme des entiers S = 1/2*n(n+1)
minimizedFuel = -1;
for targetPos in range(0, np.max(crabsPos)+1):
    fuelUsed = 0
    for pos in crabsPos:
        nbMove = abs(pos - targetPos)
        fuelUsed += int((1/2)*nbMove*(nbMove+1))
    if minimizedFuel == -1 or fuelUsed < minimizedFuel:
        minimizedFuel = fuelUsed

print(int(minimizedFuel))