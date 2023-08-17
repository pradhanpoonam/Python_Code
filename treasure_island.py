print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************     
''')

print("Welcome to treasure Island. Your goal is to find the hidden treasure!!")
choice1 = input('You\'re at crossroad, where do you want to go? Type "left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" or "swim" if you want to wait or swim\n').lower()
    if choice2 == "wait":
        choice3 = input('There\'re 3 doors. Type "red" or "green" or "blue" for the door you want to go through\n').lower()
        if choice3 == "red":
            print("Room full of fire. Game Over")
        elif choice3 == "blue":
            print("Room full of beasts. Game Over")
        elif choice3 == "green":
            print("You have won !! HURRAY")
        else:
            print("That door doesn't exist. Game Over")            
    else:
        print("You'va drowned. Game Over")
else:
    print("You fell into a hole. GaME Over")
