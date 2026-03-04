# high score tracker
import turtle
import random

def rock_paper_scissors():
    score = 0
    robo_score = 0
    rock = """
                ______________                                                                                                                                                               
    ........../      _______) 
                    (_______)
                    (_______)
                    (_______)
    -------,__________(_____)
    """
    scissors = """
                _____________                                                                                                                                                               
    ........../          ___)_________
                        _____________)
                        ____________)
                    (______)     
    -------,__________(_____)
    """
    paper = """
                _____________                                                                                                                                                               
    ........../          ___)__
                        ______)
                        _______)
                    ________)
    -------,_______________)
    """
    print("Welcome to rock paper scissors. ")
    while True:
        choose = 0
        print(f"Your score is :{score}")
        print(f"The robot's score is :{robo_score}")
        choice = input("Which do you want to choose, rock(r), paper(p), or scissors(s)? If you want to quit, then write 'q'. ")
        if choice == "q":
            break
        elif choice == "r":
            choose = 1
        elif choice == "p":
            choose = 2
        elif choice == "s":
            choose = 3
        robot_choice = random.randint(1,3)

        if choose == 1 and robot_choice == 3:
            print("You won! ")
            print(f"You chose rock! {rock}")
            print(f"The robot chose scissors! {scissors}")
            score += 1
        elif choose == 2 and robot_choice == 1:
            print("You won! ")
            print(f"You chose paper! {paper}")
            print(f"The robot chose rock! {rock}")
            score += 1
        elif choose == 3 and robot_choice == 2:
            print("You won! ")
            print(f"You chose scissors! {scissors}")
            print(f"The robot chose paper! {paper}")
            score += 1
        elif choose == 1 and robot_choice == 1:
            print("You tied! ")
            print(f"You chose rock! {rock}")
            print(f"The robot chose rock! {rock}")
        elif choose == 2 and robot_choice == 2:
            print("You tied! ")
            print(f"You chose paper! {paper}")
            print(f"The robot chose paper! {paper}")
        elif choose == 3 and robot_choice == 3:
            print("You tied! ")
            print(f"You chose scissors! {scissors}")
            print(f"The robot chose scissors! {scissors}")
        elif choose == 1 and robot_choice == 2:
            print("You lost!")
            print(f"You chose rock! {rock}")
            print(f"The robot chose paper! {paper}")
            robo_score += 1
        elif choose == 2 and robot_choice == 3:
            print("You lost!")
            print(f"You chose paper! {paper}")
            print(f"The robot chose scissors! {scissors}")
            robo_score += 1
        elif choose == 3 and robot_choice == 1:
            print("You lost!")
            print(f"You chose scissors! {scissors}")
            print(f"The robot chose rock! {rock}")
            robo_score += 1
        check = input("Do you want to stop playing? ").strip().lower()
        if check == "yes":
            return score - robo_score

def guesser_bros_lite():
    while True:
        print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
        number_to_guess = random.randint(1, 100)
        max_attempts = 10
        attempts = 0
        game_over = True
        while game_over:
            guess = int(input("Enter your guess: "))
            if attempts >= max_attempts:
                print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
                game_over = False
            elif guess == number_to_guess:
                print("Congratulations! You've guessed the number!")
                game_over = False
            elif guess > number_to_guess:
                attempts += 1
                print("Too high! Try again.")
            elif guess < number_to_guess:
                attempts += 1
                print("Too low! Try again.")  
        check = input("Do you want to stop playing? ").strip().lower()
        if check == "yes":
            return attempts


def tuterria():
    patience = 0
    money = 500
    drawer = turtle.Turtle()
    turtle1 = turtle.Turtle() 
    turtle2 = turtle.Turtle() 
    turtle3 = turtle.Turtle() 
    turtle4 = turtle.Turtle() 
    turtle5 = turtle.Turtle() 
    drawer.color("black")
    drawer.speed(0)
    drawer.teleport(510, 500)
    drawer.right(90)
    for i in range(50):
        drawer.begin_fill()
        for x in range(5):
            drawer.forward(10)
            drawer.right(90)
        drawer.end_fill()
        drawer.left(90)
        drawer.begin_fill()
        for x in range(5):
            drawer.forward(10)
            drawer.left(90)
        drawer.end_fill()
        drawer.right(90)
    drawer.hideturtle()
    while True:
        finish_order = []
        turtles = [turtle1, turtle2, turtle3, turtle4, turtle5]
        setup(turtles)
        print(f"You have ${money}. ")
        bet_choice = input("Which turtle do you want to bet on? If you don't want to bet on any, write anything. Blue(1), teal(2), green(3), orange(4), red(5). ")
        if bet_choice in ["1", "2", "3", "4", "5"]:
            while True:
                bet_amount = input("How much do you want to bet on this turtle? ")
                if bet_amount.isdigit():
                    bet_amount = int(bet_amount)
                else:
                    print("That is an invalid input. Please try again. ")
                    continue
                if money < bet_amount or bet_amount < 0:
                    print("That is an invalid input. Please try again. ")
                else:
                    break
        else:
            bet_amount = 0
        finish_order = move(turtles, finish_order)
        if finish_order[0] == bet_choice:
            bet_amount *= 4
            money += bet_amount
            print("Your turtle finished in 1st place! ")
        elif finish_order[1] == bet_choice:
            money += bet_amount
            print("Your turtle finished in 2nd place! ")
        elif finish_order[2] == bet_choice:
            print("Your turtle finished in 3rd place! ")
        elif finish_order[3] == bet_choice:
            money -= bet_amount
            print("Your turtle finished in 4th place! ")
        elif finish_order[4] == bet_choice:
            print("Your turtle finished in last place! ")
            bet_amount *= 2
            money -= bet_amount
        else:
            print("You chose not to bet this round. ")
        if money <= 0 and patience <= 5:
            print("Here is some pity money. I felt sorry for you. ")
            money = 1000
            patience += 1
        if patience >= 5:
            print("JK. You asked for too much money! I'm not giving any money to you! You are being kicked out! ")
            return 0
        check = input("Do you want to leave? If so, answer yes. ").strip().lower()
        if check == "yes":
            return money

def setup(turtles):
    colors = ["blue", "teal", "green", "orange", "red"]
    y_positions = [40, 20, 0, -20, -40]
    for i, t in enumerate(turtles):
        t.speed(0)
        t.shape("turtle")
        t.color(colors[i])
        t.teleport(-500, y_positions[i])

def move(turtles, finish_order):
    while len(finish_order) < 5:
        for t in turtles:
            t.forward(random.randint(1, 10))
        turtles[1].forward(0.025)
        turtles[4].backward(0.025)
        winner(turtles, finish_order)
    return finish_order


def winner(turtles, finish_order):
    for i, t in enumerate(turtles):
        if t.xcor() >= 500 and str(i+1) not in finish_order:
            finish_order.append(str(i+1))
    return finish_order
