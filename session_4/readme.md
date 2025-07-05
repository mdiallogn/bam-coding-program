# Session 4 - Python Functions

## Section 1: Basic Functions

### Activity 1.1: Defining and Calling Functions

Create simple functions without parameters.

**File: `basic_functions.py`**
```python
# Basic Function Examples
print("=== Basic Functions ===\n")

# Simple function without parameters
def greet():
    print("Hello, World!")
    print("Welcome to Python functions!")

# Function that performs a calculation
def calculate_area():
    length = 5
    width = 3
    area = length * width
    print(f"Area of rectangle: {area}")

# Function with multiple statements
def display_info():
    print("This is a function")
    print("Functions help organize code")
    print("They make code reusable")

# Calling functions
print("Calling greet():")
greet()

print("\nCalling calculate_area():")
calculate_area()

print("\nCalling display_info():")
display_info()
```

### Activity 1.2: Functions with Parameters

Learn to pass data to functions using parameters.

**File: `function_parameters.py`**
```python
# Function Parameters Examples
print("=== Function Parameters ===\n")

# Function with single parameter
def greet_person(name):
    print(f"Hello, {name}!")

# Function with multiple parameters
def calculate_rectangle_area(length, width):
    area = length * width
    print(f"Rectangle area: {length} x {width} = {area}")

# Function with default parameters
def greet_with_title(name, title="Mr./Ms."):
    print(f"Hello, {title} {name}!")

# Function with mixed parameters
def create_profile(name, age, city="Unknown"):
    print(f"Profile: {name}, {age} years old, from {city}")

# Calling functions with parameters
print("Single parameter:")
greet_person("Alice")
greet_person("Bob")

print("\nMultiple parameters:")
calculate_rectangle_area(4, 6)
calculate_rectangle_area(10, 2)

print("\nDefault parameters:")
greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")

print("\nMixed parameters:")
create_profile("Alice", 25)
create_profile("Bob", 30, "New York")
```

## Section 2: Return Values

### Activity 2.1: Functions that Return Values

Create functions that return results instead of printing.

**File: `return_values.py`**
```python
# Return Values Examples
print("=== Return Values ===\n")

# Function returning a single value
def add_numbers(a, b):
    return a + b

# Function returning calculated result
def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area

# Function returning multiple values
def get_name_info(full_name):
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1]
    return first_name, last_name

# Function with conditional return
def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Using return values
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
