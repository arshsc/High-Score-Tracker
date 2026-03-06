#Import all used functions
from helper import *
from accounts_arsh import *
from investments import invest
from b_games import *
from flesh_cube_two import *
from score import *
from rememberinator import run
from password import *
from accounts_arsh import *
b = '\033[34m'
r = '\033[0m'
#main menu function:
def menu():
	print('\033c', end='')
	#Welcome them to the gaming hub
	print('Welcome to the gaming hub!')
	input('\033[32mPress ENTER to begin > \033[0m')
	check = choice_input(["yes", "y", "no", "n"], "Do you have an account? ")
	if check in ["yes","y"]: user = user_sign_in()
	else: user = user_creator()
	#Loop forever:
	while True:
		#Display “MAIN MENU”
		print('\033[30m###\033[0m MAIN MENU \033[30m###\033[0m')
		#Ask user if they want to play a game, view a user, or log out
		choice = choice_input(['1','2','3'],f'Please choose an option: \n{b}1{r} Play a Game\n{b}2{r} View a User\n{b}3{r} Log Out\n> ')
		match choice:
			#if they chose to play a game:
			case '1':
				#Ask them what game they want to play
				games = ['','flesh cube','guesser bros lite','remembrinator','turtarria','the bank','rock paper scissors']
				game = choice_input(['1','2','3','4','5','6'],f'What game do you want to play?{b}\n1{r} Flesh Cube{b}\n2{r} Guesser Bros Lite{b}\n3{r} Rememberinator{b}\n4{r} Turtarria{b}\n5{r} The Bank{b}\n6{r} Rock Paper Scissors\n> ')
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
				score_recorder(user,games[int(game)],user_score)
				print(f'High scores for {games[int(game)]}:')
				#retrieve respective high score data
				high_score_collective(games[int(game)])
				#run functions in high score tracking
			#if they chose to view a user:
			case '2':
				#ask them what user to view
				username = u_input('What user do you want to view?\n> ')
				#if that user exists:
				valid_user, user_data= False,False#check_usernames(user)
				accounts = csv_to_dictionary("docs/accounts.csv")
				for i in accounts:
					if i["username"] == username:
						valid_user = True
				if valid_user:
					#retrieve user data (accounts)
					file = csv_to_dictionary("docs/high_scores.csv")
					for i in file:
						if i["user"] == username:
							user_data = i
					#if there is no data:
					if not user_data:
						#tell the user
						print('No high score data for given user!')
					#otherwise:
					else:
						#uniprint it
						uniprint(user_data)
				#otherwise:
				else:
					#tell them that user doesn’t exist
					print('That user does not exist!')
			case '3':
			#if they chose to log out:
				#set logged in to false (accounts)
				accounts = csv_to_dictionary("docs/accounts.csv")
				for i in accounts:
					if user == i["username"]:
						i["logged in"] = False
						save_csv(accounts, "docs/accounts.csv")
						#exit function
						return
				
			#take a user input telling them to press enter to continue
		input('\033[32mPress ENTER to continue > \033[0m')
		#clear screen
		print('\033c', end='')

menu()
