import numpy as np

# This function with generate a uniformly random mite (takes a seed)
def uniformRandMite(seed = None):
    if seed != None:
        np.random.seed(seed)
    return np.random.randint(0, 3, size=(1,50), dtype=np.int8)


# This function will take in a mite and return a matrix containing all its 1 hamming distance neighbors
# The output will be a 150x50 numpy array where each row is a mite
def getNeighbors(mite):
    neighbors = np.zeros((150,50), dtype=np.int8)
    for i in range(50):
        neighbors

def main():
    print 'Randomly generated mite: ' + str(list(uniformRandMite()))

if __name__ == "__main__": main()