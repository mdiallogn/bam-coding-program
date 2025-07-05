# Session 5 - Understanding Data Structures in Python: Arrays, Lists, and Dictionaries

## Section 1: Working with Lists

### Activity 1.1: List Basics and Creation

Learn different ways to create and initialize lists.

**File: `list_basics.py`**
```python
# List Basics Examples
print("=== List Basics ===\n")

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
nested_list = [[1, 2], [3, 4], [5, 6]]

print("Different types of lists:")
print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed_list}")
print(f"Nested list: {nested_list}")

# List creation methods
range_list = list(range(1, 6))
repeated_list = [0] * 5
string_list = list("hello")

print(f"\nFrom range: {range_list}")
print(f"Repeated elements: {repeated_list}")
print(f"From string: {string_list}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
evens = [x for x in range(1, 11) if x % 2 == 0]

print(f"Squares: {squares}")
print(f"Even numbers: {evens}")
```

### Activity 1.2: List Operations and Methods

Explore list manipulation methods and operations.

**File: `list_operations.py`**
```python
# List Operations Examples
print("=== List Operations ===\n")

# Initialize a list
fruits = ["apple", "banana", "orange"]
print(f"Original list: {fruits}")

# Adding elements
fruits.append("grape")
print(f"After append: {fruits}")

fruits.insert(1, "kiwi")
print(f"After insert: {fruits}")

fruits.extend(["mango", "pear"])
print(f"After extend: {fruits}")

# Removing elements
fruits.remove("banana")
print(f"After remove: {fruits}")

popped = fruits.pop()
print(f"After pop: {fruits}, popped: {popped}")

del fruits[0]
print(f"After del: {fruits}")

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nNumbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 4: {numbers.index(4)}")

# Sorting
numbers.sort()
print(f"Sorted: {numbers}")

numbers.reverse()
print(f"Reversed: {numbers}")

# Copying lists
original = [1, 2, 3]
shallow_copy = original.copy()
deep_copy = original[:]

print(f"\nOriginal: {original}")
print(f"Shallow copy: {shallow_copy}")
print(f"Deep copy: {deep_copy}")
```

### Activity 1.3: List Slicing and Indexing

Master list slicing and indexing techniques.

**File: `list_slicing.py`**
```python
# List Slicing Examples
print("=== List Slicing ===\n")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")

# Basic indexing
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Second to last: {numbers[-2]}")

# Basic slicing
print(f"First 3 elements: {numbers[:3]}")
print(f"Last 3 elements: {numbers[-3:]}")
print(f"Middle elements: {numbers[2:8]}")

# Step slicing
print(f"Every 2nd element: {numbers[::2]}")
print(f"Every 3rd from index 1: {numbers[1::3]}")
print(f"Reverse list: {numbers[::-1]}")

# Modifying with slicing
numbers[2:5] = [20, 30, 40]
print(f"After modification: {numbers}")

numbers[1:4] = [100]
print(f"After replacement: {numbers}")

# Nested list slicing
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nMatrix: {matrix}")
print(f"First row: {matrix[0]}")
print(f"First column: {[row[0] for row in matrix]}")
print(f"Center element: {matrix[1][1]}")
```

## Section 2: Working with Dictionaries

### Activity 2.1: Dictionary Basics and Creation

Learn different ways to create and initialize dictionaries.

**File: `dictionary_basics.py`**
```python
# Dictionary Basics Examples
print("=== Dictionary Basics ===\n")

# Creating dictionaries
empty_dict = {}
student = {"name": "Alice", "age": 20, "grade": "A"}
mixed_dict = {"string": "hello", "number": 42, "list": [1, 2, 3]}

print("Different types of dictionaries:")
print(f"Empty dict: {empty_dict}")
print(f"Student: {student}")
print(f"Mixed types: {mixed_dict}")

# Dictionary creation methods
keys = ["a", "b", "c"]
values = [1, 2, 3]
from_lists = dict(zip(keys, values))
print(f"From lists: {from_lists}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares_dict}")

# Using dict() constructor
person = dict(name="Bob", age=25, city="New York")
print(f"Using dict(): {person}")

# Nested dictionaries
company = {
    "name": "Tech Corp",
    "employees": {
        "john": {"position": "developer", "salary": 70000},
        "jane": {"position": "designer", "salary": 65000}
    }
}
print(f"Nested dict: {company}")
```

