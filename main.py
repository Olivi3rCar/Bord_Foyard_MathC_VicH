from utility_functions import *
from json import load
from logical_challenges import nim_game, battleship_game
from math_challenges import (math_challenge_factorial, solve_linear_equation,
                             math_challenge_prime, math_roulette_challenge)
from pere_fouras_challenge import pere_fouras_riddles
from chance_challenges import (shell_game,roll_dice_game)
import random as rd
import final_challenge

def game():
    introduction()
    team=compose_equipe()
    diff=choose_difficulty()
    """Initialisation of the available_challenges dictionnary used in the challenges_menu function.
       The role of this dict is to allow the user to only
       try the challenges that are associated with the contained numbers."""
    challenges_dict = {1: "Mathematics challenges", 2: "Logic challenge",
                            3: "Chance challenge", 4: "Père Fouras's riddle"}

    math_list = [math_challenge_factorial, solve_linear_equation, math_challenge_prime, math_roulette_challenge]
    chance_list = [shell_game, roll_dice_game]
    logical_list = [nim_game, battleship_game]
    perefouras_list = [pere_fouras_riddles]

    all_challenges = [math_list,  logical_list,chance_list, perefouras_list]

    keys=0
    while keys!=3:
        choosen_challenge = challenges_menu(challenges_dict)
        player = choose_player(team)
        if  choosen_challenge == 2:
            log_chall_choice=int(input("Choose a challenge :\n1. - Nim Game\n2. - Battleship game\nEnter the number of the chosen challenge: "))-1


            if all_challenges[1][log_chall_choice](diff):
                keys += 1
                team[player]["keys_wons"] += 1
                print(team)
            else:
                """Play sound ma gueule"""
            print(team)
        else:
            if rd.choice(all_challenges[choosen_challenge-1])(diff):
                keys+=1
                team[player]["keys_wons"]+=1
                print(team)
            else:
                """Play sound ma gueule"""
                print(team)
    final_challenge.treasure_room(diff)

    """VICTOR PLEASE IMPLEMENT WIN AND LOSS SOUND EFFECTS IN MAIN PLZZZZ"""




if __name__ == '__main__':

    game()
    """VICTOR PLEASE IMPLEMENT WIN AND LOSS SOUND EFFECTS IN MAIN PLZZZZ"""