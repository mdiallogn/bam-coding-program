# Session 5 - Python Data Structures: Lists, Dictionaries, and Arrays

## What You'll Learn Today
- [ ] How to create and use lists (ordered collections)
- [ ] How to create and use dictionaries (key-value pairs)
- [ ] How to work with arrays (efficient number storage)
- [ ] When to use lists vs dictionaries vs arrays
- [ ] How to combine these data structures for real projects

---

## Part 1: Lists - Your Digital Shopping Cart

Think of a list like a shopping cart - it keeps things in order, and you can have duplicates (like buying 2 apples).

### Activity 1.1: Creating Your First Lists

Learn the basics of making and using lists.

**File: `list_basics.py`**
```python
# List Basics - Let's start simple!
print("=== My First Lists ===\n")

# Create different types of lists
my_grades = [85, 92, 78, 90, 88]
favorite_movies = ["Spider-Man", "Avatar", "The Matrix"]
mixed_stuff = [16, "John", True, 3.14]

print(f"My grades: {my_grades}")
print(f"Favorite movies: {favorite_movies}")
print(f"Mixed list: {mixed_stuff}")

# Access items by position (index starts at 0!)
print(f"\nFirst grade: {my_grades[0]}")
print(f"Last movie: {favorite_movies[-1]}")  # -1 means last item

# How many items do we have?
print(f"Number of grades: {len(my_grades)}")
```

### Activity 1.2: Adding and Removing Items

Learn how to change your lists.

**File: `list_operations.py`**
```python
# List Operations - Making changes!
print("=== Changing Lists ===\n")

# Start with a homework list
homework = ["Math", "Science", "English"]
print(f"Original homework: {homework}")

# Add new subjects
homework.append("History")  # Add to the end
homework.insert(1, "Art")   # Insert at position 1
print(f"After adding subjects: {homework}")

# Remove subjects (when you finish them!)
homework.remove("Math")     # Remove by name
finished = homework.pop()   # Remove last item and save it
print(f"After removing Math: {homework}")
print(f"Just finished: {finished}")

# Check if something is in the list
if "Science" in homework:
    print("Don't forget about Science homework!")

# Go through all items
print("\nRemaining homework:")
for subject in homework:
    print(f"- {subject}")
```

### Activity 1.3: List Tricks and Tips

Cool things you can do with lists.

**File: `list_tricks.py`**
```python
# List Tricks - Cool techniques!
print("=== List Tricks ===\n")

# Working with numbers
test_scores = [85, 92, 78, 90, 88, 76, 95]
print(f"Test scores: {test_scores}")

# Get useful information
print(f"Highest score: {max(test_scores)}")
print(f"Lowest score: {min(test_scores)}")
print(f"Average score: {sum(test_scores) / len(test_scores):.1f}")

# Sort the list
test_scores.sort()  # Changes the original list
print(f"Sorted scores: {test_scores}")

# Make a copy and sort it differently
scores_copy = test_scores.copy()
scores_copy.sort(reverse=True)  # High to low
print(f"High to low: {scores_copy}")

# Slice the list (get parts of it)
top_three = scores_copy[:3]  # First 3 items
bottom_two = scores_copy[-2:]  # Last 2 items
print(f"Top 3 scores: {top_three}")
print(f"Bottom 2 scores: {bottom_two}")
```

---

## Part 2: Dictionaries - Your Digital Address Book

Think of a dictionary like a phone book - you look up a name (key) to find a phone number (value).

### Activity 2.1: Creating Your First Dictionary

Learn to store information with labels.

**File: `dictionary_basics.py`**
```python
# Dictionary Basics - Information with labels!
print("=== My First Dictionary ===\n")

# Create a student profile
my_profile = {
    "name": "Alex Smith",
    "age": 16,
    "grade": "11th",
    "favorite_subject": "Computer Science",
    "gpa": 3.8
}

print(f"My profile: {my_profile}")
print(f"My name: {my_profile['name']}")
print(f"My age: {my_profile['age']}")

# Add new information
my_profile["hobby"] = "Gaming"
my_profile["city"] = "Boston"
print(f"Updated profile: {my_profile}")

# Change existing information
my_profile["age"] = 17  # Happy birthday!
print(f"After birthday: {my_profile}")
```

### Activity 2.2: Dictionary Operations

Learn to work with dictionary information.

