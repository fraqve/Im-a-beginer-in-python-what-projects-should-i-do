import random
import os
import time
def select(choice):
    if choice == "1":
        weapon = rock()
    elif choice == "2":
        weapon = paper()
    elif choice == "3":
        weapon = cisours()
    return weapon

def judjement(object1,obejct2):
    if object1.weakness == obejct2.name:
        return "player2"
    elif object1.name == obejct2.name:
        return "Tie"
    else:
        return "player1"

class bot:
    def __init__(self) -> None:
        self.weapon = None
    def random_weapon_selection(self):
        options = ["1","2","3"] # 1 = rock      2 = paper     3 = cisours  
        choice = random.choice(options)
        self.weapon = select(choice) 
        return self.weapon

class rock:
    def __init__(self) -> None:
        self.name = "Rock"
        self.weakness = "Paper"
        self.stongness = "Cisours"
class cisours:
    def __init__(self) -> None:
        self.name = "Cisours"
        self.weakness = "Rock"
        self.stongness = "Paper"

class paper:
    def __init__(self) -> None:
        self.name = "Paper"
        self.weakness = "Cisours"
        self.stongness = "Rock"

print("Hello you're a pro player of rock paper cisours")
while True:
    time.sleep(4)
    os.system("cls")
    print("Select one of the options below:")
    print("1) Rock")
    print("2) Paper")
    print("3) Cisours")
    choice = input("To select type one of the numbers that corespend to one of the options above  ")
    os.system("cls")
    weapon = select(choice)


    oppnent = bot()
    oppnent.random_weapon_selection()

    winner = judjement(weapon,oppnent.weapon)


    print(f"You:\n{weapon.name}")
    print()
    print(f"Oppnent:\n{oppnent.weapon.name}")


    if winner == "player1":
        print("You won")
    elif winner == "Tie":
        print("Tie")
    else:
        print("You lost")
    time.sleep(2)
