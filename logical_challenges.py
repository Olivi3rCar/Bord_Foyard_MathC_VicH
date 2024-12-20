"""file containing the functions regarding the logical challenges"""

# imports
import random as rd
from time import sleep
from playsound import playsound

"""functions"""

def minimum(a : int, b : int) -> bool :
    """
    :param a: int
    :param b: int
    :return: minimum between a and b
    """
    if a < b : return a
    return b

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
    while not 1 <= r <= 3 & r < n : r = int(input(f"How many sticks \
do you want to remove? ({'-'.join([str(i) for i in range(1, minimum(4, n+1))])}) "))
    # play adequate sound effect
    playsound(f"soundeffects/sticks{r}.wav")
    print(r, "sticks removed", end="")
    return n - r

def master_removal(n : int, difficulty : int) -> int :
    """
    The master removes a number of sticks based on a strategy
    regarding the multiples of 4 along with the difficulty level
    :param n: number of sticks on board before removal
    :param difficulty: difficulty level
    :return: number of sticks on board after removal
    """
    # The Master will always try to remove sticks to that
    # there remains 1+4k sticks when the player has his turn
    s = rd.randint(1, 3)
    for i in range(1,4) :
        if (n-i) % 4 == 1 :
            # If the master can remove i sticks so that his strategy
            # is applicable, we choose to remove i sticks
            s = i
            # randomly change the value depending on the difficulty
            # Except if the number of remaining sticks is below 6
            if n > 6 :
                if s == 3 :
                    s -= [1, 1, 1, 0, 0, 0, 0, 0][rd.randint(difficulty-1,7)]
                else :
                    s += [1, 1, 1, 0, 0, 0, 0, 0][rd.randint(difficulty-1,7)]
    # play adequate sound effect
    playsound(f"soundeffects/sticks{s}.wav")
    print(s, "sticks removed", end="")
    return n - s

def nim_game(difficulty : int) -> bool :
    """
    Plays the game of nim
    :param difficulty: int representing the difficulty level
    :return: bool representing if the game has been won by the player
    """
    p_turn, sticks = True, 20
    while sticks > 1 :
        # The player and the master alternatively return sticks
        # until only 1 remains
        display_sticks(sticks)
        if p_turn :
            sticks = player_removal(sticks)
            print(" by yourself")
        else :
            sticks = master_removal(sticks, difficulty)
            print(" by the master")
        p_turn = not p_turn
    display_sticks(sticks)
    # if it is the player's turn when there only remains 1 stick, they lose
    if p_turn :
        print("The master has bested you...")
        return False
    print("You have bested the master!!!")
    return True

# Tests

# n = 5
# display_sticks(n)
# n = player_removal(n)
# display_sticks(n)

# n = 10
# while n != 1 :
#     display_sticks(n)
#     n = master_removal(n, 2)
# display_sticks(n)

# print(nim_game(2))

"""BATTLESHIP"""

def battleship_game(difficutly :  int) -> bool :
    """
    Plays the battleship game
    :param difficutly: int representing the difficulty level
    :return: bool representing if the game has been won by the player
    """
    return ...