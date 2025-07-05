# Session 6 - Working with JSON Files in Python

## Section 1: JSON Basics

### Activity 1.1: What is JSON?

Learn about JSON and how to use it.

**File: `json_basics.py`**
```python
# JSON Basics
print("=== JSON Basics ===\n")

import json

# Create a simple dictionary
student = {
    "name": "Alice",
    "age": 16,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

print(f"Student data: {student}")

# Save to JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=2)

print("Data saved to student.json")

# Read from JSON file
with open("student.json", "r") as file:
    loaded_student = json.load(file)

print(f"Loaded data: {loaded_student}")
print(f"Student name: {loaded_student['name']}")
```

### Activity 1.2: Multiple Records

Work with multiple records in JSON.

**File: `multiple_records.py`**
```python
# Multiple Records
print("=== Multiple Records ===\n")

import json

# Create multiple student records
students = [
    {"name": "Alice", "age": 16, "grade": "A"},
    {"name": "Bob", "age": 17, "grade": "B"},
    {"name": "Charlie", "age": 16, "grade": "A"}
]

# Save all students
with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

print("All students saved to students.json")

# Read all students
with open("students.json", "r") as file:
    loaded_students = json.load(file)

print("All students:")
for student in loaded_students:
    print(f"- {student['name']}: Grade {student['grade']}")
```

## Section 2: Practical JSON Applications

### Activity 2.1: Simple Contact Book

Create a contact book using JSON.

**File: `contact_book.py`**
```python
# Contact Book
print("=== Contact Book ===\n")

import json

# Create contact book
contacts = {
    "Alice": {"phone": "555-1234", "email": "alice@email.com"},
    "Bob": {"phone": "555-5678", "email": "bob@email.com"},
    "Charlie": {"phone": "555-9012", "email": "charlie@email.com"}
}

# Save contacts
with open("contacts.json", "w") as file:
    json.dump(contacts, file, indent=2)

print("Contacts saved!")

# Read and display contacts
with open("contacts.json", "r") as file:
    loaded_contacts = json.load(file)

print("\nContact Book:")
for name, info in loaded_contacts.items():
    print(f"{name}: {info['phone']}, {info['email']}")

# Add new contact
loaded_contacts["Diana"] = {"phone": "555-3456", "email": "diana@email.com"}

# Save updated contacts
with open("contacts.json", "w") as file:
    json.dump(loaded_contacts, file, indent=2)

print("\nContact added and saved!")
```

### Activity 2.2: Simple Game Settings

Create a simple game settings system.

**File: `game_settings.py`**
```python
# Game Settings
print("=== Game Settings ===\n")

import json

# Default game settings
settings = {
    "player_name": "Player1",
    "difficulty": "Easy",
    "sound": True,
    "music": True,
    "high_score": 0
}

# Save settings
with open("game_settings.json", "w") as file:
    json.dump(settings, file, indent=2)

print("Settings saved!")

# Load settings
with open("game_settings.json", "r") as file:
    loaded_settings = json.load(file)

print(f"Player: {loaded_settings['player_name']}")
print(f"Difficulty: {loaded_settings['difficulty']}")
print(f"Sound: {loaded_settings['sound']}")
print(f"High Score: {loaded_settings['high_score']}")

# Update high score
loaded_settings["high_score"] = 1500
loaded_settings["difficulty"] = "Hard"

# Save updated settings
with open("game_settings.json", "w") as file:
    json.dump(loaded_settings, file, indent=2)

print("\nSettings updated and saved!")
```

## Section 3: Error Handling

### Activity 3.1: Safe File Operations

Learn to handle errors when working with files.

**File: `safe_json.py`**
```python
# Safe JSON Operations
print("=== Safe JSON Operations ===\n")

import json

def save_data(filename, data):
    """Save data to JSON file safely"""
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)
        print(f"Data saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def load_data(filename):
    """Load data from JSON file safely"""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        print(f"Data loaded from {filename}")
        return data
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Test safe operations
test_data = {"name": "Test", "value": 42}

# Save data
save_data("test.json", test_data)

# Load data
loaded_data = load_data("test.json")
if loaded_data:
    print(f"Loaded: {loaded_data}")

# Try to load non-existent file
missing_data = load_data("missing.json")
```

