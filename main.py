from utility_functions import *
from json import load
from logical_challenges import nim_game, battleship_game
from math_challenges import (math_challenge_factorial, solve_linear_equation,
                             math_challenge_prime, math_roulette_challenge)
from pere_fouras_challenge import pere_fouras_riddles
from chance_challenges import (shell_game,roll_dice_game)
import random as rd
from final_challenge import treasure_room

def game():
    # introduction()
    # compose_equipe()
    # diff=choose_difficulty()
    """Initialisation of the available_challenges dictionnary used in the challenges_menu function.
       The role of this dict is to allow the user to only
       try the challenges that are associated with the contained numbers."""
    available_challenges = {1: "Mathematics challenges", 2: "Logic challenge",
                            3: "Chance challenge", 4: "Père Fouras's riddle"}

    math_list = [math_challenge_factorial, solve_linear_equation, math_challenge_prime, math_roulette_challenge]
    chance_list = [shell_game, roll_dice_game]
    logical_list = [nim_game, battleship_game]
    perefouras_list = [pere_fouras_riddles]

    all_challenges = [math_list, chance_list, logical_list, perefouras_list]

    # challenge = rd.choice(rd.choice(all_challenges))
    # if challenge(diff):
    #     print("bravo")
    keys=0
    while keys!=3:
        chosen_chall=all_challenges[challenges_menu(available_challenges)]
        print(chosen_chall)

    """VICTOR PLEASE IMPLEMENT WIN AND LOSS SOUND EFFECTS IN MAIN PLZZZZ"""




if __name__ == '__main__':

    game()