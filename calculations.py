import math


def calc_fac(n):
    # Form a list for factorials as list lookup happens in O(1) instead of O(n!) of factorials
    # making factorial lookup later a lot faster (in theory)
    facs = [1]
    for i in range(1, n + 1):
        facs.append(facs[i - 1] * i)
    return facs


def pmf(prob, n, k):
    #Partial Probability Mass function (Missing binomial coefficient)
    part_pmf = (prob[0] / prob[1]) ** k * (1 - prob[0] / prob[1]) ** (n - k)
    return part_pmf


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
        chances[1] = (1 - prob[0] / prob[1]) ** n * 100
        chances[2] = 100 - chances[1]
    else:
        chance = 0
        for i in range(0, k):
            chance += calc_single(prob, n, i)
            print("Hola")
        chances[0] = chance
        chances[1] = calc_single(prob, n, k)
        chances[2] = 100 - chances[0] - chances[1]
    return chances
