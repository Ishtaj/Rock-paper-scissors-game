# importing the necessary libraries
import random
import time
import os


#starting game
time.sleep(1.5)

print ("\n\nStarting game", end = '')
for i in range(3):
    time.sleep(1)
time.sleep(1)

print ("\n\nSetting up environment", end = '')
for i in range(3):
    time.sleep(1)
time.sleep(1)

print ("\n\nInitialising variables", end = '')
for i in range(3):
    time.sleep(1)
time.sleep(1)

#clearing screen
os.system('cls')
time.sleep(1)
os.system('cls')

# Welcome to Game message
print("_________________________________________________\n|\t\t\t\t\t\t|")
print("|\tWELCOME TO ROCK-PAPER-SCISSORS GAME\t|")
print("|_______________________________________________|\n\n")
print("Developed by ISHTAJ KAUR DEOL & SOUMYAJIT ROY\n")
print("---------------------------------------------\n\n")



# function to get input from user
def get_userinput():
    user_input = int(input("\nMake your throw (0 for rock, 1 for paper, 2 for scissors):"));

    if user_input == 0:
        print("\nYou threw rock")
    elif user_input == 1:
        print("\nYou threw paper")
    elif user_input == 2:
        print("\nYou threw scissors")

    return user_input



# function to get computer selection
def computer_input():
    comp_input = random.randint(0, 2)

    if comp_input == 0:
        print("Computer threw rock")
    elif comp_input == 1:
        print("Computer threw paper")
    elif comp_input == 2:
        print("Computer threw scissors")

    return comp_input



# function to determine winner for each round and returns 0 if tie, 1 if user wins and -1 if computer wins
def winner(user, computer):

    if user == computer:
        print("\nRound tied!")
        return 0

    elif user == 0:
        if computer == 1:
            print ("\nPaper covers Rock --- You lose :(\n")
            return -1 
        elif computer == 2:
            print ("\nRock smashes Scissors --- You win!\n")
            return 1
    
    elif user == 1:
        if computer == 0:
            print ("\nPaper covers Rock --- You win!\n")
            return 1
        elif computer == 2:
            print ("\nScissors cut Paper --- You lose :(\n")
            return -1

    elif user == 2:
        if computer == 0:
            print ("\nRock smashes Scissors --- You lose :(\n")
            return -1
        elif computer == 1:
            print ("\nScissors cut Paper --- You win!\n")
            return 1


# global variables to keep track of score
user_score = 0
comp_score = 0
rounds = 0


# driver code
while True:

    choices = [0,1,2]

    # checking validity of user input
    user_choice = get_userinput()
    if (user_choice not in choices):
        print ("\nInvalid input... Please make your throw again\n\n")
        user_choice = get_userinput()


    comp_choice = computer_input()

    win = winner(user_choice, comp_choice)

    # keeping track of scorecard and updating it
    if (win == 0):
        rounds = rounds + 1
    elif (win == 1):
        user_score = user_score + 1
        rounds = rounds + 1
    elif (win == -1):
        comp_score = comp_score + 1
        rounds = rounds + 1


    # asking user if he/she wants to play another round
    playagain = input ("\nDo you want to play another round? (y/n): ")
    if playagain.lower() == "y":
        continue
    elif playagain.lower() == 'n':

        #displaying final score
        print("\n\n\n******** FINAL SCORE ********\n")
        print("Your score:\t\t", user_score)
        print("Computer's score:\t", comp_score)
        print("No. of rounds:\t\t", rounds)

        if (user_score == comp_score):
            print("\n\nGAME TIED!\n")
        elif (user_score > comp_score):
            print("\n\nYOU WON THE GAME!\n")
        else:
            print("\n\nYou lost the game... Better luck next time!\n")

        print ("******************************\n")


        for i in range (5, -1, -1):
            print("Terminating game in", i, "seconds", end = '\r')
            time.sleep(1)
        break
    
    else:
        print("\n\nInvalid input...\n")
        for i in range (5, -1, -1):
            print("Terminating game in", i, "seconds", end = '\r')
            time.sleep(1)
        break
