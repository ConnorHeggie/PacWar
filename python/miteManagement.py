import numpy as np

# This function with generate a uniformly random mite (takes a seed)
def uniformRandMite(seed = None):
    if seed != None:
        np.random.seed(seed)

    return np.random.randint(0, 3, size=(1,50), dtype=np.int8)


# This function will take in a population matrix (each row being a mite) and will return the mean hamming distance of the population
def findAvgHammingDist(population):
    raise NotImplementedError('Not yet implemented find average hamming distance')
    return -1

# This function will take in a mite and return a matrix containing all its 1 hamming distance neighbors
# The output will be a 150x50 numpy array where each row is a mite
def getNeighbors(mite):
    if mite.shape != (1,50):
        raise ValueError('Mite has wrong dimmensions')

    neighbors = np.zeros((150,50), dtype=np.int8)

    for i in range(50):
        tempMite = np.copy(mite)

        tempMite[0, i] = (tempMite[0, i] + 1) % 4
        neighbors[3*i, :] = np.copy(tempMite)
        tempMite[0, i] = (tempMite[0, i] + 1) % 4
        neighbors[3*i+1, :] = np.copy(tempMite)
        tempMite[0, i] = (tempMite[0, i] + 1) % 4
        neighbors[3*i+2, :] = np.copy(tempMite)

    return neighbors

def main():
    randMite = uniformRandMite()
    n = getNeighbors(randMite)

    print 'Randomly generated mite: \n' + str(randMite)
    print 'First six neighbors of randomly generated mite: \n' + str(n[0:6, :])

if __name__ == "__main__": main()