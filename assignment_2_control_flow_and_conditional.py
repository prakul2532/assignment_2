# -------------------- Question 1: Simple if Statement --------------------

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")


# -------------------- Question 2: if-else Statement --------------------

num = int(input("Enter a number: "))
if num >= 0:
    print("Positive")
else:
    print("Negative")


# -------------------- Question 3: if-elif-else Statement --------------------

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# -------------------- Question 4: Nested if Statement --------------------

num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Negative")


# -------------------- Question 5: for Loop --------------------

for i in range(1, 11):
    print(i)


# -------------------- Question 6: while Loop --------------------

i = 1
while i <= 10:
    print(i)
    i += 1


# -------------------- Question 7: Nested Loops --------------------

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


# -------------------- Question 8: break Statement --------------------

total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Sum:", total)


# ----
