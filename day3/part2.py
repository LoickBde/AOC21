binaryNumbers = []

# recuperation des data
with open('input/data.txt') as f:
   for line in f:
        binaryNumbers.append(line.strip())
        if 'str' in line:
            break

oxygen = 0
carbon = 0

i = 0
binaryNumbers_copy = binaryNumbers
# oxygen
# on boucle sur l'ensemble des colonnes, de haut en bas
while len(binaryNumbers) > 1 :
    count_zero = 0 # compteur de 0
    count_one = 0 # compteur de 1
    zerosNumbers = [] # contient les binaires avec le bit caractéristiques à 1
    onesNumbers = [] # contient les binaires avec le bit caractéristiques à 0


    for j in range(0, len(binaryNumbers)):
        if int(binaryNumbers[j][i]) == 0:
            zerosNumbers.append(binaryNumbers[j])
            count_zero += 1
        elif int(binaryNumbers[j][i]) == 1:
            onesNumbers.append(binaryNumbers[j])
            count_one +=1
    
    if(count_zero > count_one):
        binaryNumbers = zerosNumbers
    else : # gère le cas dans lequel on veut garder le dernier bit a 1 (et evite out of bound)
        binaryNumbers = onesNumbers
    
    i += 1

oxygen = int(binaryNumbers[0], 2)

i = 0
binaryNumbers = binaryNumbers_copy
# carbon
# on boucle sur l'ensemble des colonnes, de haut en bas
while len(binaryNumbers) > 1 :
    count_zero = 0 # compteur de 0
    count_one = 0 # compteur de 1
    zerosNumbers = [] # contient les binaires avec le bit caractéristiques à 1
    onesNumbers = [] # contient les binaires avec le bit caractéristiques à 0


    for j in range(0, len(binaryNumbers)):
        if int(binaryNumbers[j][i]) == 0:
            zerosNumbers.append(binaryNumbers[j])
            count_zero += 1
        elif int(binaryNumbers[j][i]) == 1:
            onesNumbers.append(binaryNumbers[j])
            count_one +=1
    
    if(count_one < count_zero):
        binaryNumbers = onesNumbers
    else : # gère le cas dans lequel on veut garder le dernier bit a 0 (et evite out of bound)
        binaryNumbers = zerosNumbers
    
    i += 1

carbon = int(binaryNumbers[0], 2)

print(oxygen*carbon)