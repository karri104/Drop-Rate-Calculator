import math

def calc_fac(killcount):
    facs = []
    for i in range(1, killcount + 1):
        facs.append(math.factorial(i))
    return facs

def calc_less(drop_info, killcount, current_drops):
    pass

def calc_exact(drop_info, killcount, current_drops):
    chance = (1 - drop_info[0] / drop_info[1]) ** killcount * 100
    return chance

def calc_more(drop_info, killcount, current_drops):
    pass

calc_fac(10)