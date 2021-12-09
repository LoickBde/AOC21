import numpy as np

# lecture fic et recuperation data
crabsPos = []
with open('input/data.txt') as f:
    crabsPos = [int(i) for i in f.readline().strip().split(',')] 

# utilsiation de la mediane de la liste car on veut le moins de mouvement possible autour d une valeur
# or la médiane par def c'est 50% des val sup a la mediane et 50% des valeurs inf a la mediane
# contrainement a la moyenne
fuelUsed = 0
for pos in crabsPos:
    fuelUsed += abs(pos - int(np.median(crabsPos)))


print(fuelUsed)