from math_challenges import nearest_prime
from utility_functions import *
from math_challenges import *

if __name__ == '__main__':

    """Initialisation of the available_challenges dictionnary used in the challenges_menu function. The role of this dict is to
     allow the user to only try the challenges that are associated with the contained numbers."""
    available_challenges= {1: "Mathematics challenges", 2: "Logic challenge", 3: "Chance challenge", 4: "Père Fouras's riddle"}

    diff=choose_difficulty()

    math_challenges_list=[math_challenge_factorial,solve_linear_equation,math_challenge_prime,math_roulette_challenge]

    challenge=math_challenge(math_challenges_list)
    if challenge(diff):
        print("bravo")

    """VICTOR PLEASE IMPLEMENT WIN AND LOSS SOUND EFFECTS IN MAIN PLZZZZ"""