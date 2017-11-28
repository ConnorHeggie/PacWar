import numpy as np

# This function will generate a uniformly random mite (takes a seed)
def uniformRandMite(seed = None):
    if seed != None:
        np.random.seed(seed)

    return np.random.randint(0, 4, size=(1, 50), dtype=np.int8)

# This function will generate a population of uniformly random mites (takes a seed)
def uniformRandPop(popSize, seed = None):
    pop = np.zeros((0, 50))

    for i in range(popSize):
        pop = np.vstack((pop, uniformRandMite(seed)))

    return pop

# This function will take in a population matrix (each row being a mite)
# and will return the mean hamming distance of the population
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

def getGeneNeighbors(mite, gene):
    if mite.shape != (1,50):
        raise ValueError('Mite has wrong dimmensions')

    if gene == 'U':
        nums = (0, 4)
    elif gene == 'V':
        nums = (4, 20)
    elif gene == 'W':
        nums = (20, 23)
    elif gene == 'X':
        nums = (23, 26)
    elif gene == 'Y':
        nums = (26, 38)
    elif gene == 'Z':
        nums = (38, 50)
    else:
        raise ValueError('Gene input not valid')

    neighbors = np.zeros((3 * (nums[1]-nums[0]), 50), dtype=np.int8)
    numInds = range(nums[0], nums[1])

    for i in range(nums[1]-nums[0]):
        ind = numInds[int(i/3)]

        tempMite = np.copy(mite)

        tempMite[0, ind] = (tempMite[0, ind] + 1) % 4
        neighbors[3*i, :] = np.copy(tempMite)

        tempMite[0, ind] = (tempMite[0, ind] + 1) % 4
        neighbors[3*i+1, :] = np.copy(tempMite)

        tempMite[0, ind] = (tempMite[0, ind] + 1) % 4
        neighbors[3*i+2, :] = np.copy(tempMite)

    return neighbors

def main():
    randMite = uniformRandMite()
    n = getNeighbors(randMite)

    print 'Randomly generated mite: \n' + str(randMite)
    print 'First six neighbors of randomly generated mite: \n' + str(n[0:6, :])

    ones = np.ones((1, 50))

    print "Gene U neighbors for mite all ones"
    print getGeneNeighbors(ones, 'U')

if __name__ == "__main__": main()