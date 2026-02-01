#Random Exercise

import random

#test_seed = int(input("Create a seed number"))
#random.seed(test_seed)

ran = random.randint(0,1)

if ran == 1:
	print("Heads")
else:
	print("Tails")

#Banker Roulette

namesAsCSV = input("Give me everybody's names, separated by comma. ")
names = namesAsCSV.split(", ")

length = len(names)
genRan = names[random.randint(0,length - 1)]

print(f"{genRan} is going to buy the meal today!")


#Tressure Map

row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the tressure?")

one = int((position[0])) - 1
two = int((position[1])) - 1

(map[one][two]) = 'T'

print(map)

#Project - Rock Paper Scissors

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

array = [rock , paper, scissors]

user = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors"))

compIn = int(random.randint(0,2))

print(f"your choice {array[user]}")

print(f"computer's choice {array[compIn]}")

if(user == 0 and compIn == 2):
	print("You win")
elif(user == 0 and compIn == 1 ):
	print("You lose")
elif(user == 1 and compIn == 0):
	print("You win")
elif(user == 1 and compIn == 2):
	print("You lose")
elif(user == 2 and compIn == 0):
	print("You lose")
elif(user == 2 and compIn == 1):
	print("You win")
elif(user == compIn):
	print("Tied")
else:
	print("fedce")
