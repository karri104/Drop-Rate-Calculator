import math

def calc_fac(n):
    facs = []
    for i in range(1, n + 1):
        facs.append(math.factorial(i))
    return facs

def pmf(prob, n, k):
    #Probability Mass function
    val_pmf = (prob[0] / prob[1]) ** k * (1 - prob[0] / prob[1]) ** (n - k)
    return val_pmf

def calc_less(prob, n, k):
    pass

def calc_exact(prob, n, k):
    chance = (1 - prob[0] / prob[1]) ** n * 100
    return chance

def calc_more(prob, n, k):
    pass

calc_fac(10)