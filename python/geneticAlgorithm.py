import numpy as np
from miteManagement import uniformRandPop
from scoring import oneThreeScoring, fromFilePopScoring
from hillClimb import hillClimbedPop, miteBasicHillClimb

np.set_printoptions(threshold=np.nan)
f = open("genAlgOutput.txt", 'w')

# This function will take 2 populations and cross over randomly within each gene
def randomGenePopCrossOver(pop, hillClimb=True, fileName="savedPop.npy"):
    popSize = pop.shape[0]
    newPop = np.copy(pop)
    for i in range(popSize):
        for j in range(i + 1, popSize):
            mite1 = pop[i, :]
            mite2 = pop[j, :]
            newMite1, newMite2 = randomGeneCrossOver(mite1, mite2)
            if hillClimb:
                newPop = np.vstack((newPop, miteBasicHillClimb(newMite1, fileName=fileName), miteBasicHillClimb(newMite2, fileName=fileName)))
            else:
                newPop = np.vstack((newPop, newMite1, newMite2))
    return newPop


def randomGeneCrossOver(mite1, mite2):
    mite1 = np.reshape(np.copy(mite1), (1, 50))
    mite2 = np.reshape(np.copy(mite2), (1, 50))
    newMite1 = np.reshape(np.copy(mite1), (1, 50))
    newMite2 = np.reshape(np.copy(mite2), (1, 50))

    geneInds = np.array([(0, 4), (4, 20), (20, 23), (23, 26), (26, 38), (38, 50)])
    numCrosses = np.random.randint(0, 7)
    crossGenes = np.random.choice(range(6), size=numCrosses, replace=False)

    for i in range(numCrosses):
        curRange = geneInds[crossGenes[i], :]

        crossInds = (curRange[0], np.random.randint(curRange[0]+1, curRange[1]))

        newMite1[0, crossInds[0]:crossInds[1]] = mite2[0, crossInds[0]:crossInds[1]]
        newMite2[0, crossInds[0]:crossInds[1]] = mite1[0, crossInds[0]:crossInds[1]]

    return newMite1, newMite2


# This function will take 2 populations and cross over up to 3 random full genes between mite pairs
def fullGenePopCrossOver(pop, hillClimb=True, fileName="savedPop.npy"):
    popSize = pop.shape[0]
    newPop = np.copy(pop)
    for i in range(popSize):
        for j in range(i + 1, popSize):
            mite1 = pop[i, :]
            mite2 = pop[j, :]
            newMite1, newMite2 = fullGeneCrossOver(mite1, mite2)
            if hillClimb:
                newPop = np.vstack((newPop, miteBasicHillClimb(newMite1, fileName=fileName), miteBasicHillClimb(newMite2, fileName=fileName)))
            else:
                newPop = np.vstack((newPop, newMite1, newMite2))
    return newPop


# This function will take in 2 mites and randomly cross over up to 3 full genes
def fullGeneCrossOver(mite1, mite2):
    newMite1 = np.copy(mite1)
    newMite2 = np.copy(mite2)

    geneInds = np.array([(0, 4), (4, 20), (20, 23), (23, 26), (26, 38), (38, 50)])
    numCrosses = np.random.randint(1, 4)
    crossGenes = np.random.choice(range(6), size=numCrosses, replace=False)
    crossInds = geneInds[crossGenes, :]

    # print(crossInds)

    for i in range(numCrosses):
        newMite1[crossInds[i][0]:crossInds[i][1]] = mite2[crossInds[i][0]:crossInds[i][1]]
        newMite2[crossInds[i][0]:crossInds[i][1]] = mite1[crossInds[i][0]:crossInds[i][1]]

    return newMite1, newMite2


# This function will take in 2 mites and randomly cross them over k times
def basicCrossOver(mite1, mite2, k=1, spliceSize=-1):
    randInds = list(np.sort(np.random.choice(49, size=(k), replace=False)))
    print randInds
    newMite1 = np.copy(mite1)
    newMite2 = np.copy(mite2)

    for i in randInds:
        if spliceSize == -1:
            temp1 = newMite1[i:]
            temp2 = newMite2[i:]

            newMite1[i:] = temp2
            newMite2[i:] = temp1
        else:
            if spliceSize == 0:
                end = np.random.choice(np.array(range(i + 1, 50)))
            else:
                end = min(i + spliceSize + 1, 50)
            temp1 = np.copy(newMite1[0, i:end])
            temp2 = np.copy(newMite2[0, i:end])

            newMite1[0, i:end] = temp2
            newMite2[0, i:end] = temp1
            print newMite1
            print newMite2

    return newMite1, newMite2

# This function will take a population and breed every mite in the population
# with each other.
def totalPopCrossOver(pop, hillClimb=True, fileName="savedPop.npy"):
    popSize = pop.shape[0]
    newPop = np.copy(pop)
    for i in range(popSize):
        for j in range(i + 1, popSize):
            mite1 = pop[i, :]
            mite2 = pop[j, :]
            newMite1, newMite2 = basicCrossOver(mite1, mite2, spliceSize=0)
            if hillClimb:
                newMite1 = miteBasicHillClimb(newMite1, fileName=fileName)
                newMite2 = miteBasicHillClimb(newMite2, fileName=fileName)
            newPop = np.vstack((newPop, newMite1, newMite2))
    return newPop


