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
    for i in range(team_size):
        team.append({})
        team[i]["name"]=str(input("Enter the {} player's name : ".format(cardinals[i])))
        team[i]["profession"]=str(input("Enter the {} player's profession : ".format(cardinals[i])))
        team[i]["role"]=str(input("Enter the role of the player (Leader or Member) : "))
        while team[i]["role"]!="Leader" or team[i]["role"]!="Member":
            team[i]["role"]=str(input("INVALID INPUT\nEnter the role of the player (Leader or Member) : "))
        team[0]["keys_wons"]=0

    """When there is no leader, the first player will be selected to be one"""
    if (team[0]["role"]!="Leader") and (team[1]["role"]!="Leader") and (team[2]["role"]!="Leader"):
        team[0]["role"]="Leader"
    return team