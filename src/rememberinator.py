from random import choice, randint
from time import sleep

def run():
    print("Welcome to Rememberinator")
    print("You will recieve a list aof characters, which you will enter in the order they were displayed")
    input("Hit enter to start")
    print("\x1b[2J\x1b[H", end="")
    def getRandom():
        return chr(randint(97, 122))

    chars = []
    score = 0
    gameOver = False

    while not gameOver:
        sleep(2)
        chars.append(getRandom())
        for i in chars:
            print("\x1b[2J\x1b[H", end="")
            print(i)
            sleep(1)        
        
        print("\x1b[2J\x1b[H", end="")

        currentIndex = 0
        firstChar = input("What is the first character? ")

        if firstChar != chars[0]:
            print("Incorrect")
            gameOver = True;
        else:
            while True:
                currentIndex += 1
                print("Thats correct!")
                if len(chars) <= currentIndex:
                    score += 1
                    print(f"Level {score + 1} complete")
                    break;
                else:
                    nextChar = input("What is the next character? ")
                    if nextChar != chars[currentIndex]:
                        print("Incorrect")
                        gameOver = True
                        break;
    
    print(f"Score: {score}")
    return score

run()                    



            
