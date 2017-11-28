import numpy as np
from scoring import basicFight, fromFilePopScoring
from geneticAlgorithm import basicPopCrossOver, totalPopCrossOver
from hillClimb import miteSelfByGeneClimb

np.set_printoptions(threshold=np.nan)

ones = np.ones((1,50))
threes = np.ones((1,50)) * 3

initPop = np.load('gen0.npy')
gen = 1
while True:
	print "gen " + str(gen - 1)
	print initPop
	
	newPop = totalPopCrossOver(initPop)
	for i in range(newPop.shape[0]):
		newPop[i, :] = miteSelfByGeneClimb(newPop[i, :])
	newPopSize = newPop.shape[0]
	filteredPop = np.zeros((0, 50))
	fileScores = fromFilePopScoring(newPop)
	scores = []
	for i in range(len(fileScores)):
		scores.append((newPop[i, :], fileScores[i, 0]))
	scores.sort(key=lambda tup: tup[1], reverse=True)
	for mite, score in scores[:min(len(scores), 30)]:
		filteredPop = np.vstack((filteredPop, mite))
	np.save("gen" + str(gen) + ".npy", filteredPop)
	np.save("savedPop.npy", filteredPop)
	initPop = filteredPop
	gen += 1

