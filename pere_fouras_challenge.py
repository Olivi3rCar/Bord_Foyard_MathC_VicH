"""file containing the functions regarding the riddle challenges"""

#imports
from random import choice
from json import load
from time import sleep

"""Functions"""
def load_riddles(file : str) -> list :
    """
    Loads the riddles from a JSON file into a list of dictionaries.
    :param file: path to the JSON file
    :return: list of riddle dictionaries
    """
    with open(file, "r") as f:
        #here the conversion of elts from json to list of dictionnary
        data = load(f)
        f.close()
    return data

def display_question(q : str) -> None :
    """
    Displays a question on the screen, using sleep for a more paced effect.
    :param q: question to display
    """
    for i in q.split('\n') :
        print(i)
        sleep(2)

def pere_fouras_riddles(difficulty : int) -> bool :
    """
    Simulates an encounter with Fère Pouras :\n
    Begin a Riddle then allow the user to try 3 times
    :param difficulty: difficulty level (1 to 3)
    :return: Boolean that states if the riddle was won
    """

    # instantiation of the list of riddle dicts using load_riddles
    riddles = load_riddles("Data/PFRiddles.json")
    # random selection of a riddle from the list
    r = choice(riddles)

    # display of the question using display_question
    display_question(r['question'])

    # we begin the tries : number of attempts starts at n
    # n is dependant of the difficulty level!
    attempts = [5, 3, 1][difficulty - 1]

pere_fouras_riddles(2)