**File: `dictionary_operations.py`**
```python
# Dictionary Operations - Managing information!
print("=== Working with Dictionaries ===\n")

# Create a contact book
contacts = {
    "Mom": "555-1234",
    "Dad": "555-5678",
    "Best Friend": "555-9012",
    "Pizza Place": "555-3456"
}

print(f"My contacts: {contacts}")

# Look up a contact safely
contact_name = "Mom"
if contact_name in contacts:
    print(f"{contact_name}'s number: {contacts[contact_name]}")

# Add new contact
contacts["School"] = "555-7890"
print(f"After adding school: {contacts}")

# Get all names and numbers
print("\nAll my contacts:")
for name, number in contacts.items():
    print(f"{name}: {number}")

# Get just the names or just the numbers
print(f"\nContact names: {list(contacts.keys())}")
print(f"Phone numbers: {list(contacts.values())}")
```

### Activity 2.3: Advanced Dictionary Uses

Solve real problems with dictionaries.

**File: `dictionary_advanced.py`**
```python
# Advanced Dictionary Uses - Real world examples!
print("=== Advanced Dictionary Magic ===\n")

# Grade tracker for multiple subjects
grade_book = {
    "Math": [85, 90, 88, 92],
    "Science": [78, 85, 82, 88],
    "English": [92, 88, 90, 95],
    "History": [85, 87, 90, 92]
}

print("Grade Book:")
for subject, grades in grade_book.items():
    average = sum(grades) / len(grades)
    print(f"{subject}: {grades} → Average: {average:.1f}")

# Count things with a dictionary
favorite_colors = ["blue", "red", "blue", "green", "red", "blue", "yellow"]
color_count = {}

for color in favorite_colors:
    if color in color_count:
        color_count[color] += 1
    else:
        color_count[color] = 1

print(f"\nColor popularity: {color_count}")

# Find the most popular color
most_popular = max(color_count, key=color_count.get)
print(f"Most popular color: {most_popular}")
```

---

## Part 3: Arrays - Your Math Toolkit

Arrays are like lists but designed specifically for numbers and math operations. They're more efficient when working with lots of numbers!

### Activity 3.1: Introduction to Arrays

Learn the difference between arrays and lists.

**File: `array_basics.py`**
```python
# Array Basics - Numbers made easy!
print("=== Introduction to Arrays ===\n")

import array

# Create different types of arrays
grades_array = array.array('i', [85, 92, 78, 90, 88])  # 'i' means integers
prices_array = array.array('f', [12.99, 8.50, 15.75, 22.00])  # 'f' means floats

print(f"Grades array: {grades_array}")
print(f"Prices array: {prices_array}")

# Compare with regular lists
grades_list = [85, 92, 78, 90, 88]
print(f"Grades list: {grades_list}")

# Arrays are more memory efficient for numbers
import sys
print(f"\nMemory comparison:")
print(f"List size: {sys.getsizeof(grades_list)} bytes")
print(f"Array size: {sys.getsizeof(grades_array)} bytes")

# Array operations (similar to lists)
grades_array.append(95)
print(f"After adding grade: {grades_array}")

# Convert between arrays and lists
array_to_list = list(grades_array)
list_to_array = array.array('i', grades_list)
print(f"Array to list: {array_to_list}")
print(f"List to array: {list_to_array}")
```

### Activity 3.2: Array Operations for Math

Use arrays for mathematical calculations.

**File: `array_math.py`**
```python
# Array Math - Perfect for calculations!
print("=== Array Mathematics ===\n")

import array

# Test scores for math calculations
test_scores = array.array('i', [78, 85, 92, 88, 76, 91, 83, 89, 94, 87])
print(f"Test scores: {test_scores}")

# Basic math operations
print(f"Number of tests: {len(test_scores)}")
print(f"Highest score: {max(test_scores)}")
print(f"Lowest score: {min(test_scores)}")
print(f"Total points: {sum(test_scores)}")
print(f"Average score: {sum(test_scores) / len(test_scores):.1f}")

# Find specific scores
passing_score = 80
passing_count = 0
for score in test_scores:
    if score >= passing_score:
        passing_count += 1

print(f"Passing scores (≥{passing_score}): {passing_count}")
print(f"Passing percentage: {(passing_count / len(test_scores)) * 100:.1f}%")

# Temperature data (using floats)
temperatures = array.array('f', [23.5, 25.2, 22.8, 26.1, 24.7, 23.9, 25.5])
print(f"\nWeekly temperatures: {temperatures}")

# Convert Celsius to Fahrenheit
fahrenheit = array.array('f')
for temp in temperatures:
    fahrenheit.append(temp * 9/5 + 32)

print(f"In Fahrenheit: {fahrenheit}")
```

