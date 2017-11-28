import numpy as np
from scoring import basicFight

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

saved_pop = np.load('best-mites-1.npy')
# top_mite_inds = []

for i in range(saved_pop.shape[0]):
	mite = saved_pop[i, :]
	print mite
	curScore = basicFight(mite, threes)[0]
	print curScore

	# if curScore >= 10:
	# 	top_mite_inds.append(i)

# best_pop = saved_pop[top_mite_inds, :]
# print "Currently the best population is: "
# print best_pop
# np.save('best-mites-1.npy', best_pop)
	


