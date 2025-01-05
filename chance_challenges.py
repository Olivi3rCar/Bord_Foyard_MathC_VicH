"""file containing the functions regarding the chance challenges"""

import random as rd

def shell_game(diff) -> bool:
    """
    :param diff: the difficulty will correspond to the number of attempts the player can make before failing, ranging from 1 to 3
    :return: bool : returns whether the game is won or not
    """

    #Shells initialization, its size depends on the difficulty
    shells=[]
    for i in range(diff+1):
        shells.append(chr(65+i))

    print("In this game of shells, you will have to find in which shell the key is.")

    #for loop to allow to perform multiple tries, with 2 tries
    for attempts in range (2):
        print(" You have {} attempts left.\n".format(2-attempts))

        #Randomly choosing a shell
        computer_choice = rd.choice(shells)
        for i in shells:
            print(i, end='    ')
        player_choice=str(input("\n\nMake your choice : "))

        #checking the validity of the player's answer, then checking if it is good or not
        while (player_choice not in shells) and (chr(ord(player_choice)-32) not in shells):
            player_choice = str(input("Invalid input\n\nMake your choice : "))

        if computer_choice == player_choice or computer_choice == chr(ord(player_choice)-32):
            return True

    return False



def roll_dice_game(diff) -> bool:
    """
    :param diff: the difficulty will correspond to the number of attempts the player can make before automatically failing, ranging from 2 to 4
    :return: bool: returns whether the game is won or not
    """

    print("In this game, you will roll a dice twice and check if you rolled a 6, if not, you will give it to the game master who will also try to roll a 6. The first to roll a 6 in {} attempts wins".format(5-diff))

    #for loop keeping track of the number of attempts of the player
    for attempts in range(5-diff):
        str(input("Press enter to roll the dice!\n"))

        #Generating a tuple, with 2 random values, each one ranging from 1 to 6, if a 6 is obtained, the player wins
        player_dice= rd.randint(1,6),rd.randint(1,6)
        print(player_dice)
        if 6 in player_dice:
            print("You win !.")
            return True
        else:
            print("No 6 ! It's the master's turn.")

        #Generating a tuple, with 2 random values, each one ranging from 1 to 6, if a 6 is obtained, the game master wins and the player automatically loses
        master_dice = rd.randint(1,6),rd.randint(1,6)
        print(master_dice)
        if 6 in master_dice:
            print("The game master has won.")
            return False
        else:
            print("No 6 ! It's the master's turn.")

        print(" You have {} attempts left.\n".format(5-diff-attempts))

    #If the number of tries is exceeded, the game ends in a draw and the key is lost
    print("Nobody rolled a 6, the game ends in a draw!")
    return False