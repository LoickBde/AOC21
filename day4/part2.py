import numpy as np


# fonction check, true si une ligne ou colonne remplie
def checkGrid(grid):
    gridToCheck = grid
    
    # check des lignes
    if checkLine(gridToCheck):
        return True

    # check les colonnes
    gridToCheck = np.transpose(gridToCheck)
    if checkLine(gridToCheck):
        return True

    return False

# fonction check pour les lignes
def checkLine(gridToCheck):
    for line in gridToCheck:
            if all([num == -1 for num in line]):
                return True
    return False


# recuperation des data
f = open("input/data.txt","r") 

# recuperation du tirage
draw = [int(i) for i in f.readline().strip().split(',')]

# recuperation des grilles, une grille par entrée
gridsData = f.read().strip().split('\n\n')

# formation des grilles
grids = []
for gridData in gridsData: # pour chaque grille
    grid = []
    for lineData in gridData.replace('  ', ' ').splitlines(): # pour chaque ligne
        line = []
        for num in lineData.strip().split(' '): # pour chaque num
           line.append(int(num))
        grid.append(line)
    grids.append(grid)

grids = np.array(grids)

for drawn in draw:
    gridIndex = 0
    while gridIndex < len(grids):
        grid = grids[gridIndex]
        for line in grid:
            for i, num in enumerate(line):
                if drawn == num:
                    line[i] = -1
        if checkGrid(grid) : # si une grille est valide, on la supprime 
            if len(grids) > 1 : # si elle reste plus d'une grille
                grids = np.delete(grids, gridIndex, 0)
            else : #sinon on calcul
                count = 0
                flattenGrid = grids[0].flatten()
                for num in flattenGrid:
                    if num != -1:
                        count += num
                print(count*drawn) # on print la solution
                f.close()
                exit()
        else : # on increment l index uniquement aucune grille n'a ete supprimee
            gridIndex += 1 

f.close()