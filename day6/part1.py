import numpy as np

# lecture fic et recuperation data
initialState = []
with open('input/data.txt') as f:
    initialState = [int(i) for i in f.readline().strip().split(',')] # comprehensive list

# set nombre de jours
nbDays = 80

# state
state = np.array(initialState)

for i in range(1, nbDays+1):
    state -= 1 # wtf
    for j in range(0, len(state)) :
        if state[j] == -1:
            state[j] = 6
            state = np.append(state, 8)
    print(f"After {i} day: {state}")

print(len(state))