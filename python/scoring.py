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
