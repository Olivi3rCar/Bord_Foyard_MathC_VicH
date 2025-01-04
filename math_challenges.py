"""file containing the functions regarding the math challenges"""
import random



def factorial(n) -> int:
    """
    :param n: randomly generated number, ranging from 1 to 10
    :return: int: factorial of n using a for loop
    """
    for i in range (1,n):
        n*=i
    return n

def math_challenge_factorial(diff) -> bool:
    """
    The factorial challenge, that generates a random number, and checks if the user can compute its factorial
    :param diff: difficulty of math challenge, as the user will need to compute a larger factorial as diff increases
    :return: bool: Whether the game is won or not
    """

    #Generates a random number, the intervall is altered by diff, to provide more of a challenge in difficult difficulty
    n=random.randint(3,5)*diff

    #checks if the user's answer is correct
    if int(input("What is the factorial of {} ? ".format(n))) == factorial(n):
        return True
    else:
        return False



def solve_linear_equation(diff)-> bool:
    """
    Linear equation challenge, genereates a linear equation aX+b=0 and expects X as an input to win the game
    :param diff:
    :return: bool: Whether the game is won or not
    """

    #generates 2 random numbers and adds the difficulty variable to them, to provide more of a challenge and increase the probability of a factorial solution (more on that later)
    a=random.randint(1,8)+diff
    b=random.randint(4,12)+diff

    #We check if the answer has more than three decimals, using the split function, if yes, the algorithm excepts a "-b/a" solution, simplified at maximum in a string. If not, it excepts a float solution.
    if len(str(-b / a).split(".")[1]) > 3:
        #Simplifying the fraction by dividing the denominator and numerator again and again by the common factors between a and b

        #Setting the cursor at the lowest number, to optimize the search for common factors
        if a < b:
            k=a
        else:
            k=b

        #searching for common factors in a while loops that stops when k=1, as it means that none were found.
        while k !=1 :
            if a%k==0 and b%k==0:
                a,b=a/k,b/k
                #Setting k as a or b to continue the search
                if a < b:
                    k = a
                else:
                    k = b
            else:
                k=k-1

        if str(input("Solve this equation: {}x+{}=0\nx = ".format(a, b))) == "-{}/{}".format(int(b),int(a)):
            return True

    else:
        if float(input("Solve this equation: {}x+{}=0\nx = ".format(a, b))) == -b / a:
            return True
    return False



def is_prime(n):
    """
    Checks if n is prime by using a for loop
    :return: bool: Whether the number is prime or not
    """
    if n<=1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def nearest_prime(n):
    """
    :return: the closest prime number above n, by repeatedly calling the is_prime function
    """
    k=n
    while True:
        if is_prime(k):
            return k
        k=k+1

def math_challenge_prime(diff):
    """
    Prime challenge, expects the closest prime number to win the game
    :param diff: allows the game to generate a bigger number
    :return: bool: Whether the game is won or not
    """
    n=random.randrange(1,7)^diff
    if int(input("What is the first prime number, greater than {}? ".format(n))) == nearest_prime(n):
        return True



def math_roulette_challenge(diff):
    """
    Generates 5 random numbers and expects the result of the randomly selected operation between them
    :param diff: genereates bigger numbers
    :return: bool: Whether the game is won or not
    """

    #Generating 5 random numbers
    a,b,c,d,e=random.randint(1,7)*diff,random.randint(1,7)*diff,random.randint(1,7)*diff,random.randint(1,7)*diff,random.randint(1,7)*diff

    #Initializing and choosing an operation
    l=['add','sub','mult']
    l_index=random.randint(0,len(l)-1)
    print("Numbers on the roulette: [",a,',',b,',',c,',',d,',',e,"]")

    #If statements to check for the chosen value and checking if the value is correct to allow the player to win the game
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