### Activity 3.3: NumPy Arrays (Advanced)

Introduction to NumPy for serious math work.

**File: `numpy_intro.py`**
```python
# NumPy Arrays - Professional math tools!
print("=== NumPy Arrays (Advanced) ===\n")

try:
    import numpy as np
    
    # Create NumPy arrays
    scores = np.array([85, 92, 78, 90, 88, 76, 95])
    print(f"NumPy array: {scores}")
    
    # Amazing NumPy features
    print(f"Mean: {np.mean(scores):.1f}")
    print(f"Standard deviation: {np.std(scores):.1f}")
    print(f"Median: {np.median(scores):.1f}")
    
    # Array operations (vectorized - very fast!)
    curved_scores = scores + 5  # Add 5 to all scores
    print(f"Curved scores: {curved_scores}")
    
    # Create special arrays
    zeros = np.zeros(5)
    ones = np.ones(5)
    range_array = np.arange(0, 20, 2)
    
    print(f"Zeros: {zeros}")
    print(f"Ones: {ones}")
    print(f"Even numbers: {range_array}")
    
    # 2D arrays (like spreadsheets)
    grade_matrix = np.array([
        [85, 90, 88],  # Student 1
        [92, 87, 91],  # Student 2
        [78, 85, 82]   # Student 3
    ])
    
    print(f"\nGrade matrix:")
    print(grade_matrix)
    print(f"Average per student: {np.mean(grade_matrix, axis=1)}")
    print(f"Average per test: {np.mean(grade_matrix, axis=0)}")
    
except ImportError:
    print("NumPy not installed! Install with: pip install numpy")
    print("For now, we'll use regular Python arrays and lists:")
    
    # Alternative using regular Python
    import array
    scores = array.array('i', [85, 92, 78, 90, 88, 76, 95])
    print(f"Regular array: {scores}")
    
    # Manual calculations
    average = sum(scores) / len(scores)
    print(f"Average: {average:.1f}")
    
    # Add 5 to all scores (curve)
    curved = array.array('i')
    for score in scores:
        curved.append(score + 5)
    print(f"Curved scores: {curved}")
```

---

## Part 4: Combining Lists, Dictionaries, and Arrays

Now let's use all three together to solve complex problems!

### Activity 4.1: Sports Statistics System

Create a system to track sports team statistics.

**File: `sports_stats.py`**
```python
# Sports Statistics - All data structures together!
print("=== Sports Team Statistics ===\n")

import array

# Team data combining all structures
team_data = {
    "team_name": "Eagles",
    "players": [
        {"name": "Alex", "position": "Forward", "games": 12},
        {"name": "Sam", "position": "Guard", "games": 11},
        {"name": "Jordan", "position": "Center", "games": 12},
        {"name": "Casey", "position": "Guard", "games": 10}
    ],
    "game_scores": array.array('i', [78, 85, 92, 67, 81, 89, 77, 83, 91, 86, 79, 88])
}

print(f"Team: {team_data['team_name']}")
print(f"Games played: {len(team_data['game_scores'])}")

# Player statistics
print("\nPlayer Roster:")
for i, player in enumerate(team_data['players'], 1):
    print(f"{i}. {player['name']} - {player['position']} ({player['games']} games)")

# Game statistics using arrays
scores = team_data['game_scores']
print(f"\nGame Scores: {list(scores)}")
print(f"Average score: {sum(scores) / len(scores):.1f}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")

# Win/loss record (scores above 80 are wins)
wins = 0
losses = 0
for score in scores:
    if score >= 80:
        wins += 1
    else:
        losses += 1

print(f"Record: {wins} wins, {losses} losses")
print(f"Win percentage: {(wins / len(scores)) * 100:.1f}%")

# Position count using dictionary
position_count = {}
for player in team_data['players']:
    position = player['position']
    position_count[position] = position_count.get(position, 0) + 1

print(f"\nPositions: {position_count}")
```

### Activity 4.2: Weather Data Analysis

Analyze weather data using all three data structures.

