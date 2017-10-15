import numpy as np
from hillClimb import miteBasicHillClimb
from miteManagement import uniformRandPop

popSize = 100

print "Initializing to random...\n"
pop = uniformRandPop(popSize)

print "Starting hill climbing for each mite...\n"
for i in range(popSize):
    pop[i, :] = miteBasicHillClimb(pop[i, :])
    print "Finished mite number " + str(i) + " of " + str(popSize)

np.save(pop, 'savedPop.npy')