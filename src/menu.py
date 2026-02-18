#Import all used functions
#main menu function:
#Welcome them to the gaming hub
#Loop forever:
	#Display “MAIN MENU”
	#Ask user if they want to play a game, view a user, or log out
	#if they chose to play a game:
		#Ask them what game they want to play
		#call respective game function
		#retrieve respective high score data
		#run functions in high score tracking
	#if they chose to view a user:
		#ask them what user to view
		#if that user exists:
		#retrieve user data (accounts)
		#uniprint it
	#otherwise:
		#tell them that user doesn’t exist
		#if they chose to log out:
			#set logged in to false (accounts)
			#exit function
		#take a user input telling them to press enter to continue
		#clear screen
