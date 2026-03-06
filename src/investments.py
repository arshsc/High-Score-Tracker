import time as t
import random as r
from helper import *
def invest():
    input_stocks = ['stocks','invest','1','stock','buy','buy stocks','purchase','purchase stocks','invest money']
    input_sell_stocks = ['sell stocks','sell','3','make money']
    input_loan = ['free money','free','2','loan','money','moneys','loans','loan money','bank loan']
    input_end = ['end','terminate','exit','7','done','lose','win','die']
    input_lottery = ['6','lottery']
    input_coin_flip = ['4','coin','flip','coin flip']
    input_yes = ['yes','y','yep','yes please','yess','ye','sure','why not','ok','okay','absolutely','let\'s do it','do it','go ahead','coin flip','coin','flip','cool','uh huh','yeah','let\'s start','start','let\'s','lets do it','lets start','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','30','40','50','60','70','80','90','100','200','500','1000']
    input_head = ['heads','head','h']
    input_tails = ['tails','tail','t']
    print('Hello.')
    t.sleep(1)
    print('Welcome to ....')
    t.sleep(1.5)
    print('The bank!')
    t.sleep(1)
    print('Yes, the bank.')
    t.sleep(1)
    print('Here, we...')
    t.sleep(1.5)
    print('... Invest.')
    t.sleep(1)
    print('"Investing" works in turns.')
    t.sleep(1)
    print("Let's start!")
    t.sleep(2)
    turn = 1
    money = 100
    stock_cost = 5
    stocks = 0
    stocks_amount = 0
    stock_change = 0
    loan = 0
    loan_turns = 0
    owed = 0
    lottery = 0
    lottery_value = 10000
    coin = 0
    coinchoice = 0
    betting_value = 5
    while True:
        input('\033[32mPress ENTER to continue > \033[0m')
        print('\033c', end='')
        print(f'Turn {turn}. You have ${money}, and {stocks} stocks.')
        t.sleep(1)
        if stocks > 0:
            stock_change = r.randint(-2,2)
            if stock_cost + stock_change < 1:
                stock_change = r.randint(1,3)
            elif stock_cost + stock_change < 4:
                stock_change = r.randint(-1,2)
            elif stock_cost + stock_change > 15:
                stock_change = r.randint(-3,1)
            elif stock_cost + stock_change > 10:
                stock_change = r.randint(-3,2)
            else:
                if r.randint(0,2) == 0:
                    stock_change = r.randint(-3,3)
                else:
                    stock_change = r.randint(-2,2)
            if stock_change == 0:
                stock_change = r.randint(-1,1)
            stock_cost += stock_change
            print(f'The stock value is now {stock_cost}! It changed by {stock_change}.')
            t.sleep(1)
        if loan_turns > 0:
            loan_turns -= 1
            if loan_turns > 0:
                print(f'You have {loan_turns} turns left to return the money!')
            elif loan_turns == 0:
                print('It\'s time! Pay up!')
                t.sleep(1)
                if owed > money:
                    print('Looks like you owe a bit too much!')
                    t.sleep(1)
                    print('Too bad, so sad, you lose.')
                    break
                else:
                    money -= owed
                    owed = 0
                    print(f'You now have ${money}.')
            t.sleep(1)
        if lottery > 0:
            print('The lottery is running!')
            t.sleep(1)
            lottery_value += r.randint(-1000,1500)
            print(f'You have {lottery} tickets.')
            t.sleep(1)
            lottery_win = r.randint(1,lottery_value)
            print('The winning number is...')
            t.sleep(3)
            print(str(lottery_win) + '!')
            t.sleep(1)
            if lottery_win <= lottery:
                print(f'You won! You get ${lottery_value} dollars. Legitamate dollars.')
                t.sleep(2)
                print('Very legitamate.')
                money += lottery_value
                t.sleep(2)
                print(f'You now have ${money}!')
                t.sleep(0.5)
            else:
                print('You didn\'t win. Too bad!')
            lottery = 0

        activity = input('1. Stocks \n2. "Free money"\n3. Sell Stocks \n4. Coin Flip\n5. Pass\n6. Lottery\n7. End\n').lower().strip()
        if activity in input_stocks:
            print('Welcome to the stock market!')
            t.sleep(1.5)
            print('Here you can buy stocks in my company.')
            t.sleep(0.5)
            print('I mean-')
            t.sleep(0.5)
            print('The bank!')
            t.sleep(1)
            stocks_amount = int_input(prompt=f'How many stocks would you like to buy? They are each ${stock_cost}.\n')
            if stocks_amount == 0:
                print('No stocks? Okay then.')
            elif stocks_amount * stock_cost > money:
                print('You can\'t afford that many stocks.')
            else:
                print('Thank you for buying my... stocks!')
                money -= stocks_amount * stock_cost
                stocks += stocks_amount
        elif activity in input_sell_stocks:
            print('Here you can sell your stocks!')
            t.sleep(2)
            sell_stocks = int_input(prompt='How many, er, stocks would you like to sell?\n')
            if sell_stocks > stocks:
                print('Hey! I can count, you don\'t have that many stocks. Your tricks don\'t work on me.')
            elif sell_stocks == 0:
                print('None? Fine by me.')
            else:
                print(f'Here\'s your ${sell_stocks * stock_cost} from the {sell_stocks} stocks.')
                money += sell_stocks * stock_cost
                stocks -= sell_stocks
        elif activity in input_loan:
            if loan_turns > 0:
                print('You\'d like to add money to your loan, egh?')
                t.sleep(1)
                print('You can, but it won\'t extend the time you have.')
                t.sleep(1)
                print('And you\'ll still owe what you did before!')
                t.sleep(1)
                loan_add = int_input(prompt='How much would you like to add? I\'d say you can add up to $1000')
                owed += loan_add * 1.5
                money += loan_add
                continue
            print('You need some money, egh?')
            t.sleep(1)
            print('While don\'t worry about it! I got you covered.')
            t.sleep(1)
            print('I\'ll give you some right now if you\'ll pay it back later.')
            t.sleep(1)
            print('With interest, of course.')
            t.sleep(1)
            loan = int_input(prompt='So, what\'ll it be?\n')
            if loan == 0:
                print('No money? Okay then.')
            elif loan > 10000:
                print('No that\'s a bit ridiculous, don\'t you think?')
            else:
                print(f'Here\'s your ${loan}. Spend it wisely! I\'ll come collect the return in 5 turns.')
                money += loan
                loan_turns = 6
                owed = loan * 1.5
                t.sleep(3)
                print(f'Which will be ${owed}, by the way.')
        elif activity in input_end:
            score = money - 100
            print(f'Thanks for... "invest"ing! Your score was {score}.')
            if score < 0:
                print("You lost money! That's sad.")
                t.sleep(2)
                print('Sad for you.')
            elif score == 0:
                print("You broke even! Try harder next time.")
                t.sleep(2)
                print('Not that I care.')
            elif score > 0 and score <= 100:
                print("At least it's better than 0!")
                t.sleep(2)
                print('A *bit* better...')
            elif score > 100 and score < 1000:
                print("Nice job!")
                t.sleep(2)
                print('Ish.')
            elif score >= 1000:
                print("Wow!")
                t.sleep(2)
                print('Is what i would have said if you did better.')
            elif score >= 10000:
                print('Epic!')
                t.sleep(2)
                print('Gains, that is. Epic gains.')
                t.sleep(2)
                print('For my company.')
            elif score >= 100000:
                print('You will go down in history as an investing champion.')
                t.sleep(2)
                print('Or, at least in this company\'s history.')
            elif score >= 1000000:
                print('You made millions off investing! Very impressive! Don\'t go betting it all on a coin flip!')
                t.sleep(2)
                print('Or do, i don\'t care.')
            elif score >= 10000000:
                print('You are truly one of the greatest investors to ever live!')
                t.sleep(2)
                print('Although that might not be true for much longer.')
            elif score >= 100000000:
                print('You are either a genius, or just unbelievably lucky.')
                t.sleep(2)
                print('Unbelievable lucky for my company, that is.')
            elif score >= 1000000000:
                print('You are an investing billionare! Truly, amazing.')
                t.sleep(2)
                print('Amazing how these numbers go up.')
                t.sleep(2)
                print('Look at all those zeros.')
            elif score >= 1000000000000:
                print('Stop cheating. You know you didn\'t really earn that trillion dollars.')
                t.sleep(2)
                print('Makes you wonder where it all came from.')
                t.sleep(2)
                print('A trillion dollars.')
            elif score >= 1000000000000000:
                print('I\'m not even going to ask.')
            return score
        elif activity in input_lottery:
            print('Welcome to the lottery!')
            t.sleep(1)
            print('Here you can buy lottery tickets')
            t.sleep(1)
            print('Each ticket has a chance to get you LOTS of money.')
            t.sleep(1)
            tickets = int_input(prompt='How many tickets would you like to buy? They are each $1.\n')
            if tickets == 0:
                print('No tickets? Okay then.')
            elif tickets > money:
                print('You can\'t afford that many tickets.')
            else:
                money -= tickets
                lottery += tickets
                lottery_value += tickets
                print('Thank you for buying tickets!')
        elif activity in input_coin_flip:
            print('Welcome to the coin flip!')
            t.sleep(1)
            print('Here you can play a fun game of flipping coins!')
            t.sleep(1.5)
            print(f'And you choose the price!')
            t.sleep(1)
            print('Well then, shall we? (yes/no)')
            yes_or_no = input().replace('!','').strip().lower()
            if yes_or_no in input_yes:
                betting_value = int_input(prompt='How much would you like to wager?\n')
                if money >= betting_value:
                    money -= betting_value
                    t.sleep(0.5)
                    print('Heads or tails?')
                    while not False:
                        heads_or_tails = input().strip().lower()
                        if heads_or_tails in input_head:
                            coinchoice = 1
                            break
                        elif heads_or_tails in input_tails:
                            coinchoice = 0
                            break
                        elif heads_or_tails == 'either':
                            coinchoice = r.randint(0,1)
                            break
                        else:
                            print('Please pick heads or tails!')
                    if coinchoice == 0:
                        print('You are tails!')
                    elif coinchoice == 1:
                        print('You are heads!')
                    t.sleep(1)
                    betting_value *= 2
                    print(f'There is ${betting_value} on the table!')
                    t.sleep(1)
                    print('Flipping coin...')
                    t.sleep(1)
                    coin = r.randint(0,1)
                    if coin == 0:
                        print('The coin is tails!')
                    elif coin == 1:
                        print('The coin is heads!')
                    t.sleep(1)
                    if coin == coinchoice:
                        print(f'You win ${betting_value}!')
                        money += betting_value
                        t.sleep(1)
                        print('Come back later!')
                        t.sleep(1)
                        print('Or don\'t.')
                    else:
                        print('Aw, you lost.')
                        t.sleep(1)
                        print('Too bad!')
                        t.sleep(2)
                        print('Tooo bad.')
                else:
                    print('You don\'t have enough money!')
        else:
            print('You passed this turn.')
        t.sleep(2)
        turn += 1