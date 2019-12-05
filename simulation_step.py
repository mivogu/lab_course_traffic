# simulation_step.py
# The function defined here takes the current situation
#   autobahn_old = array of 0 and 1 indicating whether there is a car present in
#       a certain grid cell,
#   velocity_old = array of numbers in [0, v_max] that save the velocity of the
#       car in a specific grid cell
# and returns the situation after one time interval
#   autobahn_new, velocity_new

from numpy import zeros
from random import random as rand

# added a new line for git testing purposes

def one_step(autobahn_old, velocity_old, v_max, p):
    num_cells = len(autobahn_old)
    autobahn_new = zeros(num_cells)
    velocity_new = zeros(num_cells)
    
    # first step: acceleration
    for i in range(num_cells):
        if autobahn_old[i] == 1:
            velocity_old[i] = min(velocity_old[i] + 1, v_max)
    
    # second step: deceleration
    for i in range(num_cells):
        if autobahn_old[i] == 1:
            dist = 0
            while dist <= v_max + 1:
                if autobahn_old[(i + dist + 1) % num_cells] == 1:
                    break
                dist += 1
            if dist <= v_max:
                velocity_old[i] = max(dist - 1, 0)
    
    # third step: driving slowly
    for i in range(num_cells):
        if autobahn_old[i] == 1:
            if rand() < p:
                velocity_old[i] = max(velocity_old[i] - 1, 0)
    
    # fourth step: actually driving
    autobahn_new = zeros(num_cells)
    velocity_new = zeros(num_cells)
    for i in range(num_cells):
        if autobahn_old[i] == 1:
            new_index = int(i + velocity_old[i])%num_cells
            autobahn_new[new_index] = 1
            velocity_new[new_index] = velocity_old[i]
    
    return [autobahn_new, velocity_new]

def multi_step(autobahn, velocity, v_max, p, num_steps):
    for i in range(num_steps):
        [autobahn, velocity] = one_step(autobahn, velocity, v_max, p)
    
    return [autobahn, velocity]
