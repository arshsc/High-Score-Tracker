#Import all used functions
from helper import *
#from accounts_arsh import *
from investments import invest
from b_games import *
from flesh_cube_two import *
from score import *
from rememberinator import run
from password import *
from accounts_arsh import *
#main menu function:
def menu():
	#Welcome them to the gaming hub
	print('Welcome to the gaming hub!')
	input('\033[32mPress ENTER to begin > \033[0m')
	check = choice_input(["yes", "no"], "Do you have an account? ")
	if check == "yes": user = user_sign_in()
	else: user = user_creator()
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
				games = ['','flesh cube','rememberinator','guesser bros lite','turtarria','the bank','rock paper scissors']
				game = choice_input(['1','2','3','4','5','6'],'What game do you want to play?\n1. Flesh Cube\n2. rememberinator\n3. Guesser Bros Lite\n4. Turtarria\n5. The Bank\n6. Rock Paper Scissors\n> ')
				#call respective game function
				match game:
					case '1':
						user_score = runFleshCubeII(0)
					case '2':
						user_score = guesser_bros_lite()
					case '3':
						user_score = run()
					case '4':
						user_score = tuterria()
					case '5':
						user_score = invest()
					case '6':
						user_score = rock_paper_scissors()
				print(f'Your score was {user_score}!')
				#score_recorder(user,games[int(game)],user_score)
				#retrieve respective high score data
				high_score_collective(games[int(game)])
				#run functions in high score tracking
			#if they chose to view a user:
			case '2':
				#ask them what user to view
				user = u_input('What user do you want to view?\n> ')
				#if that user exists:
				valid_user, user_data= False,False#check_usernames(user)
				if valid_user:
					#retrieve user data (accounts)
					#uniprint it
					uniprint(user_data)
				#otherwise:
				else:
					#tell them that user doesn’t exist
					print('That user does not exist!')
			case '3':
			#if they chose to log out:
				#set logged in to false (accounts)
				for i in accounts:
					if user == accounts[i]["username"]:
						account[i]["logged in"] = False
						save_csv(account, "docs/accounts.csv")
				#exit function
				break
			#take a user input telling them to press enter to continue
		input('\033[32mPress ENTER to continue > \033[0m')
		#clear screen
		print('\033c', end='')