### Activity 2.2: Dictionary Operations and Methods

Explore dictionary manipulation methods and operations.

**File: `dictionary_operations.py`**
```python
# Dictionary Operations Examples
print("=== Dictionary Operations ===\n")

# Initialize a dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}
print(f"Original dict: {student}")

# Adding/updating elements
student["email"] = "alice@example.com"
student["age"] = 21
print(f"After additions: {student}")

# Dictionary methods
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Getting values safely
print(f"Name: {student.get('name')}")
print(f"Phone: {student.get('phone', 'Not provided')}")

# Removing elements
email = student.pop("email")
print(f"After pop: {student}, removed: {email}")

# Update dictionary
student.update({"city": "Boston", "major": "Computer Science"})
print(f"After update: {student}")

# Dictionary iteration
print("\nIterating through dictionary:")
for key in student:
    print(f"{key}: {student[key]}")

print("\nUsing items():")
for key, value in student.items():
    print(f"{key} -> {value}")

# Dictionary copying
original = {"a": 1, "b": 2}
shallow = original.copy()
print(f"Original: {original}, Copy: {shallow}")
```

### Activity 2.3: Advanced Dictionary Techniques

Work with nested dictionaries and complex operations.

**File: `advanced_dictionaries.py`**
```python
# Advanced Dictionary Examples
print("=== Advanced Dictionary Techniques ===\n")

# Nested dictionary operations
inventory = {
    "electronics": {
        "laptop": {"price": 999, "stock": 5},
        "phone": {"price": 699, "stock": 12}
    },
    "clothing": {
        "shirt": {"price": 29, "stock": 25},
        "pants": {"price": 49, "stock": 15}
    }
}

print("Inventory structure:")
for category, items in inventory.items():
    print(f"{category}:")
    for item, details in items.items():
        print(f"  {item}: ${details['price']}, Stock: {details['stock']}")

# Dictionary merging
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"\nMerged dictionaries: {merged}")

# Counting with dictionaries
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"Character count: {char_count}")

# Dictionary filtering
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 96
}

high_scorers = {name: score for name, score in students.items() if score >= 90}
print(f"High scorers: {high_scorers}")

# Sorting dictionaries
sorted_by_score = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
print(f"Sorted by score: {sorted_by_score}")
```

## Section 3: Working with Arrays

### Activity 3.1: Python Arrays vs Lists

Compare arrays and lists, and when to use each.

**File: `arrays_vs_lists.py`**
```python
# Arrays vs Lists Examples
print("=== Arrays vs Lists ===\n")

import array

# Creating arrays
int_array = array.array('i', [1, 2, 3, 4, 5])
float_array = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
char_array = array.array('u', 'hello')

print("Array examples:")
print(f"Integer array: {int_array}")
print(f"Float array: {float_array}")
print(f"Character array: {char_array}")

# Array vs List comparison
import sys
list_example = [1, 2, 3, 4, 5]
array_example = array.array('i', [1, 2, 3, 4, 5])

print(f"\nMemory usage:")
print(f"List size: {sys.getsizeof(list_example)} bytes")
print(f"Array size: {sys.getsizeof(array_example)} bytes")

# Array operations
print(f"\nArray operations:")
int_array.append(6)
print(f"After append: {int_array}")

int_array.insert(0, 0)
print(f"After insert: {int_array}")

removed = int_array.pop()
print(f"After pop: {int_array}, removed: {removed}")

# Array methods
print(f"Array length: {len(int_array)}")
print(f"Sum of array: {sum(int_array)}")
print(f"Index of 3: {int_array.index(3)}")
```

### Activity 3.2: NumPy Arrays (Optional)

Introduction to NumPy arrays for numerical computations.

