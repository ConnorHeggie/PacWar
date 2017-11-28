import numpy as np
from scoring import oneThreeScoring, populationVersusMiteFight, roundRobinScore, popVersusPopFight, fromFilePopScoring
from miteManagement import uniformRandMite, getNeighbors, getGeneNeighbors

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
        sortedScoreInds = np.array(np.argsort(scores, axis=0))

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


# This function will take in a mitee, a function to get neighbors, and a stoppping tolerance to allow stopping before you've perfectly beat all neighbors
# It will perform hill climbing (with neighbors scored in a basic fight against the current mite)
# and return the locally optimum mite (all neighbors are worse scores)
# THIS FUNCTION NEVER CONVERGES
def miteSelfHillClimb(startMite, neighborFunc = getNeighbors, stop_tol=1):
    curMite = np.copy(np.reshape(startMite, (1, 50)))

    while True:
        neighbors = neighborFunc(curMite)

        scores = populationVersusMiteFight(neighbors, curMite)

        if np.max(scores) <= stop_tol:
            return curMite

        # Check to see if the best value is unique
        sortedScoreInds = np.argsort(scores)

        if scores[sortedScoreInds[-1]] != scores[sortedScoreInds[-2]]:
            bestMite = sortedScoreInds[-1]

        else:
            # If the best mite is not unique, randomly grab one of the best ones that's not the current one
            possibleMites = (scores==scores[sortedScoreInds[-1]]).nonzero()[0]

            bestMite = np.random.choice(possibleMites)

        curMite = np.copy(np.reshape(neighbors[bestMite, :], (1,50)))


def miteSelfByGeneClimb(startMite, stop_tol=3):
    curMite = np.copy(np.reshape(startMite, (1, 50)))
    pastMites = np.zeros((0,50))

    genes = ['U', 'V', 'W', 'X', 'Y', 'Z']
    geneInd = 0
    maxIter = 10
    i = 0

    for _ in range(3*len(genes)):
        curGene = genes[geneInd]
        pastMites = np.vstack((pastMites, curMite))

        neighbors = getGeneNeighbors(curMite, curGene)

        scores = popVersusPopFight(neighbors, pastMites)

        if np.max(scores) <= stop_tol:
            i = 0
            geneInd = (geneInd+1)%len(genes)
            continue

        # Check to see if the best value is unique
        sortedScoreInds = np.argsort(scores)

        if scores[sortedScoreInds[-1]] != scores[sortedScoreInds[-2]]:
            bestMite = sortedScoreInds[-1]

        else:
            # If the best mite is not unique, randomly grab one of the best ones that's not the current one
            possibleMites = (scores==scores[sortedScoreInds[-1]]).nonzero()[0]
            bestMite = np.random.choice(possibleMites)

        print "Cur best score: " + str(scores[bestMite]) + " optimizing for gene " + str(curGene)

        curMite = np.copy(np.reshape(neighbors[bestMite, :], (1,50)))
        i += 1

        if i >= maxIter:
            i = 0
            geneInd = (geneInd+1)%len(genes)
            continue

    return curMite


def main():
    ones = np.ones((1, 50)) * 3

    localBestMite1 = miteBasicHillClimb(ones)
    print "Finished ones threes climb"

    newMite = '0 1 3 0 0 0 0 2 1 0 0 1 2 0 3 1 3 3 3 3 1 2 3 3 2 3 3 2 1 3 1 3 1 2 3 3 2 1 0 0 3 3 1 1 3 1 3 3 1 0'
    newMite = [int(x) for x in newMite.split()]
    newMite = np.array(newMite)

    localBestMite2 = miteSelfByGeneClimb(ones)
    print "Finished self climbing"

    print "Best mite found starting at the ones mite is: " + str(localBestMite1)
    print "Best mite found with self climbing starting at ones is: " + str(localBestMite2)


if __name__ == "__main__": main()
