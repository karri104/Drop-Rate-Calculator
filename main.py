import math
from calculations import calc_probabilities as calc_prob

def main():

    chance = input("Give the drop chance using format x/y:\n")
    n = int(input("Give current kill count:\n"))
    k = int(input("Give the current amount of drops:\n"))

    prob = chance.split("/")
    prob = [float(x) for x in prob]

    if k == 0:
        probability = ce(prob, n, k)
        #Chance to get 0 drops
        print(f"The chance of getting 0 drops is {probability:.2f}%.")
        #Chance to get more than 0 drops
        print(f"The chance of getting more than 0 drops is {100 - probability:.2f}%.")

    else:
        #Chance to get less than x drops
        chance_less_than = 0
        for i in range(0, k):
            binomial_coefficient = math.factorial(n) / (math.factorial(i) * math.factorial(n - i))
            probability_mass_function = (prob[0] / prob[1]) ** i * (1 - prob[0] / prob[1]) ** (n - i)
            chance_less_than += binomial_coefficient * probability_mass_function * 100

        print(f"Chance to get less than {k} drops is {chance_less_than:.2f}%.")

        #Chance to get exactly x drops
        binomial_coefficient = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
        probability_mass_function = (prob[0] / prob[1]) ** k * (1 - prob[0] / prob[1]) ** (n - k)
        chance_exact = binomial_coefficient * probability_mass_function * 100
        print(f"Chance to get exactly {k} drops is {chance_exact:.2f}%.")

        #Chance to get more than x drops
        print(f"Chance to get more than {k} drops is {100 - chance_exact - chance_less_than:.2f}%.")

    print(f"Expected amount of drops is {n * (prob[0] / prob[1]):.4f}.")

    input("Press enter to exit.\n")

main()