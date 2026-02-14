# -------------------- Question 1: Handling Division by Zero --------------------

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero.")
    finally:
        print("Division operation completed.")

print("Question 1 Output:", divide(10, 2))
divide(10, 0)


# -------------------- Question 2: File Reading with Exception Handling --------------------

def read_file():
    file = None
    try:
        file = open("data.txt", "r")
        content = file.read()
        return content
    except FileNotFoundError:
        print("Error: File not found.")
    finally:
        if file:
            file.close()
        print("File handling completed.")

print("Question 2 Output:", read_file())


# -------------------- Question 3: Handling Multiple Exceptions --------------------

def sum_list(numbers):
    total = 0
    try:
        for num in numbers:
            total += num
        return total
    except TypeError:
        print("Error: Non-integer value encountered.")
    finally:
        print("Sum operation completed.")

print("Question 3 Output:", sum_list([1, 2, 3]))
sum_list([1, "a", 3])


# -------------------- Question 4: Exception Handling in User Input --------------------

def get_integer():
    try:
        value = int(input("Enter an integer: "))
        return value
    except ValueError:
        print("Error: Invalid integer.")
    finally:
        print("Input operation completed.")

print("Question 4 Output:", get_integer())


# -------------------- Question 5: Exception Handling in Dictionary Access --------------------

def get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print("Error: Key not found.")
    finally:
        print("Dictionary access completed.")

print("Question 5 Output:", get_value({"a":1, "b":2}, "a"))
get_value({"a":1}, "z")


# -------------------- Question 6: Nested Exception Handling --------------------

def nested_exception(value):
    try:
        try:
            num = int(value)
        except ValueError:
            print("Error: Invalid integer conversion.")
            return
        try:
            result = 10 / num
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Division by zero.")
    finally:
        print("Nested operation completed.")

print("Question 6 Output:")
nested_exception("5")
nested_exception("0")
nested_exception("abc")


# -------------------- Question 7: Exception Handling in List Operations --------------------

def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        print("Error: Index out of range.")
    finally:
        print("List access completed.")

print("Question 7 Output:", get_element([10,20,30], 1))
get_element([10,20,30], 5)


# -------------------- Question 8: Exception Handling in Network Operations --------------------

import urllib.request

def open_url(url):
    try:
        response = urllib.request.urlopen(url)
        return response.read()
    except Exception:
        print("Error: Network operation failed.")
    finally:
        print("Network operation completed.")

print("Question 8 Output:", open_url("http://example.com"))


# -------------------- Question 9: Exception Handling in JSON Parsing --------------------

import json

def parse_json(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        print("Error: Invalid JSON.")
    finally:
        print("JSON parsing completed.")

print("Question 9 Output:", parse_json('{"a":1}'))
parse_json("invalid json")


# -------------------- Question 10: Custom Exception Handling --------------------

class NegativeNumberError(Exception):
    pass

def check_numbers(numbers):
    try:
        for num in numbers:
            if num < 0:
                raise NegativeNumberError("Negative number found.")
        print("All numbers are positive.")
    except NegativeNumberError as e:
        print("Error:", e)
    finally:
        print("Custom exception handling completed.")

print("Question 10 Output:")
check_numbers([1,2,3])
check_numbers([1,-5,3])


# -------------------- Question 11: Exception Handling in Function Calls --------------------

def risky_function():
    raise ValueError("Something went wrong.")

def caller():
    try:
        risky_function()
    except ValueError as e:
        print("Error:", e)
    finally:
        print("Function call completed.")

print("Question 11 Output:")
caller()


# -------------------- Question 12: Exception Handling in Class Methods --------------------

class Calculator:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Division by zero.")
        finally:
            print("Division method completed.")

calc = Calculator()
print("Question 12 Output:", calc.divide(10,2))
calc.divide(10,0)


# -------------------- Question 13: Exception Handling in Data Conversion --------------------

def convert_list(strings):
    result = []
    for s in strings:
        try:
            result.append(int(s))
        except ValueError:
            print(f"Error: Cannot convert '{s}'")
        finally:
            pass
    return result

print("Question 13 Output:", convert_list(["1","2","a","4"]))


# -------------------- Question 14: Exception Handling in List Comprehensions --------------------

def safe_convert(strings):
    result = []
    for s in strings:
        try:
            result.append(int(s))
        except ValueError:
            print(f"Error: Cannot convert '{s}'")
        finally:
            pass
    return result

print("Question 14 Output:", safe_convert(["5","x","7"]))


# -------------------- Question 15: Exception Handling in File Writing --------------------

def write_file(lines):
    file = None
    try:
        file = open("output.txt", "w")
        for line in lines:
            file.write(line + "\n")
        print("Write successful.")
    except IOError:
        print("Error: File writing failed.")
    finally:
        if file:
            file.close()
        print("File write operation completed.")

print("Question 15 Output:")
write_file(["Hello", "World"])
