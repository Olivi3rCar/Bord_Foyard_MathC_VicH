from utility_functions import *
from logical_challenges import nim_game, battleship_game
from math_challenges import (math_challenge_factorial, solve_linear_equation,
                             math_challenge_prime, math_roulette_challenge)
from pere_fouras_challenge import pere_fouras_riddles
import random as rd

if __name__ == '__main__':

    """Initialisation of the available_challenges dictionnary used in the challenges_menu function. The role of this dict is to
     allow the user to only try the challenges that are associated with the contained numbers."""
    available_challenges= {1: "Mathematics challenges", 2: "Logic challenge", 3: "Chance challenge", 4: "Père Fouras's riddle"}

    diff=choose_difficulty()

    math_list=[math_challenge_factorial,solve_linear_equation,math_challenge_prime,math_roulette_challenge]
    logical_list = [nim_game, battleship_game]
    perefouras_list = [pere_fouras_riddles]

    all_challenges = [math_list, logical_list, perefouras_list]

    challenge = rd.choice(rd.choice(all_challenges))
    if challenge(diff):
        print("bravo")

    """VICTOR PLEASE IMPLEMENT WIN AND LOSS SOUND EFFECTS IN MAIN PLZZZZ"""