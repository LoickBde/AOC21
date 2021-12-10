import numpy as np

# lecture fic et recuperation data
rawNotes = []
with open('input/data.txt') as f:
    rawNotes = f.readlines()

# recuperation des digits outputs
outputs = []
for row in rawNotes:
    outputs.append(row.strip().split(' | ')[1].split(' '))

# on compte l apparition des digits 1, 4, 7, 8
# 1 : 2 seg
# 4 : 4 seg
# 7 : 3 seg
# 8 : 7 seg
outputs = np.array(outputs)
outputs = outputs.flatten()
nbDigits = 0
for digit in outputs:
    if len(digit) in (2, 3, 4, 7): 
        nbDigits += 1 

print(nbDigits)