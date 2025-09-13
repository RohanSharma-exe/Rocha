from functions.run_python_file import run_python_file

# Test case 1: Run calculator's main.py without arguments
print("--- Running calculator/main.py (no args) ---")
print(run_python_file("calculator", "main.py"))
print("-------------------------------------------\n")

# Test case 2: Run calculator's main.py with an argument
print("--- Running calculator/main.py with '3 + 5' ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print("-------------------------------------------\n")

# Test case 3: Run the calculator's test file
print("--- Running calculator/tests.py ---")
print(run_python_file("calculator", "tests.py"))
print("-------------------------------------------\n")

# Test case 4: Attempt to run a file outside the working directory (should fail)
print("--- Attempting directory traversal ---")
print(run_python_file("calculator", "../main.py"))
print("-------------------------------------------\n")

# Test case 5: Attempt to run a file that doesn't exist (should fail)
print("--- Attempting to run nonexistent.py ---")
print(run_python_file("calculator", "nonexistent.py"))
print("-------------------------------------------\n")