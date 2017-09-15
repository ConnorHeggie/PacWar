import numpy as np
import _PyPacwar


# This function takes the number of rounds and final counts of the mites after a pacwar battle
# The output is the score from the given scoring method given as a tuple
def basicScoring(rounds,c1,c2):
    if c1 == 0 and c2 != 0:
        if rounds < 100:
            return 0, 20
        elif rounds < 200:
            return 1, 19
        elif rounds < 300:
            return 2, 18
        else:
            return 3, 17
    elif c2 == 0 and c1 != 0:
        if rounds < 100:
            return 20, 0
        elif rounds < 200:
            return 19, 1
        elif rounds < 300:
            return 18, 2
        else:
            return 17, 3
    elif float(c1/c2) >= 10:
        return 13, 7
    elif float(c2/c1) >= 10:
        return 7, 13
    elif float(c1 / c2) >= 3:
        return 12, 8
    elif float(c2 / c1) >= 3:
        return 8, 12
    elif float(c1 / c2) >= 1.5:
        return 11, 9
    elif float(c2 / c1) >= 1.5:
        return 9, 11
    else:
        return 10, 10


# This function will take in two mites and return the scores of each found from a battle and basic score
def basicFight(mite1, mite2):
    (rounds, c1, c2) = _PyPacwar.battle(list(mite1), list(mite2))
    return basicScoring(rounds, c1, c2)


# This function will take in a mite and a population and return the average score of that mite battled against the population
def populationFight(mite, population, scoreFunc = basicScoring):
    raise NotImplementedError('Not yet populationFight')
    return -1


# This function will take in a population (where each row is a mite) and return a column of scores for each mite
# These scores are found by round robin style battling each mite and using the scoring function provided as a parameter
def roundRobinScore(population, scoreFunc = basicScoring):
    numMites = population.shape[0]
    scores = np.zeros((numMites, 1))

    for i in range(numMites-1):
        iMite = population[i, :]

        for j in range(i+1, numMites):
            jMite = population[j, :]

            (rounds, c1, c2) = _PyPacwar.battle(list(iMite), list(jMite))
            iScore, jScore = scoreFunc(rounds, c1, c2)

            scores[i, 0] += iScore
            scores[j, 0] += jScore

    return scores


# This function will take in a population (where each row is a mite) and return a column of scores for each mite
# These scores are found by averaging the scores of each mite battled with a ones mite and a threes mite
def oneThreeScoring(population):
    ones = np.ones((1, 50))
    threes = np.ones((1, 50)) * 3

    numMites = population.shape[0]
    scores = np.zeros((numMites, 1))

    for i in range(numMites):
        score1, _ = basicFight(population[i, :], ones)
        score3, _ = basicFight(population[i, :], threes)
        scores[i] = (score1 + score3)/2.0

    return scores


# This function will take in a population (where each row is a mite) and return a column of scores for each mite
# These scores are found by averaging the scores of each mite battled with the set of saved mites from a file
def fromFileScoring(population):
    raise NotImplementedError('Not yet implemented fromFileScoring')
    return -1

def main():
    ones = np.ones((1,50))
    twos = np.ones((1,50)) * 2
    threes = np.ones((1, 50)) * 3

    scores = roundRobinScore(np.vstack((ones,twos,threes)))

    print "Round robin scoring of ones, twos, and threes produced: \n" + str(scores)


if __name__ == "__main__": main()
