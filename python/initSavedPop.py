import numpy as np
from hillClimb import miteBasicHillClimb
from miteManagement import uniformRandPop
from scoring import fromFilePopScoring
from joblib import Parallel, delayed
import multiprocessing
import os


def processMite(args_tup):
    mite = args_tup[0]
    i = args_tup[1]
    print "Starting mite number " + str(i + 1) + '\n'
    return miteBasicHillClimb(mite, scoreFunc=fromFilePopScoring)

def main():
    popSize = 30

    if 'savedPop' + str(popSize) + '.npy' not in os.listdir('./'):
        print "Initializing to random...\n"
        pop = np.vstack((np.ones((1,50)), np.ones((1,50)) * 3, uniformRandPop(popSize-2)))

        print "Starting hill climbing for each mite...\n"
        for i in range(popSize):
            pop[i, :] = miteBasicHillClimb(pop[i, :])
            print "Finished mite number " + str(i+1) + " of " + str(popSize)

        np.save('savedPop' + str(popSize) + '.npy', pop)
    else:
        pop = np.load('savedPop' + str(popSize) + '.npy')
        popSize = pop.shape[0]

    args = []

    for i in range(popSize):
        args.append((pop[i, :], i))

    num_cores = multiprocessing.cpu_count()-2
    results = Parallel(n_jobs=num_cores, verbose=1,
                       backend="multiprocessing")(map(delayed(processMite), args))

    pop = np.concatenate(tuple(results), axis=0)

    np.save('savedPop' + str(popSize) + '.npy', pop)

    print "Saved the population!"


if __name__ == "__main__":
    main()
