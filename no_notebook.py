from traffic_import import *    # all of the basic 'import' statements (math, etc.)
from simulation_step import one_step, multi_step  # our own function that implements one step of the
                                        # simulation

# some constants
num_cells = 1000
num_timesteps = 500

v_max = 5

c = 0.2
p = 0.1

# initialize the arrays we are going to use
autobahn = zeros(num_cells)
velocity = zeros(num_cells)

autobahn_matrix = zeros([num_cells, num_timesteps])

# initialize where the cars are at time = 0
for i in range(num_cells):
    if random.random() < c:
        autobahn[i] = 1

# count and print the total number of cars in the simulation at time = 0
print('number of cars: ', int(sum(autobahn)))

# Simulate a number of steps before starting the actual simulation.
# This should get us from a random initial situation to an evolved situation
# that is a typical situation at the limit as time goes to infinity.
[autobahn, velocity] = multi_step(autobahn, velocity, v_max, p, 5000)
print('multi_step done...')
print('the simulation starts now')

# Simulate one timestep at a time. After each step, save the distribution of
# cars to 'autobahn_matrix' so we can plot its development over time afterwards.
for k in range(num_timesteps):
    [autobahn, velocity] = one_step(autobahn, velocity, v_max, p)
    # save the situation
    autobahn_matrix[:, k] = autobahn

# Plot the distribution of cars over a number of timesteps
plt.matshow(autobahn_matrix.transpose())
plt.set_cmap('binary')
plt.title('A Traffic Simulation')
plt.ylabel('Time Steps')
plt.xlabel('Grid Cells')
boxText = '$v_{max}$ = %i\n$c$ = %.2f\n$p$ = %.2f' % (v_max, c, p)
plt.text(800, 800, boxText, bbox=dict(facecolor='white', alpha=0.8))
plt.show()
