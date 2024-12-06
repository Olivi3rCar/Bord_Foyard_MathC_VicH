"""file containing the functions regarding the logical challenges"""

# imports
import random as rd
from time import sleep
from playsound import playsound

"""functions"""

"""GAME OF NIM"""

def display_sticks(n : int) -> None :
    """
    Displays on screen the sticks remaining on the board
    :param n: number of sticks
    """
    print("Board : " + "|"*n)
    sleep(2)

def player_removal(n : int) -> int :
    """
    Asks the player for the number of sticks to remove (1,2,3)
    then removes this number
    :param n: number of sticks on board before removal
    :return: number of sticks on board after removal
    """
    r = -1
    while not 1 <= r <= 3 : r = int(input("How many sticks do you want to remove? (1-2-3) "))
    # play adequate sound effect
    playsound(f"soundeffects/sticks{r}.wav")
    print(r, "sticks removed")
    return n - r

def master_removal(n : int, difficulty : int) -> int :
    """
    The master removes a number of sticks based on a strategy
    regarding the multiples of 4 along with the difficulty level
    :param n: number of sticks on board before removal
    :param difficulty: difficulty level
    :return: number of sticks on board after removal
    """

# Tests
n = 5
display_sticks(n)
n = player_removal(n)
display_sticks(n)