"""file containing utility functions"""

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
    print("Welcome to Bord Foyard.\n Your goal is to collect three keys to partake in the final challenge and have a chance to unlock the treasure room.")


def compose_equipe() -> list:
    """

    :return: team_list, including players name, professions and whether they are the leader or not
    """

    """Initialisation of the team list that is going to contain all of the player's info"""
    team=[]
    team_size=int(input('\n \n Please enter the number of players in your team (max 3) : '))
    while not(1<=team_size<=3):
        team_size=int(input("\n The size entered is not valid.\n \n Please enter the number of players in your team (max 3) : "))

    """Filling up the team list with inputs coming from the user"""
    cardinals=["first", "second", "third"]

    """Initializing the leader check"""
    leader_in_team=False

    for i in range(team_size):
        team.append({})
        team[i]["name"]=str(input("Enter the {} player's name : ".format(cardinals[i])))
        team[i]["profession"]=str(input("Enter the {} player's profession : ".format(cardinals[i])))
        if not leader_in_team:
            team[i]["role"]=str(input("Enter the role of the player (Leader or Member) : "))
            while team[i]["role"]!="Leader" and team[i]["role"]!="Member":
                team[i]["role"]=str(input("INVALID INPUT\nEnter the role of the player (Leader or Member) : "))
            if team[i]["role"]=='Leader':
                leader_in_team=True
        else:
            team[i]["role"] ="Member"

        team[i]["keys_wons"]=0

    """When there is no leader, the first player will be selected to be one"""
    for i in range (team_size):
        if team[i]["role"]=="Leader":
            print(team)
            return team
    team[0]["role"]="Leader"
    print(team)
    return team

"""Next, the challenges_menu that will print the available challenges and ask the player to choose one."""

def challenges_menu(available_challenges)->int:
    """
    :param available_challenges: list of the  challenges
    :return: choice: the challenge the user chose
    """
    print("Here are the available challenges: ")
    for i in available_challenges:
        print("{}. - {}".format(i,available_challenges[i]))

    choice = int(input('Enter the number of the chosen challenge: '))
    return choice


def choose_player(team)->int:
    """
    Using the dict to display the players and their details
    :return: chosen_one :the chosen player to partake in the challenge and their information
    """

    print("Here are the players in your team: ")
    for i in team:
        print("{}. {} ({}) - {}".format(i,team[i]["name"], team[i]["profession"], team[i]["role"]))
    chosen_one = int(input("Enter the number of the chosen player: "))

    return chosen_one

def choose_difficulty()->int:
    """
    Asks the user what difficulty they want to choose
    :return: Integer corresponding to chosen difficulty
    """
    diff=int(input("1-Easy\n2-Standard\n3-Hard\nEnter the number of the chosen difficulty : "))
    return diff