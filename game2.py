from sys import exit
import random

print("What is your name?")
name = raw_input("> ")

def start():
    print("Welcome to the ultimate quest for riches and glory!")

    print("You may move any of eight cardinal directions, which are as follows: \nn \nne \ne \nse \ns \nsw \nw \nnw")

    print("To use these directions, type the letters as are above, and not the full name")

    print("Your goal is to reach the treausre room and to claim the ultimate prize, \nThe Crown of Carmel!!!")

    print("In order to get here, you will face a variety of differenct rooms and have to navigate your way through the world.")

    print("In each room you will face several encounters, and if you prevail, then you will be able to select a direction and move on.")

    print("In each encounter you will be faced with 2 choices. Just type the number of the choice you want, and press enter to select it.")

    print("So good luck, and best of whishes %s" % name)
    print("PS. Pro-Tip: Draw a map on real paper in the real world")

    print("What direction would you like to go in?")
    def der(direction):

        if direction == "n":
            souls()

        elif direction == "ne":
            cloth()

        elif direction == "e":
            pens()

        elif direction == "se":
            lava()

        elif direction == "s":
            pit()

        elif direction == "sw":
            hands()

        elif direction == "w":
            bugs()

        elif direction == "nw":
            pit()

        else:
            noder()

            print("What direction would you like to go in?")

            der(raw_input("> "))

    der(raw_input("> "))

def start1():
    print("You are back at the start again!")

    print("Which direction do you want to go in?")

    def der(direction):

        if direction == "n":
            souls()

        elif direction == "ne":
            cloth()

        elif direction == "e":
            pens()

        elif direction == "se":
            lava()

        elif direction == "s":
            pit()

        elif direction == "sw":
            hands()

        elif direction == "w":
            bugs()

        elif direction == "nw":
            pit()

        else:
            noder()
            der(raw_input("> "))

    print("What direction would you like to go in?")

    der(raw_input("> "))

def souls():
    def der(direction):

        if direction == "n":
            wall()

            print("What direction would you like to go in?")

            der(raw_input(">"))

        elif direction == "ne":
            nothing()

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif direction == "e":
            cloth()

        elif direction == "se":
            pens()

        elif direction == "s":
            start1()

        elif direction == "sw":
            bugs()

        elif direction == "w":
            nothing()

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif direction == "nw":
            sound()

        else:
            noder()

            print("What direction would you like to go in?")

            der(raw_input("> "))

    print("You have entered the room of souls")

    print("Before you there is a sad ghost, what do you do?")

    print("1. Try and sneak past the ghost and into the next room")

    print("2. Go and see what is wrong with the ghost, try and help it")

    choice = raw_input("> ")

    if choice == "1":
        print("The ghost attacks, and you realize it was all a trick to test your morales")

        print("You have two options")

        print("1. Run away from the ghost")

        print("2. Kneel down, and submit to death")

        choice = raw_input("> ")

        if choice == "1":
            print("You ran so far away that you ended back at the begining of the maze!")

            start1()

        elif choice == "2":
            die("The ghost killed you for being a bad person!")

    elif choice == "2":
        print("You go over to help the ghost, and it is made well")

        print("The ghost thanks you for helping and says depending on how you answer the next question he will diecide if he likes you")

        print("True or False, is Gandolf a wizard?")

        print("1. True")

        print("2. False")

        choice = raw_input("> ")

        if choice == "1" or "True" or "true":
            print("That is correct go ahead and make your choice")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif choice == "2" or "False" or "false":
            print("SUFFER MY WRATH!!!!!")

            die("You were kille by a ghost for not knowing your Sc-Fi Fantasy")

        else:
            print("That is not a valid answer, restart the room")

            souls()

    else:
        print("That is not a valid answer, restart the room")

        souls()

def cloth():
    def der(direction):
        if direction == "n":
            nothing()

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif direction == "ne":
            print("There is nothing there")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif direction == "e":
            tar()

        elif direction == "se":
            reading()

        elif direction == "s":
            pens()

        elif direction == "sw":
            start1()

        elif direction == "w":
            souls()

        elif direction == "nw":
            war()

        else:
            noder()

            print("What direction would you like to go in?")

            der(raw_input("> "))


    print("You have entered into the room of cloth, before you stands the great Sewing Machine")

    print("You realize that the machine is running, and that if you continue to stand on the piece of cloth it will impale you! But when you try and move you see your feet are glued down!\nWhat will you do?")

    print("1. Try and unstick your feet in an effort to get loose")

    print("2. You try and talk to the machine to make a diplomatic bargain")

    choice = raw_input("> ")

    if choice == "1":
        chance = [0, 1]

        result = random.choice(chance)

        print("Alright, there is a 50/50 chance that you will escape, litterally, we will see what happens!")

        if result == 1:
            print("You managed to escape! You run away from the sewing machine, and you are free to choose a direction")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif result == 0:
            print("We are very sorry, but you were not able to escape.")

            die(" You were impaled by a sewing machine, pathetic")

        else:
            print("There is an ERROR")

            cloth()

    elif choice == "2":
        print("The machine stops, and tells you to speak your mind")

        print("What do you do?")

        print("1. Make up a sob story about how you are trying to get back to your long lost love, and you will do anything for them")

        print("2. Tell the truth, that you are a greedy treasure hunter looking to make lots of money, and you don't care what you have to do")

        choice == raw_input("> ")

        if choice == "1":
            print("The sewing machine uses the built in lie detector function to tell you are lying!")

            print("The machine decides to kill you for lying")

            die("You lied to a lie detector")

        elif choice == "2":
            print("The machine understands the greed of humans, and decides to let you go on with your quest")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        else:
            print("That is not a valid answer, restart the room")

            cloth()

    else:
        print("That is not a valid answer, restart the romm")

        cloth()

