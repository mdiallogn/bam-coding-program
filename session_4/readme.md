# Session 4 - Python Functions

## Section 1: Basic Functions

### Activity 1.1: Simple Functions

Create and use basic functions.

**File: `basic_functions.py`**
```python
# Basic Function Examples
print("=== Basic Functions ===\n")

# Simple function
def say_hello():
    print("Hello!")

# Function with parameter
def greet(name):
    print(f"Hello, {name}!")

# Function that returns a value
def add_numbers(a, b):
    return a + b

# Using functions
say_hello()
greet("Alice")
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")
```

### Activity 1.2: Functions with Parameters

Learn to pass data to functions.

**File: `function_practice.py`**
```python
# Function Practice
print("=== Function Practice ===\n")

# Calculate area
def rectangle_area(length, width):
    return length * width

# Check if number is even
def is_even(number):
    return number % 2 == 0

# Create greeting
def make_greeting(name, age):
    return f"Hi, I'm {name} and I'm {age} years old"

# Test functions
area = rectangle_area(5, 3)
print(f"Rectangle area: {area}")

print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")

greeting = make_greeting("Bob", 16)
print(greeting)
```

## Section 2: Function Applications

### Activity 2.1: Simple Calculator with Functions

Build a calculator using functions.

**File: `calculator_functions.py`**
```python
# Calculator with Functions
print("=== Calculator with Functions ===\n")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Simple calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    print("Invalid operation!")
    exit()

print(f"Result: {result}")
```

## Execution Instructions

Run each script to practice functions:

```bash
python basic_functions.py
python function_practice.py
python calculator_functions.py
```

**Learning Goals:**
- [ ] Create and call functions
- [ ] Use parameters and return values
- [ ] Apply functions to solve problems
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Using return values

```python
print("Addition result:")
result = add_numbers(15, 25)
print(f"15 + 25 = {result}")

print("\nCircle area:")
area = calculate_circle_area(5)
print(f"Area of circle with radius 5: {area:.2f}")

print("\nMultiple return values:")
first, last = get_name_info("John Doe Smith")
print(f"First name: {first}, Last name: {last}")

print("\nGrade checking:")
grades = [95, 87, 73, 65, 45]
for score in grades:
    grade = check_grade(score)
    print(f"Score {score}: Grade {grade}")
```

### Activity 2.2: Function Return Types

Explore different types of return values.

**File: `return_types.py`**
```python
# Return Types Examples
print("=== Return Types ===\n")

# Returning strings
def format_name(first, last):
    return f"{first} {last}".title()

# Returning lists
def get_even_numbers(max_num):
    evens = []
    for i in range(2, max_num + 1, 2):
        evens.append(i)
    return evens

# Returning dictionaries
def create_student_record(name, age, grade):
    return {
        "name": name,
        "age": age,
        "grade": grade,
        "id": f"STU{age}{grade}"
    }

# Returning boolean
def is_even(number):
    return number % 2 == 0

# Using different return types
print("String return:")
full_name = format_name("john", "doe")
print(f"Formatted name: {full_name}")

print("\nList return:")
even_nums = get_even_numbers(10)
print(f"Even numbers up to 10: {even_nums}")

print("\nDictionary return:")
student = create_student_record("Alice", 20, "A")
print(f"Student record: {student}")

print("\nBoolean return:")
numbers = [4, 7, 10, 13]
for num in numbers:
    result = is_even(num)
    print(f"{num} is even: {result}")
```

## Section 3: Function Scope

### Activity 3.1: Local vs Global Variables

Understand variable scope in functions.

**File: `variable_scope.py`**
```python
# Variable Scope Examples
print("=== Variable Scope ===\n")

# Global variable
global_var = "I'm global"

def demonstrate_local():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

def modify_global():
    global global_var
    global_var = "I'm modified global"
    print(f"Modified global inside function: {global_var}")

def shadow_global():
    # This creates a local variable that shadows the global
    global_var = "I'm local shadow"
    print(f"Shadow variable: {global_var}")

# Demonstrating scope
print("Before function calls:")
print(f"Global variable: {global_var}")

print("\nCalling demonstrate_local():")
demonstrate_local()

print(f"\nAfter demonstrate_local() - Global: {global_var}")

print("\nCalling modify_global():")
modify_global()
print(f"After modify_global() - Global: {global_var}")

print("\nCalling shadow_global():")
shadow_global()
print(f"After shadow_global() - Global: {global_var}")
```

### Activity 3.2: Function Arguments and Scope

Explore how parameters affect variable scope.

**File: `parameter_scope.py`**
```python
# Parameter Scope Examples
print("=== Parameter Scope ===\n")

def modify_parameter(value):
    print(f"Original parameter: {value}")
    value = value * 2
    print(f"Modified parameter: {value}")
    return value

def modify_list(lst):
    print(f"Original list: {lst}")
    lst.append("new item")
    print(f"Modified list: {lst}")

def safe_list_modify(lst):
    # Create a copy to avoid modifying original
    new_list = lst.copy()
    new_list.append("safe item")
    return new_list

# Testing parameter modifications
print("Testing with immutable types:")
original_num = 10
result = modify_parameter(original_num)
print(f"Original after function: {original_num}")
print(f"Returned value: {result}")

print("\nTesting with mutable types:")
original_list = [1, 2, 3]
print(f"List before function: {original_list}")
modify_list(original_list)
print(f"List after function: {original_list}")

print("\nSafe list modification:")
test_list = [1, 2, 3]
safe_result = safe_list_modify(test_list)
print(f"Original list: {test_list}")
print(f"Safe result: {safe_result}")
```

## Section 4: Advanced Functions

### Activity 4.1: Recursion

Understand recursive functions.

**File: `recursion_examples.py`**
```python
# Recursion Examples
print("=== Recursion Examples ===\n")

# Factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Countdown function
def countdown(n):
    if n <= 0:
        print("Blast off!")
    else:
        print(f"Counting down: {n}")
        countdown(n - 1)

# Sum of list using recursion
def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

# Testing recursive functions
print("Factorial examples:")
for i in range(6):
    print(f"{i}! = {factorial(i)}")

print("\nFibonacci sequence:")
for i in range(8):
    print(f"F({i}) = {fibonacci(i)}")

print("\nCountdown:")
countdown(5)

print("\nSum of list:")
test_list = [1, 2, 3, 4, 5]
total = sum_list(test_list)
print(f"Sum of {test_list} = {total}")
```

## Execution Instructions

Run each script to practice different function concepts:

**Steps:**
1. Create each Python file in your project directory
2. Run the scripts one by one:

```bash
python basic_functions.py
python function_parameters.py
python return_values.py
python return_types.py
python variable_scope.py
python parameter_scope.py
python lambda_functions.py
python recursion_examples.py
```

**Learning Objectives:**
- [ ] Define and call basic functions
- [ ] Use parameters and default values
- [ ] Return values from functions
- [ ] Understand variable scope (local vs global)
- [ ] Work with lambda functions
- [ ] Implement recursive functions
- [ ] Apply functions to solve problems
