#Question 1: Creating and Accessing Sets --------------------

# Creating a set with first 10 positive integers
set1 = {1,2,3,4,5,6,7,8,9,10}
print("Question 1 Output:", set1)


#Question 2: Adding and Removing Elements --------------------

# Adding 11
set1.add(11)

# Removing 1
set1.remove(1)

print("Question 2 Output:", set1)


#Question 3: Set Operations --------------------

# First 5 positive integers
setA = {1,2,3,4,5}

# First 5 even integers
setB = {2,4,6,8,10}

# Union
print("Union:", setA.union(setB))

# Intersection
print("Intersection:", setA.intersection(setB))

# Difference
print("Difference (A - B):", setA.difference(setB))

# Symmetric Difference
print("Symmetric Difference:", setA.symmetric_difference(setB))


#Question 4: Set Comprehensions --------------------

# Squares of first 10 positive integers
square_set = {x**2 for x in range(1,11)}
print("Question 4 Output:", square_set)


#Question 5: Filtering Sets --------------------

# Even numbers from set1
even_set = {x for x in set1 if x % 2 == 0}
print("Question 5 Output:", even_set)


#Question 6: Set Methods --------------------

# Set with duplicates (duplicates removed automatically)
dup_set = {1,2,2,3,4,4,5}
print("Question 6 Output:", dup_set)


#Question 7: Subsets and Supersets --------------------

setC = {1,2,3,4,5}
setD = {1,2,3}

print("Is D subset of C?", setD.issubset(setC))
print("Is C superset of D?", setC.issuperset(setD))


#Question 8: Frozenset --------------------

# Creating frozenset
frozen = frozenset({1,2,3,4,5})
print("Question 8 Output:", frozen)


#Question 9: Set and List Conversion --------------------

setE = {1,2,3,4,5}

# Convert to list
listE = list(setE)

# Append 6
listE.append(6)

# Convert back to set
setE = set(listE)

print("Question 9 Output:", setE)


#Question 10: Set and Dictionary --------------------

# Using frozenset as dictionary keys (sets are not allowed as keys)
dict_set = {
    frozenset({1,2}): 10,
    frozenset({3,4}): 20
}

print("Question 10 Output:", dict_set)


#Question 11: Iterating Over Sets --------------------

setF = {10,20,30,40}

print("Question 11 Output:")
for item in setF:
    print(item)


#Question 12: Removing Elements from Sets --------------------

setG = {1,2,3,4}

print("Question 12 Output:")
while setG:
    removed = setG.pop()   # Removes random element
    print("Removed:", removed, "Remaining Set:", setG)


#Question 13: Set Symmetric Difference Update --------------------

setH = {1,2,3,4}
setI = {3,4,5,6}

# Update setH with symmetric difference
setH.symmetric_difference_update(setI)

print("Question 13 Output:", setH)


#Question 14: Set Membership Testing --------------------

setJ = {5,10,15,20}

print("Is 10 present?", 10 in setJ)
print("Is 25 present?", 25 in setJ)


#Question 15: Set of Tuples --------------------

# Creating set of tuples
tuple_set = {(1,2), (3,4), (5,6)}

print("Question 15 Output:", tuple_set)
