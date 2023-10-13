import math
from calculations import calc_less as cl
from calculations import calc_exact as ce
from calculations import calc_more as cm

def main():

    chance = input("Give the drop chance using format x/y:\n")
    killcount = int(input("Give current kill count:\n"))
    current_drops = int(input("Give the current amount of drops:\n"))

    drop_info = chance.split("/")
    drop_info = [float(x) for x in drop_info]

    if current_drops == 0:
        probability = ce(drop_info, killcount, current_drops)
        #Chance to get 0 drops
        print(f"The chance of getting 0 drops is {probability:.2f}%.")
        #Chance to get more than 0 drops
        print(f"The chance of getting more than 0 drops is {100-probability:.2f}%.")

    else:
        #Chance to get less than x drops
        chance_less_than = 0
        for i in range(0, current_drops):
            binomial_coefficient = math.factorial(killcount)/(math.factorial(i)*math.factorial(killcount-i))
            probability_mass_function = (drop_info[0]/drop_info[1])**i*(1-drop_info[0]/drop_info[1])**(killcount-i)
            chance_less_than += binomial_coefficient*probability_mass_function*100

        print(f"Chance to get less than {current_drops} drops is {chance_less_than:.2f}%.")


        #Chance to get exactly x drops
        binomial_coefficient = math.factorial(killcount)/(math.factorial(current_drops)*math.factorial(killcount-current_drops))
        probability_mass_function = (drop_info[0]/drop_info[1])**current_drops*(1-drop_info[0]/drop_info[1])**(killcount-current_drops)
        chance_exact = binomial_coefficient*probability_mass_function*100
        print(f"Chance to get exactly {current_drops} drops is {chance_exact:.2f}%.")

        #Chance to get more than x drops
        print(f"Chance to get more than {current_drops} drops is {100 - chance_exact - chance_less_than:.2f}%.")

    print(f"Expected amount of drops is {killcount*(drop_info[0]/drop_info[1]):.4f}.")

    input("Press enter to exit.\n")

main()