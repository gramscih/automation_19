import more_itertools


names = ['Jaime', 'Pedro', 'Gramsci', 'Chazz']

# print(names[0])
# print(names[2])

# print(names[-1])
# print(names[-2])
# print(names[-3])

items = ["item 1", 4, "item 2", names]

# print(items)

motorcicles = ['honda', 'yamaha', 'suzuki', 'honda']

# motorcicles[0] = 'ducati'  # Update

# motorcicles.append('ducati') # add elements

# motorcicles.insert(0, 'ducati')

# del motorcicles # take care with this function, if would be used.

# motorcicles.remove('honda')
motorcicles.sort(reverse=True)

# print(motorcicles)

# Tuples

cars = ('bmw', 'audi', 'toyota', 'subaru')

# print(cars)
# print(cars[1])

# for iteration
# syntax for item in items:

for motorcicle in motorcicles:
    pass
    # print(motorcicle)

for car in cars:
    pass
    # print("\n" + car)

value = 0
for index in range(0, len(motorcicles)):
    # print(motorcicles[index])
    value = value + index
    motorcicles[index] = motorcicles[index] + str(value)


# print(motorcicles)


# Looping through slice
motorcicles = ['honda', 'yamaha', 'suzuki', 'honda', 'other1', 'other2']

# print(motorcicles[1:3])
# print(motorcicles[1:4])
# print(motorcicles[:3])
# print(motorcicles[1:])


str_msg = "This is an example to show usage of an string"

print(str_msg[:10])

# for item in str_msg:
#     print(item)

# List Comprehensions

motorcicles = ['honda', 'yamaha', 'suzuki', 'honda', 'other1', 'other2']

motorcicles_with_h = [motorcicle for motorcicle in motorcicles if motorcicle.startswith('h')]

print(motorcicles_with_h)