measurements = []
triplets = []

# lecture fic et recuperation data
with open('input/data.txt') as f:
    measurements =  f.readlines()

# creation des sommes de 3 dans la limite du possible
triplet_sum = 0
for i in range(0, len(measurements)):
    if i+3 <= len(measurements):
        for j in range(0, 3):
            triplet_sum += int(measurements[i+j])
        triplets.append(triplet_sum)
        triplet_sum = 0

# reutilisation du code partie 1
count = 0
prev = int(triplets[0])

for i in range(1, len(triplets)):
    current = int(triplets[i])
    if current > prev:
        count += 1    
    prev = current

print(count) 