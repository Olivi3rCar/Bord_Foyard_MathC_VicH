# Bord Foyard - The Challenge of Fère Pouras

## Contributors :

- Victor HAFLIGER
- Mathias CARVALHO

## Description :

Engage as a team to unveil the mysteries and solve the puzzles inside
Fère Pouras' Lair : Bord Foyard !

## Key Features :

- Play a variety of minigames to win keys for the final challenge
- Solve a puzzle for the final challenge

####  Exclusive features :

- Play sound effects for many of the events 
- Choose your difficulty between 3 settings (Easy, Medium, HARD 💀)

# Technologies used

- Python Programming language, as well as JSON for data storage/exploitation
- random, time, os, json and playsound libraries
- Pycharm and Git/GitHub for project management

# Installation :

- Download the project by clicking on code → download zip on 
[This Page](https://github.com/Olivi3rCar/Bord_Foyard_MathC_VicH)
- Extract the ZIP file into an intent folder
- If all modules (Time, Random, json, playsound) are not downloaded :
  - execute the requirements.sh file present in the folder in GIT

# How to use :
- Launch the main.py file in the terminal
- Follow instructions given by the program to begin your game
- Enjoy !

# Technical Presentation
## Game algorithm
1) Importation of all the necessary modules and function for the main program
2) We define the main function that we will use to run the game.
3) We run the introdution function, which presents the game
4) We create the team of players
5) The user enters their prefered difficulty
6) We create the challenges dict, whose goal is to help us display the available challenges
7) We create lists containing the functions relative to each challenge then store them all in another list
8) We reset the number of keys to enter a while loops, which stops when the user has 3 keys
9) The user chooses a type of challenge from the diplayed list (that is coming from a dictionnary)
10) The user chooses a player to undertake the callenge
11) If the user chose a logical challenge, they can choose which one they want to do. If not, the challenge is chosen at random.
12) The user plays the challenge, if they win, they get a key.
13) The loop starts again, unless the user has 3 keys, in which case they undertake the final challenge, where they must find the secret word guarding Fère Pouras' treasure.
14) Whether they win or lose, the player is invited to try again by pressing R, which will start the game function one more time.

## Functions
#### math_challenge(math_challenges_list)
returns and executes the function relative to the randomly chosen math challenge, using the random library with randint

###
#### factorial(n)
computes and returns the factorial of n, using a for loop starting from n and decreasing by 1 until the counter reaches 1

###
#### math_challenge_factorial(diff)
computes a random number multiplied by diff and check whether the player's guess is the same as the result of the factorial of n

###
#### solve_linear_equation(diff)
computes 2 random integer "a" and "b" and adds the difficulty number to them
then, the function checks how many decimals b/a has
if it has 3 or fewer decimals, the game expects a decimal answer for the equation
if it has more than 3 decimals, the game expects a fractional answer ("-b/a")

###
#### is_prime(n)
returns True if n is prime and False if not, we verify this using a for loop, decreasing by 1 until it reaches 1

###
#### nearest_prime(n)
returns n's nearest prime above him, using a while loop and increasing n by 1 each time the prime check (utilising is_prime()) fails

###
#### math_challenge_prime(diff)
computes a random n using randrange and putting it to the power of the difficulty number.
the game then checks if the player's answer is correct using the previous function.

###
#### math_roulette_challenge(diff)
computes 5 random numbers, then chooses at random between addition, substraction or product
checks if the user's input is the same as the result of the calculation between the five numbers

#
# Input and error management 