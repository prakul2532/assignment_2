# -------------------- Question 1: Fibonacci Sequence with Memoization --------------------

def fibonacci(n, memo={}):  # memo dictionary for storing results
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print("Question 1 Output:")
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(15))


# -------------------- Question 2: Function with Nested Default Arguments --------------------

def add_to_dict(a, b=None):  # avoid mutable default directly
    if b is None:
        b = {}
    b[a] = len(b) + 1
    return b

print("\nQuestion 2 Output:")
print(add_to_dict("x"))
print(add_to_dict("y", {"a":1}))


# -------------------- Question 3: Function with Variable Keyword Arguments --------------------

def filter_integers(**kwargs):
    return {k: v for k, v in kwargs.items() if isinstance(v, int)}

print("\nQuestion 3 Output:")
print(filter_integers(a=1, b="hello", c=3, d=4.5))


# -------------------- Question 4: Function with Callback --------------------

def apply_callback(callback, numbers):
    return [callback(x) for x in numbers]

def square(x):
    return x*x

def double(x):
    return x*2

print("\nQuestion 4 Output:")
print(apply_callback(square, [1,2,3]))
print(apply_callback(double, [4,5,6]))


# -------------------- Question 5: Function that Returns a Function --------------------

def outer_function():
    def inner_function(x):
        return x*x
    return inner_function

square_func = outer_function()

print("\nQuestion 5 Output:")
print(square_func(5))
print(square_func(8))


# -------------------- Question 6: Function with Decorators --------------------

import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start)
        return result
    return wrapper

@time_decorator
def complex_calculation(n):
    total = 0
    for i in range(n):
        total += i**2
    return total

print("\nQuestion 6 Output:")
print(complex_calculation(100000))
print(complex_calculation(200000))


# -------------------- Question 7: Higher-Order Function for Filtering and Mapping --------------------

def higher_order(filter_func, map_func, numbers):
    filtered = list(filter(filter_func, numbers))
    return list(map(map_func, filtered))

print("\nQuestion 7 Output:")
print(higher_order(lambda x: x%2==0, lambda x: x*10, [1,2,3,4,5]))
print(higher_order(lambda x: x>3, lambda x: x+1, [1,2,3,4,5]))


# -------------------- Question 8: Function Composition --------------------

def compose(f, g):
    return lambda x: f(g(x))

def add_two(x):
    return x + 2

def multiply_three(x):
    return x * 3

composed = compose(add_two, multiply_three)

print("\nQuestion 8 Output:")
print(composed(5))
print(composed(10))


# -------------------- Question 9: Partial Function Application --------------------

from functools import partial

def multiply(a, b):
    return a * b

double_func = partial(multiply, 2)

print("\nQuestion 9 Output:")
print(double_func(5))
print(double_func(12))


# -------------------- Question 10: Function with Error Handling --------------------

def average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except:
        return None

print("\nQuestion 10 Output:")
print(average([1,2,3,4]))
print(average([]))


# -------------------- Question 11: Function with Generators --------------------

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\nQuestion 11 Output:")
gen = fibonacci_generator()
for _ in range(10):
    print(next(gen))


# -------------------- Question 12: Currying --------------------

def curried_product(a):
    def second(b):
        def third(c):
            return a * b * c
        return third
    return second

print("\nQuestion 12 Output:")
print(curried_product(2)(3)(4))
print(curried_product(5)(6)(2))


# -------------------- Question 13: Function with Context Manager --------------------

def write_to_file(numbers, filename):
    try:
        with open(filename, "w") as file:  # context manager
            for num in numbers:
                file.write(str(num) + "\n")
        return True
    except:
        return False

print("\nQuestion 13 Output:")
print(write_to_file([1,2,3,4], "output1.txt"))
print(write_to_file([], "output2.txt"))


# -------------------- Question 14: Function with Multiple Return Types --------------------

def separate_types(data):
    ints = [x for x in data if isinstance(x, int)]
    strings = [x for x in data if isinstance(x, str)]
    floats = [x for x in data if isinstance(x, float)]
    return ints, strings, floats

print("\nQuestion 14 Output:")
print(separate_types([1, "hello", 3.5, 2, "world", 4.2]))


# -------------------- Question 15: Function with State --------------------

def call_counter(counter=[0]):  # mutable default to maintain state
    counter[0] += 1
    return counter[0]

print("\nQuestion 15 Output:")
print(call_counter())
print(call_counter())
print(call_counter())
