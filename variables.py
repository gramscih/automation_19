name = "gramsci"
last_name = 'hermozo'

# print(name.title())
# print(name.upper())
# print(name.lower())

# full_name = name + ' ' + last_name
# full_name = "{} {}".format(name, last_name)
full_name = f"{name} {last_name}"
print(full_name)

# Tabs and Newlines

# print("Languages:\n\t Python \n\t C \n\t Javascript")

favorite_language = '  Python  '
print(favorite_language.strip())

# Numbers
age = 30

# Floats
cost = 4.5
full_name = 50

print(age, cost, full_name)

num1 = 5
num2 = 7

addition = num1 + num2
print(addition)

# Input values with input() function.

user_input = input("Please enter your name... ")
print(user_input, type(user_input))
num_value = int(user_input)
print(num_value, type(num_value))
print("Hello {}, well come...".format(user_input))