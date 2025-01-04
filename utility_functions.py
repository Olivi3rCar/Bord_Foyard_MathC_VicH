"""file containing utility functions"""
from time import sleep

def lowercase(s : str) -> str :
    """
    Returns the lowercase version of a string
    :param s: string to be lowercased
    :return: lowercase version of the string
    """
    # instantiation of string to be returned
    ns = ""
    # iteration over s
    for c in s:
        # test of position of current char relative to uppercase bounds (A & Z)
        if ord('A') <= ord(c) <= ord('Z'):
            # concatenation of lowercase-converted current char to string
            ns += chr(ord(c) + (ord('a') - ord('A')))
        else :
            # concatenation of current car to string
            ns += c
    return ns

def introduction():
    print("Welcome to Bord Foyard !\n")
    sleep(1)
    print("In this magical and mysterious castle, \
you will face numerous challenges in an attempt to steal Fère Pouras' gold\n")
    sleep(3)
    print("But before entering the Fère's lair, you will have to choose a difficulty level\
and compose a team of 3 players.")


def compose_team() -> list:
    """
    :return: team_list, including players name, professions and whether they are the leader or not
    """

    """Initialisation of the team list that is going to contain all of the player's info"""
    team=[]
    team_size=int(input('\n\nPlease enter the number of players in your team (max 3) : '))
    while not(1<=team_size<=3):
        team_size=int(input("\nThe size entered is not valid.\n\n\
Please enter the number of players in your team (max 3) : "))

    """Filling up the team list with inputs coming from the user"""
    cardinals=["first", "second", "third"]
    v = False # variable used to keep track if leader role has already been assigned
    for i in range(team_size):
        team.append({})
        team[i]["name"]=str(input(f"Enter the {cardinals[i]} player's name : "))
        team[i]["profession"]=str(input(f"Enter the {cardinals[i]} player's profession : "))
        if not v :
            # if we don't have a leader already
            team[i]["role"]=str(input("Enter the role of the player (Leader or Member) : "))
            while team[i]["role"] != "Leader" and team[i]["role"] != "Member":
                team[i]["role"]=str(input("INVALID INPUT\nEnter the role of the player (Leader or Member) : "))
            if team[i]["role"] == "Leader":
                # if the player is defined as leader, change state of v
                v = True
        else :
            # if we already have a leader, set current player as member
            team[i]["role"] = "Member"
        team[i]["keys_wons"]=0

    """When there is no leader, the first player will be selected to be one"""
    if not v :
        team[0]["role"]="Leader"
    return team

"""Next, the challenges_menu that will print the available challenges and ask the player to choose one."""

def challenges_menu(available_challenges)->int:
    """
    :param available_challenges: dict of the available challenges
    :return: choice: the challenge the user chose
    """
    print("\nHere are the available challenges: ")
    #displays the available challenges, using a for loop and the dictionnary's keys
    for i in available_challenges:
        print("{}. - {}".format(i,available_challenges[i]))

    #the user enters a number, which is associated with a challenge
    choice = int(input('Enter the number of the chosen challenge: '))
    while 1<=choice<=4:
        choice = int(input('Invalid input, Enter the number of the chosen challenge: '))
    return choice


def choose_player(team : list)->int:
    """
    Using the list to display the players and their details
    :return: chosen_one :the index of chosen player to partake in the challenge
    """

    print("Here are the players in your team: ")
    for i in range(len(team)):
        print("{}. {} ({}) - {}".format(i+1,team[i]["name"], team[i]["profession"], team[i]["role"]))
    chosen_one = -1

    #asking the user for a number between 1 and the size of the team
    while not chosen_one - 1 in range(len(team)):
        chosen_one = int(input("Enter the number of the chosen player: "))

    return chosen_one - 1

def choose_difficulty()->int:
    """
    Asks the user what difficulty they want to choose
    :return: Integer corresponding to chosen difficulty
    """
    diff = -1
    #asking the user for a number between 1 and 3
    while not 1 <= diff <= 3 :
        diff=int(input("\n1-Easy\n2-Standard\n3-Hard\n\nEnter the number of the chosen difficulty : "))
    return diff