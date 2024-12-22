"""file containing the functions regarding the logical challenges"""

# imports
import random as rd
from random import randint
from time import sleep
from playsound import playsound

"""functions"""

def minimum(a : int, b : int) -> int :
    """
    :param a: integer 1
    :param b: integer 2
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
    then removes this number of sticks
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

def next_player(n : int) -> int :
    """
    changes the player index to the next player
    :param n: current player index (0 : Player, 1 : Master)
    :return: next player index
    """
    return int(not bool(n))

def empty_grid(d : int) -> list :
    """
    generates the empty grid of dimensions dxd
    :param d: dimensions of the grid
    :return: matrix representing the empty grid
    """
    return [[" " for _ in range(d)] for _ in range(d)]

def display_grid(grid : list, msg : str) -> None:
    """
    displays the grid accompanied by an intent message
    :param grid: current state of the grid
    :param msg: message to be displayed before displaying the grid
    """
    print(msg)
    sleep(1)
    # The display of the grid also displays the positions of each square in the grid
    print(' ' + ''.join([f'  {i+1} ' for i in range(len(grid))]))
    for i in range(len(grid)) :
        print(' ' + '----'*len(grid) + '-')
        print(f"{i+1}| " + ' | '.join(grid[i]) + ' |')
    print(' ' + '----'*len(grid) + '-')

def ask_position(grid : list) -> tuple :
    """
    prompts the user to input a position and returns it if valid
    :param grid: current state of the grid
    :return: tuple of position (x,y)
    """
    x, y = -1, -1
    # Asks the user for horizontal position as long as given one is not valid
    while x not in (range(1, len(grid) + 1)):
        x = int(input(f"Enter horizontal position (1 -> {len(grid)}) : "))

    # same for vertical pos
    while y not in (range(1, len(grid) + 1)):
        y = int(input(f"Enter vertical position (1 -> {len(grid)}) : "))
    return y, x

def initialize(difficulty : int) -> list :
    """
    Initializes the player's grid with
    a board size and number of boats depending on the difficulty level
    :param difficulty: int representing the difficulty level (1-2-3)
    :return: the initialized player grid
    """
    # possible grid sizes and number of boats depending on difficulty
    pgs, pbn = [3, 4, 5], [2, 4, 6]
    # create the grid
    grid = empty_grid(pgs[difficulty - 1])
    # place the boats
    display_grid(grid, f"Place boat #1 of {pbn[difficulty - 1]}")
    pos = ask_position(grid)
    grid[pos[0] - 1][pos[1] - 1] = "B"
    print("Boat placed !")
    playsound("soundeffects/splash.wav")
    for i in range(1, pbn[difficulty - 1]) :
        display_grid(grid, f"Place boat #{i+1} of {pbn[difficulty - 1]}")
        s = False
        # verify there isn't already a boat on chosen cell
        while grid[pos[0] - 1][pos[1] - 1] != " " :
            if s :
                print("There is already a boat on this position !")
            else :
                s = not s
            pos = ask_position(grid)
        grid[pos[0] - 1][pos[1] - 1] = "B"
        print("Boat placed !")
        playsound("soundeffects/splash.wav")
    return grid

def init_master(difficulty : int) -> list :
    """
    Automatically initializes the master's grid
    :param difficulty: int representing the difficulty level (1-2-3)
    :return: the initialized master grid
    """
    # possible grid sizes and number of boats depending on difficulty
    pgs, pbn = [3, 4, 5], [2, 4, 6]
    # create the grid
    grid = empty_grid(pgs[difficulty - 1])
    # place the boats
    pos = (randint(1, len(grid)), randint(1, len(grid)))
    grid[pos[0] - 1][pos[1] - 1] = "B"
    for i in range(1, pbn[difficulty - 1]):
        # verify there isn't already a boat on chosen cell
        while grid[pos[0] - 1][pos[1] - 1] != " ":
            pos = (randint(1, len(grid)), randint(1, len(grid)))
        grid[pos[0] - 1][pos[1] - 1] = "B"
    return grid

def turn(player : int, player_shots_grid : list, opponent_grid : list) -> None :
    display_grid(player_shots_grid, "Here are the shots you took..."
                                    "Were do you want to shoot now ?")
    if player == 0 :
        # Ask the player where to shoot when it's his turn
        pos = ask_position(player_shots_grid)
        while player_shots_grid[pos[0] - 1][pos[1] - 1] != " " :
            # Verify the player's not already shot here
            print("You have already shot there !")
            pos = ask_position(player_shots_grid)
    else :
        sleep(2)
        # Takes a random position when it's the master's turn
        pos = (randint(1, len(player_shots_grid)), randint(1, len(player_shots_grid)))
        while player_shots_grid[pos[0] - 1][pos[1] - 1] != " " :
            # Verify the master's not already shot here
            pos = (randint(1, len(player_shots_grid)), randint(1, len(player_shots_grid)))
    # add suspense
    print("Did you hit ?")
    playsound("soundeffects/cannonball.wav")
    if opponent_grid[pos[0] - 1][pos[1] - 1] == "B" :
        print("You hit them !")
        # play adequate sound effect
        playsound("soundeffects/hit.wav")
        player_shots_grid[pos[0] - 1][pos[1] - 1] = "X"
        opponent_grid[pos[0] - 1][pos[1] - 1] = "X"
    else :
        print("You missed them !")
        # play adequate sound effect
        playsound("soundeffects/miss.wav")
        player_shots_grid[pos[0] - 1][pos[1] - 1] = "."

def has_won(player_shots_grid : list, difficulty) -> bool :
    """
    Returns boolean representing if the player has won
    :param player_shots_grid: grid of shots taken by the player
    :param difficulty: int representing the difficulty level (1-2-3)
    :return: bool representing if the player has won
    """
    # Set max number of boats depending on difficulty level
    m = [2, 4, 6][difficulty - 1]
    s = 0
    for i in player_shots_grid :
        for j in i :
            if j == "X" :
                s += 1
    return s == m

def battleship_game(difficulty :  int) -> bool :
    """
    Plays the battleship game
    :param difficulty: int representing the difficulty level
    :return: bool representing if the game has been won by the player
    """
    # Welcoming messages
    print("Welcome to Battleship, sailor!")
    sleep(1)
    print("Here, you will have to manage to sink all of your opponent's boats,\nwithout having your fleet sunken !")
    sleep(3)
    dimensions, boat_nbr = [3, 4, 5][difficulty - 1], [2, 4, 6][difficulty - 1]
    print("With a difficulty level of", difficulty, "you will both have to place")
    print(boat_nbr, "boats in a", dimensions, "by", dimensions, "grid.")
    sleep(3)
    # grids initialisations
    print("Well then, place your ships !")
    sleep(1)
    player_grid = initialize(difficulty)
    display_grid(player_grid, "Here is your grid !")
    sleep(3)
    print("The master has placed their ships too !")
    sleep(2)
    master_grid = init_master(difficulty)
    player_shots, master_shots = empty_grid(dimensions), empty_grid(dimensions)
    # begin the turns with the player (index 0)
    curr_player = 0
    v = False
    while not v :
        if curr_player == 0 :
            # Time for the player to play
            print("Time for you to play !")
            playsound("soundeffects/bsplayer.wav")
            sleep(1)
            turn(curr_player, player_shots, master_grid)
            if has_won(player_shots, difficulty) :
                # player has won : stop the game
                print("You won the battle, sailor!")
                return True
        else :
            # Time for the master to play
            print("Time for the master to play !")
            playsound("soundeffects/bsmaster.wav")
            sleep(1)
            turn(curr_player, master_shots, player_grid)
            if has_won(master_shots, difficulty) :
                # master has won : stop the game
                print("You lost the battle, sailor...")
                return False
        curr_player = next_player(curr_player)

# tests :

# print(next_player(0), next_player(1))

# display_grid(empty_grid(3), "This is a test!")
# display_grid(empty_grid(5), "This is another test!")

# print(ask_position(empty_grid(3)))

# display_grid(initialize(2), "yet another test...")

# print(battleship_game(2))