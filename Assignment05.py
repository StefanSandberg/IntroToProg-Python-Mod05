# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Stefan Sandberg,5/21/2025, Added JSON file functionality by using JSON file structure.
#                              Added structured error handling associated with options 1-4
#                              from the MENU
# ------------------------------------------------------------------------------------------ #

import json

# Define the Constants
MENU = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME = "Enrollments.json"

# Initialize Variables
students = []                # List to store all student data
choice = ""                 # Store user's menu selection
student = {}                # Store individual student data
first_name = ""            # Store student's first name
last_name = ""             # Store student's last name
course_name = ""           # Store course name
file_obj = None            # File object for file operations
create_file = ""           # Store user's response for file creation
error_message = ""         # Store error messages

# Load existing data with structured error handling
try:
    with open(FILE_NAME, 'r') as file:
        students = json.load(file)
except FileNotFoundError:
    print(f"\nError: The file {FILE_NAME} was not found.")
    create_file = input(f"Would you like to create {FILE_NAME}? (yes/no): ") \
        .lower().strip()
    if create_file == 'yes':
        try:
            with open(FILE_NAME, 'w') as file:
                json.dump([], file, indent=4)
            print(f"Successfully created {FILE_NAME}")
            students = []
        except Exception as e:
            error_message = str(e)
            print(f"Error creating file: {error_message}")
            print("Program will continue with empty student list.")
            students = []
    else:
        print("Program will continue with empty student list.")
        students = []
except json.JSONDecodeError:
    print(f"\nError: {FILE_NAME} exists but contains invalid data.")
    print("Program will continue with empty student list.")
    students = []
except Exception as e:
    error_message = str(e)
    print(f"\nUnexpected error: {error_message}")
    print("Program will continue with empty student list.")
    students = []

# Main program loop
while True:
    # Show menu
    print(MENU)
    choice = input("What would you like to do (1-4): ").strip()
    
    # Register new student
    if choice == "1":
        # Get student's first name
        first_name = input("Enter the student's first name: ").strip()
        while not first_name.isalpha():
            print("First name must contain only letters!")
            first_name = input("Enter the student's first name: ").strip()
        
        # Get student's last name
        last_name = input("Enter the student's last name: ").strip()
        while not last_name.isalpha():
            print("Last name must contain only letters!")
            last_name = input("Enter the student's last name: ").strip()
        
        # Get course name
        course_name = input("Enter the course name: ").strip()
        while not course_name:
            print("Course name cannot be empty!")
            course_name = input("Enter the course name: ").strip()
        
        # Create student record
        student = {
            "first_name": first_name,
            "last_name": last_name,
            "course_name": course_name
        }
        
        # Add to students list
        students.append(student)
        print(f"Registered {student['first_name']} {student['last_name']} \
        for {student['course_name']}")
        
        # Save to file
        try:
            with open(FILE_NAME, 'w') as file:
                json.dump(students, file, indent=4)
            print("Data saved successfully!")
        except Exception as e:
            error_message = str(e)
            print(f"Error saving data: {error_message}")
    
    # Show all students
    elif choice == "2":
        if not students:
            print("No students registered yet!")
        else:
            print("\nCurrent Registrations:")
            for student in students:
                print(f"Student {student['first_name']} {student['last_name']} is enrolled in \
                {student['course_name']}")
    
    # Save data
    elif choice == "3":
        try:
            with open(FILE_NAME, 'w') as file:
                json.dump(students, file, indent=4)
            print("Data saved successfully!")
        except Exception as e:
            error_message = str(e)
            print(f"Error saving data: {error_message}")
    
    # Exit program
    elif choice == "4":
        try:
            with open(FILE_NAME, 'w') as file:
                json.dump(students, file, indent=4)
            print("Data saved successfully!")
        except Exception as e:
            error_message = str(e)
            print(f"Error saving data: {error_message}")
        print("Thank you for using the program!")
        break
    
    # Invalid choice
    else:
        print("Please enter a whole number between 1 and 4!") 
