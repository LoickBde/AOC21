binaryNumbers = []

# recuperation des data
with open('input/data.txt') as f:
   for line in f:
        binaryNumbers.append(line.strip())
        if 'str' in line:
            break

gamma = ""
epsilon = ""

# on boucle sur l'ensemble des colonnes, de haut en bas
for i in range(0, len(binaryNumbers[0])):
    count_zero = 0 # compteur de 0
    count_one = 0 # compteur de 1

    for j in range(0, len(binaryNumbers)):
        if int(binaryNumbers[j][i]) == 0:
            count_zero += 1
        elif int(binaryNumbers[j][i]) == 1:
            count_one +=1
    if(count_zero > count_one):
        gamma += '0'
        epsilon += '1'
    elif(count_one > count_zero):
        gamma += '1'
        epsilon += '0'

gamma = int(gamma, 2) # conversion bin to int
epsilon = int(epsilon, 2) # conversion bin to int

print(gamma*epsilon)