def pens():
    def der(direction):
        if direction == "n":
            cloth()

        elif direction == "ne":
            tar()

        elif direction == "e":
            reading()

        elif direction == "se":
            print("There is nothing there")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif direction == "s":
            lava()

        elif direction == "sw":
            pit()

        elif direction == "w":
            start1()

        elif direction == "nw":
            souls()

        else:
            noder()

            print("What direction would you like to go in?")

            der(raw_input("> "))

    print("Welcome to the room of pens!")

    print("You are walking to the next door")

    print("......................")

    print("And then a pen comes down from the cieling stabbing you under it")

    print("You are bleeding and will die very soon \nWhat will you do?")

    print("1. Remove the pen from your body, and go as fast as you can to the next door")

    print("2. Know that death is coming, and call on the Pen Godess for help")

    choice = raw_input("> ")

    if choice == "1":
        print("As you remove the pen some ink coomes out the tip, and enters your blood stream, giving you blood posining")

        print("What will you do?")

        print("1. Cut your main artery so that you bleed to death quikly")

        print("2. Call on the Pen Godess's son for help")

        choice = raw_input("> ")

        if choice == "1":
            die("You bleed to death painfully")

        elif choice == "2":
            print("The demigod says that his mother probably would have helped, but you blew it, and he will kill you")

            die("You were killed by a todler demigod")

        else:
            print("That is not a valid answer, restart the room")

            pens()

    elif choice == "2":
        print("The Godess answers you and removes the pen very carefully")

        print("You die, but she revieves you, and says she will let you go on, but after a test")

        print("She asks you what is better, Band or Orchestra")

        print("1. Band \n2. Orchestra")

        choice = raw_input("> ")

        if choice == "1":
            print("I agree with you! You may pass")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif choice == "2":
            print("I do not agree with you, but I suppose that everyone is entitled to their own opnions so I will let you pass, but know I hate you now :)")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        else:
            print("That is not a valid answer, restart the room")

            pens()
    else:
        print("That is not a valid answer, restart the room.")

def hands():
    def der(direction):
        if direction == "n":
            bugs()

        elif direction == "ne":
            start1()

        elif direction == "e":
            pit()

        elif direction == "se":
            numbers()

        elif direction == "s":
            lava()

        elif direction == "sw":
            nothing()

            der(raw_input("> "))

        elif direction == "w":
            nothing()

            der(raw_input("> "))

        elif direction == "nw":
            pit()

        else:
            noder()

            der(raw_input("> "))

    print("Welcome to the Hall of Hands")

    print("After you walk in, you feel somethings touching you, and you look over and see thousands of hands on the wals!")

    print("What will you do?")

    print("1. Run through the room as fast as you possibly can to get to the door you see at the end of the hall")

    print("2. Just go back to the start of the maze")

    choice = raw_input("> ")

    if choice == "1":
        print("There is a 3/5 chance that you will survive, lets see what happnens \n**suspense**")

        chance = [1, 2, 3, 4, 5]

        result = random.choice(chance)

        if result == 4 or 5:
            print("The odds were against your favor! Be more wise next time")

            die("Stupidity and bad descision making")

        elif result == 1 or 2 or 3:
            print("You beat the odds, congrats!")

            print("You make it to the end of the hall and are allowed to move on")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        else:
            print("For some reason there was an ERROR")

            hands()

    elif choice == "2":
        print("It may take longer, but trust me, it was for the better..... maybe")

        start1()

    else:
        print("That is not a valid answer, restart the room")

        hands()

def die(why):
    print("You died becuase %s" % why)

    def leave():
        print("Which of the following would you like to do?")

        print("1. Exit the game")

        print("2. Restart the game")

        choice = raw_input("> ")

        if choice == "2":
            start()

        elif choice == "1":
            exit(0)

        else:
            print("That is not a valid answer")

            leave()

    leave()

def lava():
    print("You tripped and fell.")

    die("You fell into lava!")

def wall():
    print("You can not pass because there is a wall, go another way.")

def pit():
    print("You slip on a napkin and fall")

    die("When you fell you landed in a botomless pit, where you starve")

def nothing():
    print("There is nothing there")

def noder():
    print("That is not a direction, try again, rememberuse lowercase letters without a space, for example, ne")

    print("Which way do you want to go?")

start()
