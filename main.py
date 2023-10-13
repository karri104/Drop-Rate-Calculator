import math
from calculations import calc_probabilities as calc_prob

def main():

    chance = input("Give the occurence chance using format x/y:\n")
    n = int(input("Give current amount of triggers (events that may lead to a thing happening):\n"))
    k = int(input("Give the current amount of occurences:\n"))

    prob = chance.split("/")
    prob = [float(x) for x in prob]

    #Chance to get 0 occurences
    print(f"The chance of getting 0 occurences is {probability:.2f}%.")

    #Chance to get more than 0 occurences
    print(f"The chance of getting more than 0 occurences is {100 - probability:.2f}%.")

    #Chance to get less than x occurences
    print(f"Chance to get less than {k} occurences is {chance_less_than:.2f}%.")

    #Chance to get exactly x occurences
    print(f"Chance to get exactly {k} occurences is {chance_exact:.2f}%.")

    #Chance to get more than x occurences
    print(f"Chance to get more than {k} occurences is {100 - chance_exact - chance_less_than:.2f}%.")

    #Expected amount of occurences
    print(f"Expected amount of occurences is {n * (prob[0] / prob[1]):.4f}.")

    input("Press enter to exit.\n")

main()