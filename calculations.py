import math

def calc_fac(n):
    facs = []
    for i in range(0, n + 1):
        facs.append(math.factorial(i))
    return facs

def pmf(prob, n, k):
    #Probability Mass function
    val_pmf = (prob[0] / prob[1]) ** k * (1 - prob[0] / prob[1]) ** (n - k)
    return val_pmf

def bc(n, k, facs):
    #Binomial coefficient
    coeff = facs[n] / (facs[k] * facs[n - k])
    return coeff

def calc_single(prob, n, k):
    facs = calc_fac(n)
    chance = bc(n, k, facs) * pmf(prob, n, k) * 100
    return chance

def calc_probabilities(prob, n, k):
    chances = [0, 0, 0]
    if k == 0:
        chances[1] = prob[0] / prob[1] ** n
        chances[2] = 100 - chances[1]
    else:
        chance = 0
        for i in range(0, k - 1):
            chance += calc_single(prob, n, i)
        chances[0] = chance
        chances[1] = calc_single(prob, n, k)
        chances[2] = 100 - chances[0] - chances[1]
    return chances
