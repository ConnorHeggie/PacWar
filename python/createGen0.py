import numpy as np
from scoring import basicFight
from miteManagement import uniformRandPop

np.set_printoptions(threshold=np.nan)

# my_mites = [
# "0 1 3 0 0 0 0 2 1 0 0 1 2 0 3 1 3 3 3 3 1 2 3 3 2 3 3 2 1 3 1 3 1 2 3 3 2 1 0 0 3 3 1 1 3 1 3 3 1 0",
# "0 1 3 0 0 0 0 3 0 0 0 1 2 0 3 1 3 3 3 3 1 2 3 3 2 3 3 2 1 3 1 3 1 2 3 3 2 1 0 0 3 3 1 1 3 1 3 3 1 0",
# "3 0 3 3 3 3 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3",
# "3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3",
# "1 0 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1",
# "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"
# ]
#
# for i in range(len(my_mites)):
# 	my_mites[i] = [int(x) for x in my_mites[i].split()]

my_mites = uniformRandPop(100).astype(np.uint8)

mites = np.array(my_mites)
np.save("gen0.npy", mites)