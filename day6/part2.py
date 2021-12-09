import numpy as np

# lecture fic et recuperation data
initialState = []
with open('input/data.txt') as f:
    initialState = [int(i) for i in f.readline().strip().split(',')] # comprehensive list

# set nombre de jours
nbDays = 256

# state
state = np.array(np.zeros(9, dtype=np.longlong))

# on rempli le tableau de base
for num in initialState:
    state[num] += 1

for i in range(1, nbDays+1):
    nbDeadFishes = state[0]
    for i in range(1, len(state)):
        state[i-1] = state[i] 
    state[6] += nbDeadFishes
    state[8] = nbDeadFishes

print(np.sum(state, dtype=np.longlong))