# This function will take in a population and return a population of the same size
# where the new population is a crossovered version of the original population

# THIS FUNCTION DOES NOT SELECTIVELY BREED. IT JUST BREEDS THE ENTIRE POPULATION.
# IT DOES NOT MODEL SURVIVAL OF THE FITTEST.
def basicPopCrossOver(pop, k=1, seed=None, hillClimb=True, fileName="savedPop.npy"):
    if seed != None:
        np.random.seed(seed)

    popSize = pop.shape[0]
    newPop = np.zeros(pop.shape)

    # YOU DON"T USE THIS SO THE SAME MITES ARE ALWAYS BEING CROSSED.
    randInds = np.random.choice(popSize, size=(popSize), replace=False)

    for i in range(0, popSize, 2):
        mite1 = pop[randInds[i], :]
        mite2 = pop[randInds[i+1], :]

        newMite1, newMite2 = basicCrossOver(mite1, mite2, k, spliceSize=0)

        if hillClimb:
            newPop[i, :] = miteBasicHillClimb(newMite1, fileName=fileName)
            newPop[i+1, :] = miteBasicHillClimb(newMite2, fileName=fileName)
        else:
            newPop[i, :] = newMite1
            newPop[i + 1, :] = newMite2

    return newPop


# This function will take in a mite and return a mutated version of it
# where the mutation is decided with the mutation rate and will randomly change to one of the other values
def basicMutation(mite, mutationRate = .02):
    newMite = np.copy(mite)

    mutationInds = np.random.choice(2, size=(len(mite)), p=np.array([1-mutationRate, mutationRate]))
    mutationInds = np.nonzero(mutationInds)[0]

    for i in mutationInds:
        if mite[i] == 0:
            newMite[i] = np.random.choice([1, 2, 3])
        elif mite[i] == 1:
            newMite[i] = np.random.choice([0, 2, 3])
        elif mite[i] == 2:
            newMite[i] = np.random.choice([0, 1, 3])
        else:
            newMite[i] = np.random.choice([0, 1, 2])

    return newMite


# This function will take in a population and return a population of the same size
# where the new population is a mutated version of the original
def basicPopMutation(pop, mutationRate = .02):
    popSize = pop.shape[0]
    newPop = np.copy(pop)

    # CURRENTLY MUTATING ENTIRE POPULATION. MAYBE SELECTIVELY MUTATE
    for i in range(popSize):
        newPop[i, :] = basicMutation(pop[i, :], mutationRate)

    return newPop


# This function will take a pop size, selection keep rate, number of generations, mutation func,
# crossover function, initialize population function, and scoring function, perform a genetic algorithm,
# and then return the resulting population
def genetic_algorithm(popSize=50, keepRate=0.3, mutationFunc=basicPopMutation, numGen=10, initPopFunc=uniformRandPop, crossOverFunc=basicPopCrossOver, scoreFunc=fromFilePopScoring):
    pop = initPopFunc(popSize)
    print "intial population: "
    print pop
    f.write("inital population:\n")
    f.write(pop)
    keepNum = int(np.ceil(keepRate*popSize))
    crossNum = popSize-keepNum

    if crossNum % 2 != 0:
        # Makes sure we have an even number for crossover
        keepNum -= 1
        crossNum += 1

    for i in range(numGen):
        scores = scoreFunc(pop)

        print "Average score for generation " + str(i+1) + " is " + str(np.mean(scores))
        f.write("Average score for generation " + str(i+1) + " is " + str(np.mean(scores)) + "\n")
        print "Generation " + str(i + 1) + " population:"
        f.write("Generation " + str(i + 1) + " population:\n")
        print pop
        f.write("pop")

        newPop = np.zeros(pop.shape)

        # Perform selection
        selectionProbs = np.reshape(scores / np.sum(scores), (-1)) #need the reshape to turn it into 1D array
        selectionInds = np.random.choice(popSize, size=(keepNum), p=selectionProbs)
        newPop[0:keepNum, :] = np.copy(pop[selectionInds, :])

        # Perform crossover
        crossPop = pop[np.random.choice(popSize, size=(crossNum), replace=False), :]
        newPop[keepNum:, :] = crossOverFunc(crossPop)

        # Perform mutation
        newPop = mutationFunc(newPop)

        pop = np.copy(newPop)

    return pop


def main():
    # pop = genetic_algorithm(popSize=50, numGen=250, initPopFunc=hillClimbedPop)

    # print(pop)

    ones = np.ones((1,50))
    threes = np.copy(ones) * 3

    print "Full gene crossover: " + str(fullGeneCrossOver(ones, threes))
    print "Random gene crossover: " + str(randomGeneCrossOver(ones, threes))


if __name__ == "__main__": main()
