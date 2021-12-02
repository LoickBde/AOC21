measurements = []

# lecture fic et recuperation data
with open('input/data.txt') as f:
    measurements =  f.readlines()

count = 0
prev = int(measurements[0])

for i in range(1, len(measurements)):
    current = int(measurements[i])
    if current > prev:
        count += 1    
    prev = current

print(count) 