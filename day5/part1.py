import numpy as np

# recupere les dim max pour la carte des vents
def getDimMax(mArray) :
    xSize = 0 
    ySize = 0 
    dimMax = np.amax(mArray, 0)
    xSize = dimMax[0] if dimMax[0] > dimMax[2] else dimMax[2]
    ySize = dimMax[1] if dimMax[1] > dimMax[3] else dimMax[3]   
    return xSize+1, ySize+1

# lecture fic et recuperation data
rawData = []
with open('input/data.txt') as f:
    rawData = f.readlines()

# parse data
fullCoordinates = []
for line in rawData :
    parsedData = [int(i) for i in line.strip().replace(' -> ',',').split(',')]
    fullCoordinates.append(parsedData)

# garde que les lignes ou colonnes
coordinates = []
for line in fullCoordinates :
    if line[0] == line[2] or line[1] == line[3] : # x1 == x2 ou y1 == y2 pour ligne et colonne
        coordinates.append(line)
coordinates = np.array(coordinates)

# creation de la carte des vents
ventsMap = np.array(np.zeros(getDimMax(coordinates), dtype=int))

# on rempli la carte
for pos in coordinates :
    x1, y1, x2, y2 = tuple(pos) # on parse les coordonnées
    if x1 == x2 : # cas ligne, attention inversion avec lecture tableau et réalité
        if y1 < y2 :
            ventsMap[y1:y2+1, x1] +=1
        else : 
            ventsMap[y2:y1+1, x1] +=1
    elif y1 == y2: #cas colonne, attention inversion avec lecture tableau et réalité
        if x1 < x2 :
            ventsMap[y1, x1:x2+1] +=1
        else : 
            ventsMap[y1, x2:x1+1] +=1

print(np.count_nonzero(ventsMap >= 2))