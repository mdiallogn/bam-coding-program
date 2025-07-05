# Session 3 - Python Loops

## Section 1: Basic For Loops

### Activity 1.1: Range-based For Loop

Create a script that demonstrates counting with for loops.

**File: `range_loops.py`**
```python
# Range-based For Loop Examples
print("=== Range-based For Loops ===\n")

# Counting from 1 to 5
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# Counting with steps
print("\nCounting by 2s from 0 to 10:")
for i in range(0, 11, 2):
    print(f"Count: {i}")

# Sum of numbers
print("\nSum of numbers 1-10:")
total = 0
for num in range(1, 11):
    total += num
print(f"Sum: {total}")
```

### Activity 1.2: List Iteration

Practice iterating through lists and using enumerate.

**File: `list_loops.py`**
```python
# List Iteration Examples
print("=== List Iteration ===\n")

# Basic list iteration
fruits = ["apple", "banana", "orange", "grape"]
print("Iterating through a list:")
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Using enumerate
print("\nUsing enumerate:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Working with multiple lists
print("\nZipping two lists:")
colors = ["red", "yellow", "orange", "purple"]
for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")
```

## Section 2: While Loops

### Activity 2.1: Basic While Loop

Learn while loop syntax and counting.

**File: `basic_while.py`**
```python
# Basic While Loop Examples
print("=== Basic While Loops ===\n")

# Simple counting down
print("Counting down:")
count = 5
while count > 0:
    print(f"Count: {count}")
    count -= 1
print("Finished!")

# Accumulating values
print("\nAccumulating values:")
total = 0
num = 1
while num <= 5:
    total += num
    print(f"Adding {num}, total: {total}")
    num += 1
```

### Activity 2.2: Interactive While Loop

Create interactive programs with user input validation.

**File: `interactive_while.py`**
```python
# Interactive While Loop Examples
print("=== Interactive While Loops ===\n")

# Number guessing game
import random
print("Number guessing game:")
secret_number = random.randint(1, 10)
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1-10: "))
    attempts += 1
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempts!")

# Menu system
print("\nSimple menu system:")
choice = ""
while choice != "quit":
    print("\nOptions: info, help, quit")
    choice = input("Enter your choice: ").lower()
    
    if choice == "info":
        print("This is a demo program.")
    elif choice == "help":
        print("Available commands: info, help, quit")
    elif choice == "quit":
        print("Goodbye!")
    else:
        print("Invalid choice. Try again.")
```

## Section 3: Nested Loops

### Activity 3.1: Multiplication Tables

Use nested loops to create multiplication tables.

**File: `multiplication_table.py`**
```python
# Multiplication Table Examples
print("=== Multiplication Tables ===\n")

# Simple multiplication table
print("Multiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{result:2d}", end=" ")
    print()  # New line after each row

# Formatted multiplication table
print("\nFormatted multiplication table:")
print("   ", end="")
for i in range(1, 6):
    print(f"{i:3d}", end="")
print()

for i in range(1, 6):
    print(f"{i:2d} ", end="")
    for j in range(1, 6):
        result = i * j
        print(f"{result:3d}", end="")
    print()
```

### Activity 3.2: Pattern Generation

Create various patterns using nested loops.

**File: `pattern_generator.py`**
```python
# Pattern Generation Examples
print("=== Pattern Generation ===\n")

# Right triangle
print("Right triangle:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Pyramid
print("\nPyramid:")
for i in range(1, 6):
    # Print spaces
    for j in range(5 - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Number pattern
print("\nNumber pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

### Activity 3.3: 2D Data Processing

Work with 2D lists and matrices using nested loops.

**File: `matrix_processing.py`**
```python
# 2D Data Processing Examples
print("=== 2D Data Processing ===\n")

# Working with 2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    for element in row:
        print(f"{element:2d}", end=" ")
    print()

# Calculate sum of all elements
total = 0
for row in matrix:
    for element in row:
        total += element
print(f"Sum of all elements: {total}")

# Find maximum element
max_element = matrix[0][0]
for row in matrix:
    for element in row:
        if element > max_element:
            max_element = element
print(f"Maximum element: {max_element}")
```

## Section 4: Loop Control

### Activity 4.1: Break Statement

Practice using break to exit loops early.

**File: `break_examples.py`**
```python
# Break Statement Examples
print("=== Break Statement ===\n")

# Finding first even number
print("Finding first even number:")
numbers = [1, 3, 7, 8, 11, 12, 15]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
    print(f"Checking: {num}")

# Breaking out of while loop
print("\nBreaking out of while loop:")
count = 0
while True:
    count += 1
    if count > 3:
        print("Breaking out of infinite loop")
        break
    print(f"Count: {count}")
```

### Activity 4.2: Continue Statement

Learn to skip iterations using continue.

**File: `continue_examples.py`**
```python
# Continue Statement Examples
print("=== Continue Statement ===\n")

# Skipping odd numbers
print("Skipping odd numbers:")
for num in range(1, 11):
    if num % 2 == 1:
        continue
    print(f"Even number: {num}")

# Processing only valid data
print("\nProcessing only valid data:")
data = [10, -5, 0, 15, -3, 8]
for value in data:
    if value <= 0:
        print(f"Skipping invalid value: {value}")
        continue
    print(f"Processing: {value}")
```

### Activity 4.3: Nested Loop Control

Control flow in nested loops with break and continue.

**File: `nested_control.py`**
```python
# Nested Loop Control Examples
print("=== Nested Loop Control ===\n")

# Breaking inner loop only
print("Breaking inner loop only:")
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(3):
        if j == 1:
            print("  Breaking inner loop")
            break
        print(f"  Inner loop: {j}")

# Using continue in nested loops
print("\nUsing continue in nested loops:")
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(3):
        if j == 1:
            print("  Skipping inner loop iteration")
            continue
        print(f"  Inner loop: {j}")
```

## Execution Instructions

Run each script to practice different loop concepts:

**Steps:**
1. Create each Python file in your project directory
2. Run the scripts one by one:

```bash
python range_loops.py
python list_loops.py
python basic_while.py
python interactive_while.py
python multiplication_table.py
python pattern_generator.py
python matrix_processing.py
python break_examples.py
python continue_examples.py
python nested_control.py
```

**Learning Objectives:**
- [ ] Understand for loop syntax and usage
- [ ] Master while loop conditions and control
- [ ] Create patterns using nested loops
- [ ] Use break and continue statements effectively
- [ ] Process lists and 2D data structures with loops
- [ ] Build interactive programs with user input
