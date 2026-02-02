#Q1.) Write a Python program to print "Hello, World!"
print("Hello,World!")
#Q2.) Write a Python program that takes a user input and prints it.
user_input = input("enter anything")
print(user_input)
#Q3.) Write a Python program to check if a number is positive, negative, or zero.
num = int(input("enter a number"))
result = "num is =+ve" if num > 0 else "num is -ve"
print(result)
#Q4.) Write a Python program to find the largest of three numbers.
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))
max = num1
if num2 > num1:
    max = num2
elif num3 > num1:
    max = num3
else:
    max = num1
print("the maximum value is ", max)
#Q5.) Write a Python program to calculate the factorial of a number.
num = int(input("enter the value :"))
if num == 0 or num == 1:
    print(f"factorial of {num} is 1")
else:
    i=1
    while(i<num):
        factorial = num*i
        i += 1
    print(f"the factorial of {num} is {factorial}")
#Q6.) Create variables of different data types: integer, float, string, and boolean. Print their values and types.
data1 = 23
data2 = 23.4
data3 = "Hello world"
data4 = True
print(f"{data1},type:- {type(data1)}; {data2},type:- {type(data2)}; {data3},type:- {type(data3)}; {data4}, type:- {type(data4)}")
#Q7.) Write a Python program to swap the values of two variables.
data1 = "string"
data2 = 23
print(f"{data1}, {data2} initially {type(data1)} , {type(data2)}")
data2 = "string"
data1 = 23
print(f"{data1}, {data2} second {type(data1)} , {type(data2)}")
#Q8.) Write a Python program to check if a variable is of a specific data type.
data = 67
result = "integer" if type(data) == int else "string"
print(result)
#Q9.) Write a Python program to convert Celsius to Fahrenheit.
celsius = float(input("enter the value of temperature in celsius :- "))
fahrenheit = 9/5 * celsius +32
print("The temperature in fahrenheit is: ", fahrenheit)
#Q10.) Write a Python program to concatenate two strings.
string1 = "hello "
string2 = "world"
print(string1+string2)
#Q11.) Write a Python program to perform arithmetic operations: addition, subtraction, multiplication, and division.
num1 = int(input("Enter the 1st number:- "))
num2 = int(input("Enter the 2nd number:- "))
addition = num1 + num2
subtraction = max(num1, num2) - min(num1, num2)
multiplication = num1 * num2
division = num1 / num2
print(f"the addition of {num1} and {num2} is: {addition}")
print(f"the subtraction of {max(num1,num2)} and {min(num1,num2)} is : {subtraction}")
print(f"the multiplication of {num1} and {num2} is : {multiplication}")
print(f"the division of {num1} and {num2} is : {division}")
#Q12.) Write a Python program to demonstrate comparison operators: equal to, not equal to, greater than, less than.
num1 = int(input("enter the 1st number:- "))
num2 = int(input("Enter the 2nd number:- "))
if num1 != num2:
    print("num1 is not equal to num2")
elif num1 == num2:
    print("num1 is equal to num2")
elif num1 > num2:
    print("num1 is greater than num2")
elif num1 < num2:
    print("num2 is greater than num2")
#Q13.) Write a Python program to demonstrate logical operators: and, or, not.
num1 = int(input("Enter the 1st number:- "))
num2 = int(input("Enter the 2nd number:- "))
if num1 != num2 and num1 > num2:
    print("num1 is greater than num2")
elif num1 != num2 and num1 < num2:
    print("num2 is greater than num1")
elif num1 == num2 or 1<2:
    print("num1 is equal to num2")
lst1 = [1,2,3]
if num1 not in lst1:
    print("num1 is not in lst1")
else:
    print("num1 is in lst1")
#Q14.) Write a Python program to calculate the square of a number.
num = int(input("enter the number whose square you want to print :- "))
print(f"the square of the number is :- {num**2}")
#Q15.) Write a Python program to check if a number is even or odd.
num = int(input("enter the number :-"))
is_even = True
if num % 2 == 0:
    is_even = True
else:
    is_even = False
print(is_even)
#Q16.) Write a Python program to find the sum of the first n natural numbers.
total_number = int(input("enter the number :-"))
sum = 0
for i in range(0,total_number):
    sum = sum + i
print(sum)
#Q17.) Write a Python program to check if a year is a leap year.
year = int(input("enter the year :- "))
if year % 4 == 0 :
    print(f"{year} is an leap year")
else :
    print(f"{year} is not a leap year")
#Q18.) Write a Python program to reverse a string.
Random_string = input("enter a random word :- ")
list1 = list(Random_string)
list2 = []
for i in range(0, len(list1)):
    list2.append(list1[4-i])
new_string = "".join(list2)
print(new_string)
#Q19.) Write a Python program to check if a string is a palindrome
Random_string = input("enter a random word :- ")
if Random_string == Random_string[::-1]:
    print(f"{Random_string} is a palindrome ")
else :
    print(f"{Random_string} is not a palindrome")
#Q20.) Write a Python program to sort a list of numbers in ascending order.
list1 = [2, 3, 1, 5]
list2 = []
for i in range(len(list1)):
    max_num = list1[0]
    for x in list1:
        if x > max_num:
            max_num = x
    list2.append(max_num)
    list1.remove(max_num)
print(list2)


