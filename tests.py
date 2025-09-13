# tests.py
from functions.get_file_content import get_file_content

def main():
    print("--- Testing Truncation ---")
    # This will test the truncation functionality
    print(get_file_content("calculator", "lorem.txt"))
    print("\n--- Testing Standard File Read ---")
    # This should return the full content of main.py
    print(get_file_content("calculator", "main.py"))
    print("\n--- Testing Nested File Read ---")
    # This should return the full content of the nested calculator.py
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\n--- Testing Directory Traversal Error ---")
    # This should return an error for being outside the working directory
    print(get_file_content("calculator", "../../../../../../../../../bin/cat")) # Adjusted path for a common example
    print("\n--- Testing File Not Found Error ---")
    # This should return an error because the file does not exist
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()