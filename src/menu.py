#Import all used functions
from helper import *
#main menu function:
def menu():
	#Welcome them to the gaming hub
	print('Welcome to the gaming hub!')
	input('\033[32mPress ENTER to begin > \033[0m')
	#Loop forever:
	while True:
		#Display “MAIN MENU”
		print('\033[30m###\033[0m MAIN MENU \033[30m###\033[0m')
		#Ask user if they want to play a game, view a user, or log out
		choice = choice_input(['1','2','3'],'Please choose an option: \n1. Play a Game\n2. View a User\n3. Log Out\n> ')
		match choice:
			#if they chose to play a game:
			case '1':
				#Ask them what game they want to play
				game = choice_input(['1','2','3','4','5'],'What game do you want to play?\n1. Flesh Cube\n2. Memory Game\n3. Turtarria\n4. The Bank\n5. Rock Paper Scissors\n> ')
				#call respective game function
				#retrieve respective high score data
				#run functions in high score tracking
			#if they chose to view a user:
			case '2':
				#ask them what user to view
				user = u_input('What user do you want to view?\n> ')
				#if that user exists:
				#retrieve user data (accounts)
				#uniprint it
			#otherwise:
				#tell them that user doesn’t exist
			case '3':
			#if they chose to log out:
				#set logged in to false (accounts)
				#exit function
				break
			#take a user input telling them to press enter to continue
		input('\033[32mPress ENTER to continue > \033[0m')
		#clear screen
		print('\033c', end='')
            
menu()