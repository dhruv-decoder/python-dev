# project-4 ROCK-PAPER-SCISSORS
# Dhruv Tibarewal
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

var = [rock, paper, scissors]
n = int(input("what do you choose?Type 0 for rock,1 for paper and 2 for scissor. "))
r = random.randint(0, 2)
if n == 0:
    print(f"you choose{var[n]}")
    if r == 0:
        print(f"computer choose{var[r]}")
        print("draw")
    elif r == 1:
        print(f"computer choose{var[r]}")
        print("win")
    elif r == 2:
        print(f"computer choose{var[r]}")
        print("loose")
elif n == 1:
    print(f"you choose{var[n]}")
    if r == 0:
        print(f"computer choose{var[r]}")
        print("win")
    elif r == 1:
        print(f"computer choose{var[r]}")
        print("draw")
    elif r == 2:
        print(f"computer choose{var[r]}")
        print("loose")
elif n == 2:
    print(f"you choose{var[n]}")
    if r == 0:
        print(f"computer choose{var[r]}")
        print("loose")
    elif r == 1:
        print(f"computer choose{var[r]}")
        print("win")
    elif r == 2:
        print(f"computer choose{var[r]}")
        print("draw")
else:
    print("wrong choice")
