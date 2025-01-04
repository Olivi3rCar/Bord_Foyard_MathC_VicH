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

# Logbook
## Project chronology
- 6/12/2024 : Project's beginning, GitHub repo setup. Implementation of Fère Pouras' riddles, as well as the utility functions.
- 20/12/2024 : Math challenges are fully implemented, logical challenges are almost done.
- 22/10/2024 : Logical challenges are done
- 28/12/2024 : Chance challenges implementation
- 2/01/2025 : Final challenge and main are implemented
- 4/01/2025 : Documentation is finalized, project is finished

## Task distribution
- Olive / Oliver3rCar : Mathias C: implemented fère pourras' riddles, logical challenges and added sound effects. Redacted half of the documentation.
- Pandadulol : Victor H: implemented chance and math challenges as well as the utility functions and the main. Redacted the other half of the documentation.

#
# Testing and validation
## Test strategies
