#Data types

num = input("Enter a 2 digit number ")

res = int(num[0]) + int(num[1])

print(res)

#BMI Calculator

weight = float(input("Enter your Weight in KG's"))
height = float(input("Enter your Height in m"))

result = int(weight / (height**2))

print(result)

#Life in Weeks

print("Life in Weeks")
curAge = int(input("Enter your current age "))

totalAgeInWeeks = 90 * 52
totalAgeInDays = 90 * 365
totalAgeInMonths = 90 * 12

cAgeInDays = curAge * 365
cAgeInWeeks = curAge * 52
cAgeInMonths = curAge * 12

weeksLeft = totalAgeInWeeks - cAgeInWeeks
daysLeft = totalAgeInDays - cAgeInDays
monthsLeft = totalAgeInMonths - cAgeInMonths

print(f"You have {daysLeft} days left, {weeksLeft} weeks left and {monthsLeft} months left to live")

#OR

yearsRemaining = 90 - curAge
monthsRemaining = yearsRemaining * 12
weeksRemaining = yearsRemaining * 52
daysRemaining = yearsRemaining * 365

print(f"You have {daysRemaining} days left, {weeksRemaining} weeks left and {monthsRemaining} months left to live")

#Project - Tip Calculator

print("Welcome to the tip calculator")

totalBill = float(input("What was the total bill? "))
per = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
split = float(input("How many people to split the bill? "))

ans = (totalBill * (per / 100)) + totalBill

final = ans / split
print(round(final), 2)