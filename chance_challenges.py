"""file containing the functions regarding the chance challenges"""

import random as rd

def shell_game(diff) -> bool:
    """
    :param diff: the difficulty will correspond to the number of attempts the player can make before failing
    :return: bool : returns whether the game is won or not
    """

    shells=['A','B','C']
    attempts = 4-diff
    print("In this game of shells, you will have to find in which shell the key is, you have {} tries.\n".format(attempts))
    while attempts > 0:
        computer_choice = rd.choice(shells)
        player_choice=str(input("A     B     C\n\nMake your choice : "))
        while (player_choice not in shells) and (chr(ord(player_choice)-32) not in shells):
            player_choice = str(input("Invalid input\nA     B     C\n\nMake your choice : "))

        if computer_choice == player_choice or computer_choice == chr(ord(player_choice)-32):
            return True
        else:
            attempts -= 1
            print(" You have {} attempts left.\n".format(attempts))

    print("You lose the key.")
    return False



def roll_dice_game(diff) -> bool:
    """
    :param diff: the difficulty will correspond to the number of attempts the player can make before automatically failing
    :return: bool: returns whether the game is won or not
    """

    attempts = 5-diff
    print("In this game, you will roll a dice twice and check if you rolled a 6, if not, you will give it to the game master who will also try to roll a 6. The first to roll a 6 in {} attempts wins".format(attempts))
    while attempts > 0:
        str(input("Press enter to roll the dice!\n"))
        player_dice= rd.randint(1,6),rd.randint(1,6)
        print(player_dice)
        if 6 in player_dice:
            print("You win ! You take the key.")
            return True
        else:
            print("No 6 ! It's the master's turn.")

        master_dice = rd.randint(1,6),rd.randint(1,6)
        print(master_dice)
        if 6 in master_dice:
            print("The game master has won, you lose the key.")
            return False
        else:
            print("No 6 ! It's the master's turn.")

        attempts -= 1
        print(" You have {} attempts left.\n".format(attempts))

    print("Nobody rolled a 6, the game ends in a draw! You lose the key.")
    return False