
"""file containing the functions regarding the math challenges"""


import random

def math_challenge(math_challenges_list):
    """
    :return:challenge: returns and executes the function relative to the randomly chosen challenge
    """
    return math_challenges_list[random.randint(0, len(math_challenges_list) - 1)]

def factorial(n):
    """
    :param n: randomly generated number, ranging from 1 to 10
    :return: n!
    """
    for i in range (1,n):
        n*=i
    return n

def math_challenge_factorial(diff):
    
    n=random.randint(3,5)*diff
    #
    #
    #
    if int(input("What is the factorial of {} ? ".format(n))) == factorial(n):
        return True
    else:
        return False

def solve_linear_equation(diff):
    
    a=random.randint(1,8)*diff
    b=random.randint(4,12)*diff

    if int(input("Solve this equation: {}x+{}=0\nx = ".format(a,b)))==-b/a:
        return True
    else:
        return False


def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def nearest_prime(n):
    k=n
    while True:
        if is_prime(k):
            return k
        k=k+1

def math_challenge_prime(diff):
    n=random.randint(2,6)^diff
    if int(input("What is the first prime number, greater than {}? ".format(n))) == nearest_prime(n):
        return True


def math_roulette_challenge(diff):
    a,b,c,d,e=random.randint(1,7)*diff,random.randint(1,7)*diff,random.randint(1,7)*diff,random.randint(1,7)*diff,random.randint(1,7)*diff
    l=['add','sub','mult']
    l_index=random.randint(0,len(l)-1)
    print("Numbers on the roulette: [",a,b,c,d,e,"]")
    if l[l_index]=='add':
        if int(input("What is the sum of the numbers on the roulette?\nYour answer : "))==a+b+c+d+e:
            return True
    elif l[l_index]=='sub':
        if int(input("What is the difference of the numbers on the roulette?\nYour answer : "))==a-b-c-d-e:
            return True
    else:
        if int(input("What is the product of the numbers on the roulette?\nYour answer : "))==a*b*c*d*e:
            return True
    return False