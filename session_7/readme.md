# Session 7 - Python Debugging and Error Handling

## What You'll Learn Today
- [ ] How to identify and fix syntax errors
- [ ] How to handle runtime exceptions
- [ ] How to spot and correct logical errors

---

## Part 1: Syntax Errors - Grammar Problems

Syntax errors happen when Python can't understand your code because it doesn't follow the rules.

### Activity 1.1: Common Syntax Errors

Learn to spot and fix basic syntax mistakes.

**File: `syntax_errors.py`**
```python
# Syntax Errors - Let's fix the grammar!
print("=== Fixing Syntax Errors ===\n")

# Example 1: Missing quotes
print("Hello World")  # Correct
# print(Hello World)  # ERROR: Missing quotes

# Example 2: Missing parentheses
print("Python is fun")  # Correct
# print "Python is fun"  # ERROR: Missing parentheses

# Example 3: Incorrect indentation
if True:
    print("This is indented correctly")  # Correct
# print("This is wrong")  # ERROR: Should be indented

# Example 4: Missing colon
for i in range(3):  # Correct
    print(i)
# for i in range(3)  # ERROR: Missing colon

# Example 5: Unmatched brackets
my_list = [1, 2, 3]  # Correct
# my_list = [1, 2, 3  # ERROR: Missing closing bracket

print("All syntax errors fixed!")
```

### Activity 1.2: Debugging Syntax Errors

Practice finding and fixing syntax problems.

**File: `syntax_practice.py`**
```python
# Syntax Practice - Fix these errors!
print("=== Syntax Debugging Practice ===\n")

# Fix these examples (uncomment and correct):

# Example 1: Fix the missing quotes
name = "Alice"
print(f"Hello {name}")

# Example 2: Fix the indentation
age = 16
if age >= 16:
    print("You can drive!")

# Example 3: Fix the missing colon and parentheses
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")

# Example 4: Fix the bracket mismatch
student_info = {"name": "Bob", "grade": "A"}
print(student_info["name"])

print("Great job fixing syntax errors!")
```

---

## Part 2: Runtime Exceptions - Problems During Execution

Runtime exceptions happen when your code runs but encounters problems it can't handle.

### Activity 2.1: Common Runtime Exceptions

Learn about errors that happen while your program is running.

**File: `runtime_exceptions.py`**
```python
# Runtime Exceptions - Handling problems during execution
print("=== Runtime Exceptions ===\n")

# Example 1: Division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    result = 0

# Example 2: File not found
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
    content = ""

# Example 3: Index out of range
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: Index out of range!")

# Example 4: Key not found in dictionary
student = {"name": "Alice", "age": 16}
try:
    print(student["grade"])
except KeyError:
    print("Error: Key not found in dictionary!")

# Example 5: Type error
try:
    result = "5" + 3
except TypeError:
    print("Error: Cannot add string and number!")
    result = int("5") + 3
    print(f"Fixed result: {result}")

print("Runtime exceptions handled successfully!")
```

### Activity 2.2: Exception Handling Practice

Practice catching and handling different types of exceptions.

**File: `exception_practice.py`**
```python
# Exception Handling Practice
print("=== Exception Handling Practice ===\n")

def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        return a / b
    except ZeroDivisionError:
        print("Warning: Division by zero!")
        return 0

def safe_list_access(lst, index):
    """Safely access list item"""
    try:
        return lst[index]
    except IndexError:
        print(f"Warning: Index {index} out of range!")
        return None

def safe_convert_to_int(value):
    """Safely convert to integer"""
    try:
        return int(value)
    except ValueError:
        print(f"Warning: Cannot convert '{value}' to integer!")
        return 0

# Test the functions
print("Testing safe functions:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

test_list = [1, 2, 3]
print(f"List[1] = {safe_list_access(test_list, 1)}")
print(f"List[5] = {safe_list_access(test_list, 5)}")

print(f"Convert '123' = {safe_convert_to_int('123')}")
print(f"Convert 'abc' = {safe_convert_to_int('abc')}")
```

---

## Part 3: Logical Errors - Wrong Results

Logical errors don't crash your program, but they give wrong answers.

### Activity 3.1: Finding Logical Errors

