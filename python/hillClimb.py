import numpy as np
from scoring import oneThreeScoring
from miteManagement import getNeighbors


# This function will take in a mite, a function to get neighbors, and a scoring function
# It will perform hill climbing and return the locally optimum mite (all neighbors are worse scores)
def miteBasicHillClimb(startMite, neighborFunc = getNeighbors, scoreFunc = oneThreeScoring):
    curMite = np.copy(np.reshape(startMite, (1, 50)))
    while 1:
        neighbors = neighborFunc(curMite)
        scores = scoreFunc(np.vstack((curMite, neighbors)))

        bestMite = np.argmax(scores, axis = 0)

        # If best mite is the current mite, return it
        if bestMite == 0:
            return curMite

        else:
            print "Cur best score: " + str(scores[bestMite,0])
            curMite = np.copy(neighbors[bestMite-1, :])


def main():
    ones = np.ones((1, 50))

    localBestMite1 = miteBasicHillClimb(ones)

    print "Best mite found starting at the ones mite is: " + str(localBestMite1)


if __name__ == "__main__": main()