**File: `numpy_arrays.py`**
```python
# NumPy Arrays Examples (requires: pip install numpy)
print("=== NumPy Arrays ===\n")

try:
    import numpy as np
    
    # Creating NumPy arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    
    print("NumPy array examples:")
    print(f"1D array: {arr1}")
    print(f"2D array:\n{arr2}")
    print(f"Array shape: {arr2.shape}")
    print(f"Array dtype: {arr1.dtype}")
    
    # Array operations
    print(f"\nArray operations:")
    print(f"arr1 * 2: {arr1 * 2}")
    print(f"arr1 + 10: {arr1 + 10}")
    print(f"arr1 ** 2: {arr1 ** 2}")
    
    # Array functions
    print(f"Sum: {np.sum(arr1)}")
    print(f"Mean: {np.mean(arr1)}")
    print(f"Max: {np.max(arr1)}")
    print(f"Min: {np.min(arr1)}")
    
    # Array creation functions
    zeros = np.zeros((3, 3))
    ones = np.ones((2, 4))
    range_arr = np.arange(0, 10, 2)
    
    print(f"\nZeros array:\n{zeros}")
    print(f"Ones array:\n{ones}")
    print(f"Range array: {range_arr}")
    
except ImportError:
    print("NumPy not installed. Install with: pip install numpy")
    print("Using Python lists instead:")
    
    # List-based operations
    numbers = [1, 2, 3, 4, 5]
    doubled = [x * 2 for x in numbers]
    squared = [x ** 2 for x in numbers]
    
    print(f"Original: {numbers}")
    print(f"Doubled: {doubled}")
    print(f"Squared: {squared}")
```

## Section 4: Data Structure Comparison and Use Cases

### Activity 4.1: Performance Comparison

Compare performance characteristics of different data structures.

**File: `performance_comparison.py`**
```python
# Performance Comparison Examples
print("=== Performance Comparison ===\n")

import time

# List vs Dictionary lookup
large_list = list(range(10000))
large_dict = {i: i for i in range(10000)}

# List search
start = time.time()
result = 9999 in large_list
list_time = time.time() - start

# Dictionary search
start = time.time()
result = 9999 in large_dict
dict_time = time.time() - start

print(f"Search performance:")
print(f"List search time: {list_time:.6f} seconds")
print(f"Dict search time: {dict_time:.6f} seconds")
print(f"Dictionary is {list_time/dict_time:.1f}x faster")

# Memory usage comparison
import sys
test_list = [i for i in range(1000)]
test_dict = {i: i for i in range(1000)}

print(f"\nMemory usage:")
print(f"List: {sys.getsizeof(test_list)} bytes")
print(f"Dict: {sys.getsizeof(test_dict)} bytes")
```

### Activity 4.2: Choosing the Right Data Structure

Examples of when to use each data structure.

**File: `data_structure_choice.py`**
```python
# Data Structure Choice Examples
print("=== Choosing the Right Data Structure ===\n")

# Use Lists for:
print("1. Lists - Use when you need:")
print("   - Ordered collection")
print("   - Allow duplicates")
print("   - Index-based access")

shopping_cart = ["apple", "banana", "apple", "orange"]
print(f"Shopping cart: {shopping_cart}")
print(f"First item: {shopping_cart[0]}")

# Use Dictionaries for:
print("\n2. Dictionaries - Use when you need:")
print("   - Key-value pairs")
print("   - Fast lookups")
print("   - No duplicates for keys")

user_profile = {
    "username": "john_doe",
    "email": "john@example.com",
    "age": 30,
    "preferences": ["coding", "reading"]
}
print(f"User profile: {user_profile}")
print(f"Email: {user_profile['email']}")

# Use Sets for:
print("\n3. Sets - Use when you need:")
print("   - Unique elements")
print("   - Fast membership testing")
print("   - Set operations")

unique_visitors = {"alice", "bob", "charlie", "alice"}
print(f"Unique visitors: {unique_visitors}")

# Combined usage example
print("\n4. Combined usage example:")
student_grades = {
    "Alice": [85, 92, 78, 90],
    "Bob": [88, 85, 92, 87],
    "Charlie": [92, 88, 85, 91]
}

for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    print(f"{student}: grades {grades}, average {average:.1f}")
```

## Execution Instructions

Run each script to practice different data structure concepts:

**Steps:**
1. Create each Python file in your project directory
2. Run the scripts one by one:

```bash
python list_basics.py
python list_operations.py
python list_slicing.py
python dictionary_basics.py
python dictionary_operations.py
python advanced_dictionaries.py
python arrays_vs_lists.py
python numpy_arrays.py
python performance_comparison.py
python data_structure_choice.py
```

**Learning Objectives:**
- [ ] Create and manipulate lists effectively
- [ ] Master dictionary operations and methods
- [ ] Understand when to use arrays vs lists
- [ ] Compare performance characteristics
- [ ] Choose appropriate data structures for different use cases
- [ ] Work with nested data structures
- [ ] Apply data structures to solve real-world problems
