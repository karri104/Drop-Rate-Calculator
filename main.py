import math
from calculations import calc_probabilities as calc_probs

def main():

    chance = input("Give the drop chance using format x/y:\n")
    n = int(input("Give current killcount:\n"))
    k = int(input("Give the current amount of drops:\n"))

    prob = chance.split("/")
    prob = [float(x) for x in prob]

    chances = calc_probs(prob, n, k)

    if k == 0:
        #Chance to get 0 drops
        print(f"The chance of getting 0 drops is {chances[1]:.2f}%.")

        #Chance to get more than 0 drops
        print(f"The chance of getting more than 0 drops is {chances[2]:.2f}%.")
    else:
        #Chance to get less than x drops
        print(f"Chance to get less than {k} drops is {chances[0]:.2f}%.")

        #Chance to get exactly x drops
        print(f"Chance to get exactly {k} drops is {chances[1]:.2f}%.")

        #Chance to get more than x drops
        print(f"Chance to get more than {k} drops is {chances[2]:.2f}%.")

        #Expected amount of drops
        print(f"Expected amount of drops is {n * (prob[0] / prob[1]):.4f}.")

    input("Press enter to exit.\n")

main()