**File: `weather_analysis.py`**
```python
# Weather Analysis - Real-world data science!
print("=== Weather Data Analysis ===\n")

import array

# Weather data for a week
weather_data = {
    "city": "Boston",
    "week": "March 15-21",
    "daily_temps": array.array('f', [18.5, 22.3, 20.1, 25.6, 23.8, 19.2, 21.7]),
    "conditions": ["Sunny", "Cloudy", "Rainy", "Sunny", "Partly Cloudy", "Rainy", "Sunny"],
    "humidity": [45, 60, 85, 40, 55, 80, 50]
}

print(f"Weather Report for {weather_data['city']}")
print(f"Week: {weather_data['week']}")

# Daily report combining all data
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temps = weather_data['daily_temps']
conditions = weather_data['conditions']
humidity = weather_data['humidity']

print("\nDaily Weather:")
for i in range(len(days)):
    print(f"{days[i]}: {temps[i]:.1f}°C, {conditions[i]}, {humidity[i]}% humidity")

# Temperature analysis using arrays
print(f"\nTemperature Analysis:")
print(f"Average temperature: {sum(temps) / len(temps):.1f}°C")
print(f"Highest temperature: {max(temps):.1f}°C")
print(f"Lowest temperature: {min(temps):.1f}°C")

# Condition analysis using dictionaries
condition_count = {}
for condition in conditions:
    condition_count[condition] = condition_count.get(condition, 0) + 1

print(f"\nWeather Conditions:")
for condition, count in condition_count.items():
    print(f"{condition}: {count} days")

# Find best day (highest temp + sunny)
best_day = None
best_temp = -100
for i, condition in enumerate(conditions):
    if condition == "Sunny" and temps[i] > best_temp:
        best_temp = temps[i]
        best_day = days[i]

if best_day:
    print(f"\nBest day: {best_day} ({best_temp:.1f}°C and Sunny)")
```

---

## Practice Exercises

Try these on your own!

### Exercise 1: Grade Book System
Create a complete grade book using lists for students, dictionaries for student info, and arrays for grades.

### Exercise 2: Shopping Cart Calculator
Build a shopping system with lists of items, dictionaries for product info, and arrays for prices.

### Exercise 3: Music Playlist Analyzer
Create a music analysis system using all three data structures.

---

## How to Run Your Code

1. **Save each code example** in a separate `.py` file
2. **Open your terminal/command prompt**
3. **Navigate to your project folder**
4. **Run each file** using Python:

```bash
python list_basics.py
python list_operations.py
python list_tricks.py
python dictionary_basics.py
python dictionary_operations.py
python dictionary_advanced.py
python array_basics.py
python array_math.py
python numpy_intro.py
python student_system.py
python class_schedule.py
python sports_stats.py
python weather_analysis.py
```

---

## Quick Reference

### Lists Cheat Sheet
```python
# Creating lists
my_list = [1, 2, 3]

# Adding items
my_list.append(4)        # Add to end
my_list.insert(0, 0)     # Insert at position

# Removing items
my_list.remove(2)        # Remove by value
last_item = my_list.pop()  # Remove and return last

# Useful operations
len(my_list)            # Get length
my_list.sort()          # Sort the list
my_list[0]              # Get first item
my_list[-1]             # Get last item
```

### Dictionaries Cheat Sheet
```python
# Creating dictionaries
my_dict = {"name": "Alex", "age": 16}

# Adding/changing items
my_dict["grade"] = "A"   # Add new key-value pair
my_dict["age"] = 17      # Change existing value

# Getting information
my_dict["name"]          # Get value by key
my_dict.get("phone", "Not found")  # Safe get with default

# Useful operations
my_dict.keys()           # Get all keys
my_dict.values()         # Get all values
my_dict.items()          # Get key-value pairs
```

### Arrays Cheat Sheet
```python
import array

# Creating arrays
int_array = array.array('i', [1, 2, 3])     # integers
float_array = array.array('f', [1.1, 2.2])  # floats

# Array operations
int_array.append(4)      # Add item
len(int_array)           # Get length
sum(int_array)           # Sum all numbers
max(int_array)           # Find maximum
min(int_array)           # Find minimum

# Convert to/from lists
list_version = list(int_array)
array_version = array.array('i', [1, 2, 3])
```

---

## When to Use Each Data Structure

**Use Lists when:**
- You need to store items in order
- You want to allow duplicates
- You need to access items by position
- Example: Shopping cart, to-do list, student roster

**Use Dictionaries when:**
- You need to look up values by keys
- You want to store related information together
- You need fast lookups
- Example: Phone book, student profiles, settings

**Use Arrays when:**
- You're working with lots of numbers
- You need efficient storage
- You're doing math calculations
- Example: Test scores, temperatures, measurements

---

## What's Next?

Great job learning about lists, dictionaries, and arrays! These are the foundation of data organization in programming. In the next session, we'll learn about functions and how to organize our code into reusable pieces.

**Remember:** The best way to learn is by doing! Try creating your own projects using these data structures.