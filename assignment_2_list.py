# -------------------- Question 1: Creating and Accessing Lists --------------------

# List of first 20 positive integers
list1 = list(range(1, 21))
print("Question 1 Output:", list1)


# -------------------- Question 2: Accessing List Elements --------------------

first = list1[0]
middle = list1[len(list1)//2]
last = list1[-1]

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# -------------------- Question 3: List Slicing --------------------

print("First 5:", list1[:5])
print("Last 5:", list1[-5:])
print("Index 5 to 15:", list1[5:16])


# -------------------- Question 4: List Comprehensions --------------------

square_list = [x**2 for x in range(1, 11)]
print("Question 4 Output:", square_list)


# -------------------- Question 5: Filtering Lists --------------------

even_list = [x for x in list1 if x % 2 == 0]
print("Question 5 Output:", even_list)


# -------------------- Question 6: List Methods --------------------

import random

random_list = [random.randint(1, 10) for _ in range(15)]
print("Original List:", random_list)

# Ascending sort
asc_list = sorted(random_list)
print("Ascending:", asc_list)

# Descending sort
desc_list = sorted(random_list, reverse=True)
print("Descending:", desc_list)

# Remove duplicates
unique_list = list(set(random_list))
print("Without Duplicates:", unique_list)


# -------------------- Question 7: Nested Lists --------------------

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Question 7 Output:", matrix)

# Element at 2nd row, 3rd column
print("Element (2nd row, 3rd column):", matrix[1][2])


# -------------------- Question 8: List of Dictionaries --------------------

students = [
    {"name": "A", "score": 85},
    {"name": "B", "score": 92},
    {"name": "C", "score": 78}
]

# Sort by score descending
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)

print("Question 8 Output:", sorted_students)


# -------------------- Question 9: Matrix Transposition --------------------

def transpose(matrix):
    return [[matrix[j][i] for j in range(3)] for i in range(3)]

original_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transposed_matrix = transpose(original_matrix)

print("Original Matrix:", original_matrix)
print("Transposed Matrix:", transposed_matrix)


# -------------------- Question 10: Flattening a Nested List --------------------

def flatten(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

nested = [1, [2, 3], [4, [5, 6]], 7]

print("Original Nested List:", nested)
print("Flattened List:", flatten(nested))


# -------------------- Question 11: List Manipulation --------------------

list2 = list(range(1, 11))

# Remove indices 6, 4, 2 (reverse order to avoid shifting)
for index in sorted([2,4,6], reverse=True):
    list2.pop(index)

# Insert 99 at index 5
list2.insert(5, 99)

print("Question 11 Output:", list2)


# -------------------- Question 12: List Zipping --------------------

listA = [1,2,3,4]
listB = ["a","b","c","d"]

zipped = list(zip(listA, listB))

print("Question 12 Output:", zipped)


# -------------------- Question 13: List Reversal --------------------

def reverse_list(lst):
    return lst[::-1]

print("Original List:", list1)
print("Reversed List:", reverse_list(list1))


# -------------------- Question 14: List Rotation --------------------

def rotate_list(lst, n):
    n = n % len(lst)
    return lst[n:] + lst[:n]

print("Original List:", list1)
print("Rotated List by 3:", rotate_list(list1, 3))


# -------------------- Question 15: List Intersection --------------------

def list_intersection(listA, listB):
    return list(set(listA) & set(listB))

print("Question 15 Output:", list_intersection([1,2,3,4], [3,4,5,6]))
