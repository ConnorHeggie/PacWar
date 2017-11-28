import numpy as np
from scoring import oneThreeScoring, fromFilePopScoring
from miteManagement import uniformRandMite, getNeighbors

# This function will generate a random mite and then run it through basic hill climbing with the provided
# scoring function
def hillClimbedMite(scoreFunc=fromFilePopScoring,seed=None):
    return miteBasicHillClimb(uniformRandMite(seed), scoreFunc=scoreFunc)


# This function will generated a hill climbed population
def hillClimbedPop(popSize, scoreFunc=fromFilePopScoring,seed=None):
    print "Generating random hill climbed population"
    pop = np.zeros((popSize, 50))

    for i in range(popSize):
        print "Start hill climber for mite creation: " + str(i+1) + " / " + str(popSize)
        pop[i, :] = hillClimbedMite(scoreFunc, seed)

    return pop


# This function will take in a mite, a function to get neighbors, and a scoring function
# It will perform hill climbing and return the locally optimum mite (all neighbors are worse scores)
def miteBasicHillClimb(startMite, neighborFunc = getNeighbors, scoreFunc = oneThreeScoring):
    curMite = np.copy(np.reshape(startMite, (1, 50)))
    plateauCounter = 0

    while 1:
        neighbors = neighborFunc(curMite)
        scores = scoreFunc(np.vstack((curMite, neighbors)))
        curScore = scores[0]
        # Check to see if the best value is unique
        sortedScoreInds = np.argsort(scores, axis=0)

        if scores[sortedScoreInds[-1]] != scores[sortedScoreInds[-2]] or scores[sortedScoreInds[-1]] == 20:
            bestMite = sortedScoreInds[-1][0]
            plateauCounter = 0

        else:
            # If the best mite is not unique, randomly grab one of the best ones that's not the current one
            possibleMites = (scores==scores[sortedScoreInds[-1]]).nonzero()[0]
            newMite = 0
            while newMite==0:
                newMite = np.random.choice(possibleMites)

            bestMite = newMite

            if scores[sortedScoreInds[-1]] == curScore:
                plateauCounter += 1
                if plateauCounter > 10:
                    return curMite

        # If best mite is the current mite, return it
        if bestMite == 0:
            print "Ending hill climber, best mite is: " + str(curMite)
            return curMite

        else:
            print "Cur best score: " + str(scores[bestMite,0])
            curMite = np.copy(np.reshape(neighbors[bestMite-1, :], (1,50)))


def main():
    ones = np.ones((1, 50))

    localBestMite1 = miteBasicHillClimb(ones)

    print "Best mite found starting at the ones mite is: " + str(localBestMite1)


if __name__ == "__main__": main()
