import numpy as np
from scoring import basicFight, fromFilePopScoring
from geneticAlgorithm import basicPopCrossOver, totalPopCrossOver, fullGenePopCrossover, basicPopMutation
from hillClimb import miteSelfByGeneClimb
import sys

np.set_printoptions(threshold=np.nan)

print sys.argv

runDir = './run-X/'
populationSize = 6
hillClimb = False

if len(sys.argv) > 1 and sys.argv[1] == "climb":
	hillClimb = True

if len(sys.argv) > 2:
	try:
		populationSize = int(sys.argv[2])
	except:
		populationSize = 6

if len(sys.argv) > 3:
	runDir = sys.argv[3]

ones = np.ones((1,50))
threes = np.ones((1,50)) * 3

initPop = np.load(runDir + 'gen0.npy')
gen = 1
while True:
	print "gen " + str(gen - 1)
	print initPop
	
	newPop = fullGenePopCrossover(initPop, hillClimb=hillClimb, fileName=runDir + 'savedPop.npy')
	newPop = basicPopMutation(newPop)
	if hillClimb:
		for i in range(newPop.shape[0]):
			newPop[i, :] = miteSelfByGeneClimb(newPop[i, :])
	newPopSize = newPop.shape[0]
	filteredPop = np.zeros((0, 50))
	fileScores = fromFilePopScoring(newPop, savedMitesFile=runDir + 'savedPop.npy')
	scores = []
	for i in range(len(fileScores)):
		scores.append((newPop[i, :], fileScores[i, 0]))
	scores.sort(key=lambda tup: tup[1], reverse=True)
	for mite, score in scores[:min(len(scores), populationSize)]:
		filteredPop = np.vstack((filteredPop, mite))
	np.save(runDir + "gen" + str(gen) + ".npy", filteredPop)
	np.save(runDir + "savedPop.npy", filteredPop)
	initPop = filteredPop
	gen += 1

