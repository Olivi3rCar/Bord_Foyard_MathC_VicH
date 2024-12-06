"""file containing the functions regarding the riddle challenges"""

#imports
from random import choice
from json import load
from time import sleep
from playsound import playsound

from utility_functions import lowercase

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
    # n is dependent on the difficulty level
    attempts = [5, 3, 1][difficulty - 1]
    while attempts > 0 :
        # attempt to answer
        answer = input("Answer, if you dare... ")
        # intense sound effect is played
        playsound(f"soundeffects/intense{6 - attempts}.wav")
        if lowercase(answer) == lowercase(r['answer']) :
            # case for correct answer : return true
            print("Correct! You snatched the key from Fère Pouras!")
            sleep(2)
            return True
        elif attempts > 1 :
            # case for incorrect answer and more than 1 attempts left
            attempts -= 1
            print(f"Incorrect answer, try again... You have {attempts} attempts left!")
            sleep(2)
        else :
            # case for incorrect answer and no attempts left
            print("Incorrect, you lost! the correct answer was : " + r['answer'])
            sleep(2)
            return False

# # TEST
# pere_fouras_riddles(2)