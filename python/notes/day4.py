# Library
import random

# Casting
# Demonstrating type conversions
a = str(3)  # "3"
b = int(3)  # 3 (whole number)
c = float(3)  # 3.0 (decimal)

# Data Types
print(type(a))  # <class 'str'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'float'>

# Setting Variables
x = 5
y = "Jeremy"

d, e, f = "Detroit", "Eureka!", "Fayetteville"

g = h = i = "France"

# List
cars = ["Mercedes", "Lamborghini", "Ferrari"]
j, k, l = cars

print(cars[2])  # Prints "Ferrari"
print(cars[1:2])  # Prints a range of elements: ["Lamborghini", "Ferrari"]
print(cars[:1])  # Prints elements up to index 1: ["Mercedes", "Lamborghini"]

cars.insert(2, "Ford")  # Inserts "Ford" at index 2 and shifts elements
cars[4:5] = "Chevy"  # Replaces element at index 4 with "Chevy"
cars.remove("Mercedes")  # Removes "Mercedes" from the list
cars.pop(1)  # Removes element at index 1
cars.clear()  # Clears the list

# Sorting Lists
numberList = [1, 2, 4, 6, 12, 61, 412, 15, 99]
print(numberList)
numberList.sort()  # Sorts the list in ascending order
print(numberList)
numberList.sort(key=str.lower)  # Sorts the list case-insensitively
print(numberList)
numberList.sort(reverse=True)  # Sorts the list in descending order
print(numberList)

# Copying Lists
numberList2 = numberList.copy()  # Creates a copy of numberList

# Output
print(b, l)  # Prints both an integer and a string with a comma separator

# Escape Characters
print("We are currently in class and here is a \"quote\"")  # Using double quotes within a double-quoted string
print('We are currently in class and here is a "quote"')  # Using single quotes within a single-quoted string

# Mini Challenge
repCities = [
    "Charlotte", "Salisbury", "Greenville", "Seattle", "Atlanta", "Hampton",
    "Tashkent", "East Orange"
]

userCity = input("What city do you represent?: ").capitalize()

if userCity in repCities:
    print("Your city is represented")
else:
    print("Your city is not represented")
