#Q1.) Write a Python program to print "Hello, World!"
print("Hello,World!")
#Q2.) Write a Python program that takes a user input and prints it.
user_input = input("enter anything")
print(user_input)
#Q3.) Write a Python program to check if a number is positive, negative, or zero.
num = int(input("enter a number"))
result = "numis =+ve" if num > 0 else "num is -ve"
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
        factorial = num*(i)
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