Learn to spot when your code works but gives wrong results.

**File: `logical_errors.py`**
```python
# Logical Errors - When code works but results are wrong
print("=== Finding Logical Errors ===\n")

# Example 1: Wrong comparison operator
def is_passing_grade(score):
    """Check if score is passing (60 or above)"""
    # Wrong: return score > 60  # This excludes exactly 60
    return score >= 60  # Correct: includes 60

# Example 2: Off-by-one error
def count_items(items):
    """Count items in a list"""
    count = 0
    # Wrong: for i in range(len(items) - 1):  # Misses last item
    for i in range(len(items)):  # Correct: includes all items
        count += 1
    return count

# Example 3: Wrong calculation
def calculate_average(numbers):
    """Calculate average of numbers"""
    total = sum(numbers)
    # Wrong: return total / (len(numbers) - 1)  # Wrong denominator
    return total / len(numbers)  # Correct: divide by actual count

# Example 4: Wrong loop condition
def print_countdown(n):
    """Print countdown from n to 1"""
    # Wrong: while n > 1:  # Stops at 2, doesn't print 1
    while n > 0:  # Correct: goes down to 1
        print(n)
        n -= 1

# Test the corrected functions
print("Testing logical error fixes:")
print(f"Is 60 passing? {is_passing_grade(60)}")
print(f"Count of [1,2,3]: {count_items([1,2,3])}")
print(f"Average of [10,20,30]: {calculate_average([10,20,30])}")
print("Countdown from 3:")
print_countdown(3)
```

### Activity 3.2: Debugging with Print Statements

Use print statements to understand what your code is doing.

**File: `debug_with_print.py`**
```python
# Debug with Print Statements
print("=== Debugging with Print Statements ===\n")

def find_max_number(numbers):
    """Find the maximum number in a list"""
    print(f"DEBUG: Input list: {numbers}")
    
    if not numbers:
        print("DEBUG: Empty list detected")
        return None
    
    max_num = numbers[0]
    print(f"DEBUG: Starting with max_num = {max_num}")
    
    for i, num in enumerate(numbers[1:], 1):
        print(f"DEBUG: Checking position {i}, value {num}")
        if num > max_num:
            print(f"DEBUG: New maximum found: {num}")
            max_num = num
        else:
            print(f"DEBUG: {num} is not greater than {max_num}")
    
    print(f"DEBUG: Final maximum: {max_num}")
    return max_num

def calculate_grade_average(grades):
    """Calculate average grade"""
    print(f"DEBUG: Calculating average for: {grades}")
    
    total = 0
    for grade in grades:
        print(f"DEBUG: Adding {grade}, total now: {total + grade}")
        total += grade
    
    average = total / len(grades)
    print(f"DEBUG: Total: {total}, Count: {len(grades)}, Average: {average}")
    return average

# Test with debug output
test_numbers = [3, 7, 2, 9, 1]
max_result = find_max_number(test_numbers)
print(f"Maximum number: {max_result}\n")

test_grades = [85, 92, 78, 90]
avg_result = calculate_grade_average(test_grades)
print(f"Average grade: {avg_result:.1f}")
```

---

## How to Run Your Code

```bash
python syntax_errors.py
python syntax_practice.py
python runtime_exceptions.py
python exception_practice.py
python logical_errors.py
python debug_with_print.py
python performance_issues.py
python memory_efficiency.py
```

---

## Quick Reference

### Common Error Types
```python
# Syntax Errors
# - Missing quotes, parentheses, colons
# - Wrong indentation
# - Unmatched brackets

# Runtime Exceptions
try:
    # risky code
    pass
except SpecificError:
    # handle specific error
    pass
except:
    # handle any other error
    pass

# Logical Errors
# - Wrong comparisons (> vs >=)
# - Off-by-one errors
# - Wrong calculations
```

### Debugging Tips
```python
# Use print statements
print(f"DEBUG: variable = {variable}")

# Check types
print(f"Type: {type(variable)}")

# Check values at different points
print(f"Before: {value}")
# ... code ...
print(f"After: {value}")
```

---

## What's Next?

Apply your knowledge on the capstone project

**Remember:** Every programmer deals with bugs. The key is learning how to find and fix them quickly!