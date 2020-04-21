print("\t\t\tWELCOME TO STONE, PAPER, SCISSORS GAME PLAY NOW")
import random
comp_choice = ["s","p","sc"]

chance = 0
chance_limit = 3
comp_point = 0
man_point = 0
u = "you"
com= "computer"
compoint = "Computer point is: "
manpoint = "Your point is: "
print("Click to choose your option\n")
print("s- Stone\np- paper\nsc- scissors")

while chance < chance_limit:
    _input = input("\nStone, Paper, Scissors: ")
    _random = random.choice(comp_choice)

    if _input == _random:
        print("You both have ", _input)
        
    elif _input == "s" and _random == "p":
        comp_point = comp_point +1
        print(f"{compoint}", comp_point)
        print("You Lose!")
        print("Computer have paper but you have stone")
    elif _input == "p" and _random == "s":
        man_point = man_point  + 1
        print(f"{manpoint}",man_point)
        print("Winner!")
        print("You have paper but computer have stone")
    elif _input == "sc" and _random == "s":
        comp_point = comp_point + 1
        print(f"{compoint}", comp_point)
        print("You lose!")
        print("Computer have stone but you have scissors")
    elif _input == "s" and _random == "sc":
        man_point = man_point + 1
        print(f"{manpoint}",man_point)
        print("Winner!")
        print("You have stone but computer have scissors")
    elif _input == "p" and _random == "sc":
        comp_point = comp_point + 1
        print(f"{compoint}", comp_point)
        print("You lose!")
        print("computer have scissors but you have paper")
    elif _input == "sc" and _random == "p":
        man_point = man_point + 1
        print(f"{manpoint}", man_point)
        print("Winner!")
        print("You have scissors but computer have paper")
    else:
        print("You have entered a wrong choice try again")
    chance = chance + 1
        
print("Your leaderboard")
name = input("\nEnter Your name: ")
if comp_point > man_point:
    print("Computer is winner. You lose")
    print("Computer point is " , comp_point)
    print("Your point is" , man_point)
    print("Please Play again")
    
elif man_point > comp_point:
    print(name + " is winner. Computer lose")
    print("Your point is" , man_point)
    print("Computer point is " , comp_point)
    print("Please Play again")
else:
    print(name + " and computer you both have tied")
    print("Please Play again")

