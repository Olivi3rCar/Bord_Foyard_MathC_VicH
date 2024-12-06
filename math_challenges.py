"""file containing the functions regarding the math challenges"""
import random

from utility_functions import choose_difficulty


def math_challenge():
    """
    :return:challenge:returns the randomly chosen challenge
    """
    return random.randint(1, 4)

def factorial(n):
    """
    :param n: randomly generated number, ranging from 1 to 10
    :return: n!
    """
    for i in range (1,n):
        n*=i
    return n

def math_challenge_factorial(team,chosen_one):
    diff=choose_difficulty()
    if diff==1:
        n=random.randint(3,5)
    elif diff==2:
        n=random.randint(6,9)
    else:
        n=random.randint(10,12)
    if int(input("What is the factorial of {} ? ".format(n))):
        print("Correct ! You win a key !")
        team[chosen_one]["keys_won"] += 1
    else:
        print("Wrong ! The key disappears.")


