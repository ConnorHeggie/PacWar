import numpy as np
from scoring import basicFight, popVersusPopFight, roundRobinScore
from geneticAlgorithm import basicCrossOver

np.set_printoptions(threshold=np.nan)

ones = np.ones((1,50))
threes = np.ones((1,50)) * 3

mite1 = "0 1 3 0 0 0 0 3 0 0 0 1 2 0 3 1 3 3 3 3 1 2 3 3 2 3 3 2 1 3 1 3 1 2 3 3 2 1 0 0 3 3 1 1 3 1 3 3 1 0"
mite1 = [int(x) for x in mite1.split()]
mite1 = np.array(mite1)

# mite2 = "0 1 3 0 0 0 0 2 1 0 0 1 2 0 3 1 3 3 3 3 1 2 3 3 2 3 3 2 1 3 1 3 1 2 3 3 2 1 0 0 3 3 1 1 3 1 3 3 1 0"
# mite2 = [int(x) for x in mite2.split()]
# mite2 = np.array(mite2)

# print basicFight(mite1, mite2)

saved_pop = np.load('./run2-pop6-hc/savedPop.npy')
test_pop = np.load('./run3-pop100/savedPop.npy')

all_mites = np.load('./run2-pop6-hc/gen0.npy')


for i in range(1, 29):
	all_mites = np.vstack((all_mites, np.load('./run2-pop6-hc/gen' + str(i) + ".npy")))
scores = roundRobinScore(all_mites)
score_pairs = []

for i in range(all_mites.shape[0]):
	mite = all_mites[i, :].astype(np.unint8)
	score = scores[i][0]
	score_pairs.append((mite, score))
score_pairs.sort(key=lambda tup: tup[1], reverse=True)

best_mites = score_pairs[0][0]
for i in range(1, 10):
	best_mites = np.vstack((best_mites, score_pairs[i][0]))
print best_mites

# print popVersusPopFight(saved_pop, test_pop)
# print roundRobinScore(saved_pop)
# print saved_pop[5, :].astype(np.uint8)


# top_mite_inds = []

# for i in range(test_pop.shape[0]):
# 	mite = test_pop[i, :]
# 	print mite
# 	curScore = basicFight(mite, mite1)[0]
# 	print curScore

	# if curScore >= 10:
	# 	top_mite_inds.append(i)

# best_pop = saved_pop[top_mite_inds, :]
# print "Currently the best population is: "
# print best_pop
# np.save('best-mites-1.npy', best_pop)
	