## Execution Instructions

Run each script to practice JSON file handling:

```bash
python json_basics.py
python multiple_records.py
python contact_book.py
python game_settings.py
python safe_json.py
```

**Learning Goals:**
- [ ] Understand what JSON is
- [ ] Save and load data to/from JSON files
- [ ] Create practical applications with JSON
- [ ] Handle errors safely
# Update user
```python
update_success = update_user(users_db, id1, {"age": 29, "department": "Senior Engineering"})
if update_success:
    print("User updated successfully")

# Display current state
print(f"\nTotal users: {users_db['metadata']['total_users']}")
for user in users_db['users']:
    print(f"  {user['name']} - {user['department']}")

# Save to file
with open("users_database.json", "w") as file:
    json.dump(users_db, file, indent=2)

print("\nDatabase saved to 'users_database.json'")
```

## Section 2: Advanced JSON Techniques

### Activity 2.1: Nested JSON Structures

Work with complex nested JSON data structures.

**File: `nested_json.py`**
```python
# Nested JSON Examples
print("=== Nested JSON Structures ===\n")

import json

# Complex nested structure
company_data = {
    "company": {
        "name": "Tech Solutions Inc.",
        "founded": 2015,
        "headquarters": {
            "address": {
                "street": "456 Tech Ave",
                "city": "San Francisco",
                "state": "CA",
                "zip": "94105"
            },
            "coordinates": {
                "latitude": 37.7749,
                "longitude": -122.4194
            }
        },
        "departments": [
            {
                "name": "Engineering",
                "head": "John Doe",
                "employees": [
                    {
                        "id": 1,
                        "name": "Alice Johnson",
                        "position": "Senior Developer",
                        "skills": ["Python", "JavaScript", "React"],
                        "projects": [
                            {"name": "Project A", "status": "completed"},
                            {"name": "Project B", "status": "in-progress"}
                        ]
                    },
                    {
                        "id": 2,
                        "name": "Bob Wilson",
                        "position": "DevOps Engineer",
                        "skills": ["Docker", "Kubernetes", "AWS"],
                        "projects": [
                            {"name": "Infrastructure", "status": "ongoing"}
                        ]
                    }
                ]
            },
            {
                "name": "Marketing",
                "head": "Jane Smith",
                "employees": [
                    {
                        "id": 3,
                        "name": "Charlie Brown",
                        "position": "Marketing Manager",
                        "skills": ["Digital Marketing", "Analytics"],
                        "projects": [
                            {"name": "Campaign 2024", "status": "planning"}
                        ]
                    }
                ]
            }
        ]
    }
}

def save_nested_json(data, filename):
    """Save nested JSON with proper formatting"""
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)
    print(f"Saved nested JSON to '{filename}'")

def navigate_nested_json(data, path):
    """Navigate through nested JSON using dot notation"""
    keys = path.split('.')
    current = data
    
    try:
        for key in keys:
            if key.isdigit():
                current = current[int(key)]
            else:
                current = current[key]
        return current
    except (KeyError, IndexError, TypeError):
        return None

def find_employees_by_skill(data, skill):
    """Find all employees with a specific skill"""
    employees = []
    for dept in data["company"]["departments"]:
        for emp in dept["employees"]:
            if skill in emp["skills"]:
                employees.append({
                    "name": emp["name"],
                    "department": dept["name"],
                    "position": emp["position"]
                })
    return employees

def get_project_status_summary(data):
    """Get summary of all project statuses"""
    status_count = {}
    for dept in data["company"]["departments"]:
        for emp in dept["employees"]:
            for project in emp["projects"]:
                status = project["status"]
                status_count[status] = status_count.get(status, 0) + 1
    return status_count

# Test nested JSON operations
print("Working with nested JSON structures:")

# Save the complex structure
save_nested_json(company_data, "company_data.json")

# Navigate nested structure
company_name = navigate_nested_json(company_data, "company.name")
print(f"Company name: {company_name}")

city = navigate_nested_json(company_data, "company.headquarters.address.city")
print(f"City: {city}")

first_employee = navigate_nested_json(company_data, "company.departments.0.employees.0.name")
print(f"First employee: {first_employee}")

# Find employees by skill
python_developers = find_employees_by_skill(company_data, "Python")
print(f"\nPython developers:")
for dev in python_developers:
    print(f"  {dev['name']} - {dev['position']} ({dev['department']})")

# Project status summary
status_summary = get_project_status_summary(company_data)
print(f"\nProject status summary: {status_summary}")
```

