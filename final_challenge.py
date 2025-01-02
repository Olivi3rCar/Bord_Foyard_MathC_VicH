"""file containing the functions regarding the final challenge"""
from json import load
from random import choice
import os

def uppercase(s : str) -> str :
    """
    Returns the uppercased version of a string
    :param s: string to be upercased
    :return: uppercase version of the string
    """
    # instantiation of string to be returned
    ns = ""
    # iteration over s
    for c in s:
        # test of position of current char relative to uppercase bounds (A & Z)
        if ord('a') <= ord(c) <= ord('z'):
            # concatenation of lowercase-converted current char to string
            ns += chr(ord(c) + (ord('A') - ord('a')))
        else :
            # concatenation of current car to string
            ns += c
    return ns



def treasure_room(diff) -> bool:
    """
    :return: bool: Returns whether the player has won the game or not
    """
    parent=os.path.dirname(__file__)
    json_path=parent +"\Data\TRClues.json"

    f=open(json_path,'r')
    clues_dict=load(f)

    year = choice(list(clues_dict['Fort Boyard'].keys()))
    show= choice(list(clues_dict['Fort Boyard'][year].keys()))
    clues_list=list(clues_dict['Fort Boyard'][year][show].values())

    print("Here goes the final challenge !\nIn this trial, you will have to guess the secret word using the clues we will give you.")

    for tries in range(5-diff):

        if 3-tries==1:
            print("You have 1 try left.")
        else:
            print("You have {} tries left.".format(3-tries))

        print(clues_list[0][:3+tries])
        answer=str(input("What is the secret word ? "))

        if uppercase(answer) == clues_list[1]:
            return True

    return False