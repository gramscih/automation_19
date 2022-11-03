# Dictionaries

person = {"name": 'Gramsci', "last_name": 'Hermozo', 'age': 30, 'title': 'Dev'}

for key, val in person.items():
    pass
    # print(key, val)

# print('\n')
# print(person['name'])


# if 'title' in person:
#     print(person['title'])

title = person.get('title', 'Unknow')
# print(title)

# Data structure definition other alternative
oid = dict() # {}
lst = list() # []
tp = tuple() # ()
#############################################

# if statement

name = "Gramsci"
name = None

if name:
    print(name)

age = 0
if not age:
    print(age)

name = "gramsci"
if name and 'y' in name:
    print(f"Invalid name {name}")
elif not name.startswith('G'):
    print('Enter a correct personal name')
else:
    print(f"Hello {name}")