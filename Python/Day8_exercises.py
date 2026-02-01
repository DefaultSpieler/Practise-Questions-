#Paint area Calculator

test_h = int(input("Height of walls: "))
test_w = int(input("Width of walls : "))
coverage = 5

def paint_calc(height, width, cover):
	no_of_cans = (height * width) / cover 
	print(round(no_of_cans))


paint_calc(height = test_h, width = test_w,  cover = coverage)

#Prime Number Checker

n = int(input("Check this number: "))

def prime_checker(number):
	check = True
	for i in range(2,number - 1):
		if number % i == 0:
			check = False
	if check:
		print("prime")
	else:
		print("not prime")


prime_checker(number = n)


# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encrypted = ""
decoded = ""

def encrypt():
	
	for i in text:
		pos = alphabet.index(i)
		new_pos = pos + shift
		global encrypted
		encrypted += alphabet[new_pos]
	print("-----------------------------------")
	print(encrypted)
	print("-----------------------------------")


def decode():
	encrypted
	for i in encrypted:
		pos = alphabet.index(i)
		new_pos = pos - shift
		global decoded
		decoded += alphabet[new_pos]
	print("-----------------------------------")
	print(f"The decoded message is {decoded}")
	print("-----------------------------------")

print("Welcome to Caesar Cipher")
print("-----------------------------------")
text = input("Type your message:\n").lower()
print("-----------------------------------")
shift = int(input("Type the shift number:\n"))
print("-----------------------------------")
encrypt()
print("-----------------------------------")
option = input("DO you wish to decode the mesaage? Press yes to decode \n")
if option == "yes":
	print("-----------------------------------")
	decode()
	print("-----------------------------------")





