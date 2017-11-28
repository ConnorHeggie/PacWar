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

saved_pop = np.load('gen0.npy')

for mite in saved_pop:
	print mite
	print basicFight(mite, mite1)
	


