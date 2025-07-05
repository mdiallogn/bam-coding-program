# Session 2 - Python Environment and Basic Programming

## Activities

### Activity 1: Writing a Simple Script

Create a basic Python script to verify the Python environment is working correctly.

**File: `hello_python.py`**
```python
# Simple script to verify Python environment
print("Hello, Python!")
print("Python is working!")
```

### Activity 2: Building a Simple Calculator

Develop a Python program for basic arithmetic operations.

**File: `calculator.py`**
```python
# Simple Calculator Program
print("=== Simple Calculator ===")

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    print("Invalid operation!")
    exit()

# Display result
print(f"Result: {result}")
```

### Activity 3: Executing the Script

Run both scripts to confirm Python is installed and working correctly.

**Steps:**
1. Open terminal/command prompt
2. Navigate to your project directory
3. Run the scripts:
   ```bash
   python hello_python.py
   python calculator.py
   ```

**Learning Goals:**
- [ ] Python executes without errors
- [ ] Calculator performs basic operations
- [ ] Understand input and output
   python hello_python.py
   ```
   **Expected output:**
   ```
   Hello, Python!
   Python environment is working correctly!
   Python version: 3.x.x
   ```

4. Run the calculator program:
   ```bash
   python calculator.py
   ```
   **Example interaction:**
   ```
   === Simple Calculator ===
   Enter first number: 10
   Enter second number: 5
   Enter operation (+, -, *, /): +
   Result: 10.0 + 5.0 = 15.0
   ```

**Verification Checklist:**
- [ ] Python executes without errors
- [ ] Version information displays correctly
- [ ] Calculator accepts input and performs operations
- [ ] Error handling works for invalid operations and division by zero
