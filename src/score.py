#Import the csv library
from helper import *

#Make a function called the high score tracker (it will be called every time someone gets a score), using the user account, game, and new score as a parameter
def score_recorder(user, game, new_score)
	#Have the computer attempt to 
	try:
		#Call the csv to dictionary function that changes the csv to a dictionary
		high_scores = csv_to_dictionary("docs/high_scores.csv")
	#If it doesn’t work
	except Exception as e:
		#Tell the player that the file is not found
		print(f"You had a {e} error. ")
	#Otherwise if it does work
	else:
		for users in high_scores:
			if high_scores[users] == user:
				if high_scores[users][game] < new_score:
					print(f"You beat your high score of {high_scores[users][game]}! ")
					high_scores[users][game] = new_score
		#Update the dictionary
		save_csv(high_scores, "docs/high_scores.csv")


#Make a function that finds the high score of the player, with the player and game as parameters
def high_score_player():
	#Have the computer attempt to 
		#Call the csv to dictionary function that changes the csv to a dictionary
	#If it doesn’t work
		#Tell the player that the file is not found
	#Otherwise if it does work
		#Pull up the player’s account
		#See if their high score is beaten
			#If so, tell them they beat their high score
		#Otherwise, 
#Show the comparison between their new score and the high score

#Make a function that displays the high scores, using the game as the parameter
	#Have the computer attempt to 
		#Call the csv to dictionary function that changes the csv to a dictionary and returns the dictionary
	#If it doesn’t work
		#Tell the player that the file is not found
	#Otherwise if it does work
		#Make a loop that repeats for every player in the csv file
			#Make a loop that loops through all the previous names
				#If the name is bigger than the next name
				#Put the name in the list in front of the other one
		#Make a loop that repeats for every name in the list
			#Print the name and their score
