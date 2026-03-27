# Assignment (12/02/2026)

# Assignment Name : Smart Input Program
# Description : Build a Python program that takes name, age, hobby 
# and prints a personalized message while categorizing age using conditionals.

# Personalized message program

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")
if age < 13:
    category = "a child"
elif age < 20:
    category = "a teenager"
elif age < 60:
    category = "an adult"
else:
    category = "a senior"
print(f"Hello {name}! You are {age} years old, which makes you {category}.")
print(f"It's awesome that you enjoy {hobby}!")