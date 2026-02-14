# -------------------- Question 1: Creating and Accessing Dictionaries --------------------

# Dictionary with keys 1–10 and their squares
dict1 = {x: x**2 for x in range(1, 11)}
print("Question 1 Output:", dict1)


# -------------------- Question 2: Accessing Dictionary Elements --------------------

# Value of key 5
print("Value of key 5:", dict1[5])

# All keys
print("Keys:", dict1.keys())


# -------------------- Question 3: Dictionary Methods --------------------

# Adding new key-value pair
dict1[11] = 121

# Removing key 1
dict1.pop(1)

print("Question 3 Output:", dict1)


# -------------------- Question 4: Iterating Over Dictionaries --------------------

print("Question 4 Output:")
for key, value in dict1.items():
    print(key, ":", value)


# -------------------- Question 5: Dictionary Comprehensions --------------------

# Cubes of first 10 positive integers
cube_dict = {x: x**3 for x in range(1, 11)}
print("Question 5 Output:", cube_dict)


# -------------------- Question 6: Merging Dictionaries --------------------

dictA = {x: x**2 for x in range(1, 6)}
dictB = {x: x**2 for x in range(6, 11)}

# Merging dictionaries
merged_dict = {**dictA, **dictB}

print("Question 6 Output:", merged_dict)


# -------------------- Question 7: Nested Dictionaries --------------------

student = {
    "name": "John",
    "age": 20,
    "grades": {
        "math": 85,
        "science": 90,
        "english": 88
    }
}

print("Question 7 Output:", student)


# -------------------- Question 8: Dictionary of Lists --------------------

dict_list = {x: [x*i for i in range(1, 6)] for x in range(1, 6)}
print("Question 8 Output:", dict_list)


# -------------------- Question 9: Dictionary of Tuples --------------------

dict_tuple = {x: (x, x**2) for x in range(1, 6)}
print("Question 9 Output:", dict_tuple)


# -------------------- Question 10: Dictionary and List Conversion --------------------

dict2 = {x: x**2 for x in range(1, 6)}

# Convert to list of tuples
tuple_list = list(dict2.items())

print("Question 10 Output:", tuple_list)


# -------------------- Question 11: Dictionary Filtering --------------------

dict3 = {x: x**2 for x in range(1, 11)}

# Filter even keys
even_dict = {k: v for k, v in dict3.items() if k % 2 == 0}

print("Question 11 Output:", even_dict)


# -------------------- Question 12: Dictionary Key and Value Transformation --------------------

dict4 = {x: x**2 for x in range(1, 6)}

# Swap keys and values
swapped_dict = {v: k for k, v in dict4.items()}

print("Question 12 Output:", swapped_dict)


# -------------------- Question 13: Default Dictionary --------------------

from collections import defaultdict

# Default value as empty list
default_dict = defaultdict(list)

# Adding elements
default_dict["a"].append(1)
default_dict["a"].append(2)
default_dict["b"].append(3)

print("Question 13 Output:", dict(default_dict))


# -------------------- Question 14: Counting with Dictionaries --------------------

def count_characters(text):
    count_dict = {}
    for char in text:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict

print("Question 14 Output:", count_characters("hello world"))


# -------------------- Question 15: Dictionary and JSON --------------------

import json

book = {
    "title": "Python Basics",
    "author": "ABC",
    "year": 2023,
    "genre": "Education"
}

# Convert to JSON string
json_string = json.dumps(book)

print("Question 15 Output:", json_string)
