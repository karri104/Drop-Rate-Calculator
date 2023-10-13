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
    coeff = facs(n) / (facs(k) * facs(n - k))
    return coeff

def calc_single(prob, n, k):
    chance = (1 - prob[0] / prob[1]) ** n * 100
    return chance

def calc_probabilities(prob, n, k):
    pass
