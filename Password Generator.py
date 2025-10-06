import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# #Easy way
# generated_password = ""
# for letter in range(0,nr_letters):
#     generated_password += random.choice(letters)
#
# for number in range(0,nr_numbers):
#     generated_password += random.choice(numbers)
#
# for symbol in range(0,nr_symbols):
#     generated_password += random.choice(symbols)
#
# print(generated_password)

#hard way
generated_password = []
for letter in range(0,nr_letters):
    generated_password.append(random.choice(letters))

for number in range(0,nr_numbers):
    generated_password.append(random.choice(numbers))

for symbol in range(0,nr_symbols):
    generated_password.append(random.choice(symbols))


#shuffle manually
#myPass = " "
# for char in generated_password:
#     myPass +=  random.choice(generated_password)

#auto shuffle

random.shuffle(generated_password)
seperator = ""
myPass = seperator.join(generated_password)

#print(type(myPass))

print(myPass)