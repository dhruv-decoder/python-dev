#PROJECT-3(TREASURE ISLAND)
#Dhruv Tibarewal

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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# code below this line 👇
ch1 = input('you\'re at a crossroad,where do you want to go ?Type "left" or "right" ').lower()
if ch1 == "left":
  #continue in game
  ch2=input('You\'ve come to a lake . There is an island in the middle of the lake.Type "wait" to wait for the boat else type "swim " to swim across').lower()
  if ch2=="wait":
    #Game will continue
    ch3 = input("you arrived in an island unharmed.There is a house with 3 doors.one red,one yellow and one blue.which colour do you choose? ").lower()
    if ch3=="red":
      print("Its a room full of fire.Game over")
    elif ch3=="yellow":
      print("You found the treasure.You win")
    elif ch3=="blue":
      print("you looked in the sky.Game over.")
    else:
      print("you chose a door that doesnt exist.Game over")  
  else:
    print("you got attacked by an angry trout")
else :
  print("You fe1l into a hole,Game over.")
  


