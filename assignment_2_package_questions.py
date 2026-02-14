# -------------------- Question 1: Importing and Using Modules --------------------

import math

# Square root of 25
print("Square Root of 25:", math.sqrt(25))

# Sine of 90 degrees (convert to radians)
print("Sine of 90 degrees:", math.sin(math.radians(90)))


# -------------------- Question 2: Aliasing Modules --------------------

import datetime as dt

# Current date and time
print("Current Date and Time:", dt.datetime.now())


# -------------------- Question 3: Importing Specific Functions --------------------

from random import randint

# Random integer between 1 and 100
print("Random Number:", randint(1, 100))


# -------------------- Question 4: Importing Multiple Functions --------------------

from math import sqrt, pow

print("Square Root of 16:", sqrt(16))
print("2 raised to power 3:", pow(2, 3))


# -------------------- Question 5: Handling Import Errors --------------------

try:
    import non_existent_module
except ImportError:
    print("Module not found.")


# -------------------- Question 6: Working with the os Module --------------------

import os

# Create directory
os.mkdir("test_directory")

# List current directory contents
print("Directory Contents:", os.listdir())

# Remove directory
os.rmdir("test_directory")


# -------------------- Question 7: Working with the sys Module --------------------

import sys

print("Python Version:", sys.version)
print("Command-line Arguments:", sys.argv)


# -------------------- Question 8: Working with the math Module --------------------

print("GCD of 12 and 18:", math.gcd(12, 18))
print("Factorial of 5:", math.factorial(5))


# -------------------- Question 9: Working with the datetime Module --------------------

from datetime import datetime, timedelta

today = datetime.now()
print("Current Date:", today.date())

# Date after 100 days
future_date = today + timedelta(days=100)
print("Date after 100 days:", future_date.date())

# Day of the week for a given date
given_date = datetime(2025, 1, 1)
print("Day of Week (2025-01-01):", given_date.strftime("%A"))


# -------------------- Question 10: Working with the random Module --------------------

import random

# List of 5 random numbers
random_list = [random.randint(1, 50) for _ in range(5)]
print("Random List:", random_list)

# Shuffle a list
sample_list = [1, 2, 3, 4, 5]
random.shuffle(sample_list)
print("Shuffled List:", sample_list)


# -------------------- Question 11: Creating a Simple Package --------------------

# Assume structure:
# mypackage/
#   module1.py  -> add(a, b)
#   module2.py  -> multiply(a, b)

# Example usage:
# from mypackage import module1, module2
# print(module1.add(2,3))
# print(module2.multiply(2,3))


# -------------------- Question 12: Using __init__.py --------------------

# __init__.py contains:
# from .module1 import add
# from .module2 import multiply

# Example usage:
# from mypackage import add, multiply
# print(add(5,6))
# print(multiply(5,6))


# -------------------- Question 13: Importing from a Package --------------------

# Direct import from package (after modifying __init__.py)
# from mypackage import add, multiply
# print(add(10,20))
# print(multiply(10,20))


# -------------------- Question 14: Relative Imports --------------------

# New structure:
# mypackage/
#   module1.py
#   subpackage/
#       module2.py

# __init__.py:
# from .module1 import add
# from .subpackage.module2 import multiply

# Example usage:
# from mypackage import add, multiply
# print(add(3,4))
# print(multiply(3,4))


# -------------------- Question 15: Handling Package Import Errors --------------------

try:
    from mypackage import non_existent_function
except ImportError:
    print("Function not found in package.")
