#Odd or Even Introducing the Modulo

num = int(input("Enter the desired number"))

if num % 2 == 0:
	print("This is a even number")
else:
	print("This is a odd number")

#BMI 2.0

weight = float(input("Enter your weight"))
height = float(input("Enter your height"))

bmi = weight / height ** 2

if bmi < 18.5:
	print("underweight")
elif bmi < 25:
	print("normal weight")
elif bmi < 30:
	print("overweight")
elif bmi < 35:
	print("obese")
else:
	print("clinically obese")

#Leap Year

year = int(input("Enter the year you want to check"))

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print(f"The year {year} is a leap year")
		else:
			print(f"The year {year} is not a leap year")
	else:
		print(f"The year {year} is a leap year")
else:
	print(f"The year {year} is not a leap year")

#Pizza Order Practice

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0

if size =="S":
	price = 15
	if add_pepperoni == "Y":
		price = price + 2
	else:
		price = price
	if extra_cheese == "Y":
		price = price + 1
	else:
		price = price
elif size == "M":
	price = 20
	if add_pepperoni == "Y":
		price = price + 3
	else:
		price = price
	if extra_cheese == "Y":
		price = price + 1
	else:
		price = price
elif size == "L":
	price = 25
	if add_pepperoni == "Y":
		price = price + 3
	else:
		price = price
	if extra_cheese == "Y":
		price = price + 1
	else:
		price = price
else:
	print("Enter a correct value")

print(f"Your final bill is {price}")

#Love Calculator

print("Welcome to Love Calculator")

urName = input("What is your Name? ")
theirName = input("What is their name? ")

combine = urName + theirName
combined = combine.lower()

T = combined.count("t")
R = combined.count("r")
U = combined.count("u")
E = combined.count("e")

totalTrue = T + R + U + E

L = combined.count("l")
O = combined.count("o")
V = combined.count("v")
E = combined.count("e")

totalLove = L + O + V + E

per = int(str(totalTrue) + str(totalLove))


if per >= 90 or per <= 10:
	print(f"Your score is {per}%. You together are like mentos and coke")
elif per >= 40 and per <= 50:
	print(f"Your score is {per}%. You are alright together")
else:
	print(f"Your score is {per}%.")

#Project - Treasure island

print("Welcome to Tressue Island.")
print(" Your mission is to find the Tressure")

que = input('You are at a cross road. Where do you want to go ? Type "right" or "left"')

if que == "left":
	print("...")
	que2 = input("Will you swim or wait?")
	if que2 == "swim":
		print("You lose.")
		print("Game Over")
	elif que2 == "wait":
		print("...")
		que3 = input("There are three doors - yellow, green and red. Choose one")
		if que3 == "yellow":
			print("You win. You have the tressure now")
		elif que3 == "green" or que3 == "red":
			print("You lose. Game Over")
elif que == "right":
	print("You lose.")
	print("Game Over")
else:
	print("Input not appropriate")

