
""" AUTOMATING TASKS WITH LISTS """
import random
import functions

""" LESSON 2: LIST ITERATIONS """
info = [80, 91, 92, 100, 85, 42]
top_mark = 0

""" While loops """
# index = 0
# while index < len(info) - 1:
#     if info[index] >= 90:
#         top_mark += 1
         
#     index += 1
# print(f"You got {top_mark} top mark!")

""" For loops """
# for i in range(len(info)):
#     if info[i] >= 90:
#         top_mark += 1
# print(f"You got {top_mark} top marks!")

""" For each loops """
# for grade in info:
#     if grade >= 90:
#         top_mark += 1
# print(f"You got {top_mark} top marks!")

""" IN OPERATORS  """
# data = [1, 3, 6, 9, 6, 7, 4, 8]

# num = int(input("Enter a number from 1 to 10: "))

# if num in data:
#     print(f"{num} is in the list")
# elif num not in data:
#     print(f"{num} is not in the list")
# else:
#     print("Try again.")

""" Searching for an element """
# data = [2, 3, 5, 4, 5]

# has_bad_review = False
# for review in data:
#     if review < 3:
#         has_bad_review = True
#         break

# if has_bad_review:
#     print("Bad review ditected") 

""" Modifying elements """
# data = [32.34235, 35.246644, 46.46434, 25.464311]

# for i in range(len(data)):
#     data[i] = round(data[i], 2)

# print(data)


""" Keeping track of states """
data = [34, 32, 35, 64, 46]

# biggest = data[0]

# for num in data:
#     if num > biggest:
#         biggest = num

# print(f"Biggest number is: {biggest}") 

""" Syntax shortcuts """
# minimum = min(data)
# maximum = max(data)
# addieren = sum(data)

# print(minimum)
# print(maximum)
# print(addieren)

""" Lists and functions """
# names = ["Maxwell", "Adaobi", "Chimereze", "Vivian", "Chibuzor", "Sylvester"]
# functions.find_longest_name(names)

""" Generalize with length """
# prices = [23.3425, 36.4623, 56.2454]
# for i in range(len(prices)):
#     prices[i] = round(prices[i], 2)
# print(prices)

""" Check for valid inclusion """
# def in_compass(direction):
#     """ Returns true if direction is valid """
#     return direction in ["W", "S", "E", "N"]

# direction = ""
# while not in_compass(direction):
#     direction = input("Enter a compass direction: ")

""" Skip unneeded element """
# def get_average_temperature(temperatures):
#     counts = 0
#     total = 0

#     for temp in temperatures:
#         # Extreme cases are likely false readings
#         if temp < 30 or temp > 40:
#             continue

#         total += 1
#         counts += temp

#     return round(counts / total, 1)

# Temperatures = [34.323, 42.552, 35.5343, 36.585]
# average = get_average_temperature(Temperatures)
# print(f"The average temperature is {average}")

""" Return from all branches """
# def find_empty_slot(slots):
#     """ Returns the index of empty slots """
#     for i in range(len(slots)):
#         if slots[i] == "":
#             return i 
#     return -1

# invent = ["we", "cronus", "athena", "zeus", "", "rabies", ""]

# slot = find_empty_slot(invent)
# if slot >= 0:
#     invent[slot] = "pump"
# print(invent)

""" LESSON 3: String manipulation"""
# message = "Let's Go!"
# # Character indices and numbers
# print(message[0])
# print(message[6:8])
# print(message[-1])
# print(len(message))
# # Containment 
# if "Go" in message:
#     print("Substring identified.")
# # Iteration by index and element
# for i in range(len(message)):
#     print(message[i])
# for car in message:
#     print(car)

""" String methods """
# # using a simple function
# def count(string, cha):
#     count = 0 
#     for c in string:
#         if c == cha:
#             count += 1  
#     return count

# string = "   Bananas are healthy, look at what it did to saitama.  "
# print(count(string, "a"))

# # methods
# print(string.count("a"))
# print(string.lower())
# print(string.upper())
# print("Bananas are healthy, look at what it did to saitama.,,,,,,,,,,,,,,,,".strip(".,"))
# print(string.strip())
# print(string.split())
# print(string.index("a"))

# row = "106,Laptop Stand,Accessories,40,22.50"
# fire = row.split(",")
# print(fire)
# print(",".join(fire))

""" String patterns """
# # String normalization
# roll = input("Pick yes or no: ")
# roll = roll.lower().strip().strip(".,!`?")

# if roll == "yes":
#     print("Good")
# else:
#     print("Bad")

# # String parsing
# def get_domain(email):
#     """ Get's email domain after @ """
#     if email.count("@") != 1:
#         return ""
#     domain = email.index("@")
#     return email[domain + 1:]

# print(get_domain("kimcodes47@example.com"))
# print(get_domain("khan@test.example.org"))

# CSV file
def reset_stats(row):
    stat = row.split(",")
    for i in range(len(stat)):
        if stat[i].isdigit():
            stat[i] = "0"
    return ",".join(stat)


row = "Lionel Messi,Inter Miami,1756,86,45,forward"
print(reset_stats(row))











