### Activity 2.2: JSON Schema Validation

Implement JSON schema validation and data integrity.

**File: `json_validation.py`**
```python
# JSON Validation Examples
print("=== JSON Validation ===\n")

import json
from datetime import datetime

# Define schema for user data
user_schema = {
    "required_fields": ["name", "email", "age"],
    "optional_fields": ["phone", "address", "skills"],
    "field_types": {
        "name": str,
        "email": str,
        "age": int,
        "phone": str,
        "address": dict,
        "skills": list
    },
    "field_constraints": {
        "age": {"min": 0, "max": 150},
        "email": {"pattern": "@"}
    }
}

def validate_user_data(data, schema):
    """Validate user data against schema"""
    errors = []
    
    # Check required fields
    for field in schema["required_fields"]:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    
    # Check field types
    for field, value in data.items():
        if field in schema["field_types"]:
            expected_type = schema["field_types"][field]
            if not isinstance(value, expected_type):
                errors.append(f"Field '{field}' must be {expected_type.__name__}")
    
    # Check constraints
    for field, constraints in schema["field_constraints"].items():
        if field in data:
            value = data[field]
            
            if "min" in constraints and value < constraints["min"]:
                errors.append(f"Field '{field}' must be >= {constraints['min']}")
            
            if "max" in constraints and value > constraints["max"]:
                errors.append(f"Field '{field}' must be <= {constraints['max']}")
            
            if "pattern" in constraints and constraints["pattern"] not in str(value):
                errors.append(f"Field '{field}' must contain '{constraints['pattern']}'")
    
    return len(errors) == 0, errors

def sanitize_user_data(data):
    """Sanitize user data"""
    sanitized = {}
    
    for key, value in data.items():
        if isinstance(value, str):
            sanitized[key] = value.strip()
        else:
            sanitized[key] = value
    
    return sanitized

def create_user_record(data, schema):
    """Create a valid user record"""
    # Sanitize data
    sanitized_data = sanitize_user_data(data)
    
    # Validate
    is_valid, errors = validate_user_data(sanitized_data, schema)
    
    if not is_valid:
        return None, errors
    
    # Add metadata
    sanitized_data["id"] = hash(sanitized_data["email"]) % 10000
    sanitized_data["created_at"] = datetime.now().isoformat()
    sanitized_data["status"] = "active"
    
    return sanitized_data, []

# Test validation
print("Testing JSON validation:")

# Valid user data
valid_user = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "age": 28,
    "skills": ["Python", "JavaScript"]
}

# Invalid user data
invalid_user = {
    "name": "Bob Smith",
    "age": "thirty",  # Should be int
    "phone": "123-456-7890"
    # Missing email
}

# Test valid data
print("\nTesting valid user data:")
user_record, errors = create_user_record(valid_user, user_schema)
if user_record:
    print("Valid user created:")
    print(json.dumps(user_record, indent=2))
else:
    print(f"Validation errors: {errors}")

# Test invalid data
print("\nTesting invalid user data:")
user_record, errors = create_user_record(invalid_user, user_schema)
if user_record:
    print("User created successfully")
else:
    print(f"Validation errors: {errors}")

# Save validation schema
with open("user_schema.json", "w") as file:
    json.dump(user_schema, file, indent=2)

print("\nUser schema saved to 'user_schema.json'")
```

## Execution Instructions

Run each script to practice JSON file handling concepts:

**Steps:**
1. Create each Python file in your project directory
2. Run the scripts in order:

```bash
python json_basics.py
python json_error_handling.py
python json_manipulation.py
python nested_json.py
python json_validation.py
```

**Learning Objectives:**
- [ ] Master JSON file reading and writing operations
- [ ] Implement proper error handling for JSON operations
- [ ] Manipulate complex nested JSON structures
- [ ] Validate JSON data against schemas
- [ ] Use JSON for application configuration management
- [ ] Create environment-specific configurations
- [ ] Build robust JSON-based data persistence systems
