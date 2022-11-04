password = "dsafdsafdASDFDSF123" # chars > 8 and chars <= 16
              # at least one capital letter (ASDDFG)
              # At least one number (0 - 9)
              # at least one lower letter

# capital_letters = [A, S,C,"Q",Df,F]
# lower_letters = [a,b,f,w,h,d]
numbers = [0,1,5,9]

def generate_passoword():
    pass

# app = input("Application Name")
print("1. Generate Password")
print("2. Get Password")
print("3. Exit")
user_input = input("Your option: ")

if user_input == 1:
    password = generate_passoword()# Generate_passowor
    print(app, password)
elif user_input == 2:
    print(password)


# print(app, password)