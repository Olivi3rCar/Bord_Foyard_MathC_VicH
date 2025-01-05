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
    Returns True if the keyword entered by the user is the answer and False if the user fails to get correct after 5-diff tries
    :param diff: used to determine the number of tries, ranging from 4 to 2 depending on the difficulty
    :return: bool: True if the user wins, False otherwise
    """
    #Gets the parent directory of the file to access the clues' JSON located in another directory
    parent=os.path.dirname(__file__)
    json_path=parent +"\Data\TRClues.json"

    #opening the file and loading it with JSON
    f=open(json_path,'r')
    clues_dict=load(f)

    #Randomly choosing a set of clues and its corresponding keyword using choice and dictionnary
    year = choice(list(clues_dict['Fort Boyard'].keys()))
    show= choice(list(clues_dict['Fort Boyard'][year].keys()))
    clues_list=list(clues_dict['Fort Boyard'][year][show].values())

    print("Here goes the final challenge !\nIn this trial, you will have to guess the secret word using the clues we will give you.\n")

    #for loop to allow to perform multiple tries, with 5-diff tries
    for tries in range(5-diff):

        #Displaying the number of tries left
        if 5-diff-tries==1:
            print("You have 1 try left.")
        else:
            print("You have {} tries left.".format(5-diff-tries))

        #Printing the clues list and adding one clue after each failed try whith list slices
        print(clues_list[0][:3+tries])
        answer=str(input("What is the secret word ? "))

        #Checking the user's answer
        if uppercase(answer) == clues_list[1]:
            f.close()
            return True
        else:
            print("Wrong answer!\n")
    f.close()
    return False