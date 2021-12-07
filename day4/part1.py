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

# on marque les numeros en fonction du tirage
for drawn in draw: 
    for grid in grids:
        for line in grid:
            for i, num in enumerate(line):
                if drawn == num:
                    line[i] = -1
        if checkGrid(grid): # si une ligne ou colonne est marquée complète, on sommme tout sauf les -1
            count = 0
            flattenGrid = grid.flatten()
            for num in flattenGrid:
                if num != -1:
                    count += num
            print(count*drawn) # on print la solution
            f.close()
            exit()

f.close()