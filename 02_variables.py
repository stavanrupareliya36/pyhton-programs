"""
Program: Variables in Python
File: 02_variables.py
Topic: Python Basics

Description:
    Learn how to create variables, assign values,
    update values, and print variables in Python.
"""

# --------------------------------------------------
# 1. Creating Variables
# --------------------------------------------------

name = "Akshar"
age = 30
height = 5.8
is_engineer = True

print(name)
print(age)
print(height)
print(is_engineer)


# --------------------------------------------------
# 2. Print Variables with Messages
# --------------------------------------------------

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Engineer:", is_engineer)


# --------------------------------------------------
# 3. Different Types of Variables
# --------------------------------------------------

company = "ABC Technologies"   # String
experience = 6                 # Integer
salary = 50000.50              # Float
is_working = True              # Boolean

print("\nEmployee Information")

print("Company:", company)
print("Experience:", experience)
print("Salary:", salary)
print("Currently Working:", is_working)


# --------------------------------------------------
# 4. Changing Variable Values
# --------------------------------------------------

score = 50

print("\nOriginal Score:", score)

score = 75

print("Updated Score:", score)


# --------------------------------------------------
# 5. Multiple Variable Assignment
# --------------------------------------------------

x, y, z = 10, 20, 30

print("\nx =", x)
print("y =", y)
print("z =", z)


# --------------------------------------------------
# 6. Assign Same Value to Multiple Variables
# --------------------------------------------------

a = b = c = 100

print("\na =", a)
print("b =", b)
print("c =", c)


# --------------------------------------------------
# 7. Simple Calculation Using Variables
# --------------------------------------------------

num1 = 10
num2 = 20

total = num1 + num2

print("\nNumber 1:", num1)
print("Number 2:", num2)
print("Total:", total)


# --------------------------------------------------
# 8. Variable Naming Examples
# --------------------------------------------------

student_name = "Rahul"
student_age = 25
total_marks = 450

print("\nStudent Name:", student_name)
print("Student Age:", student_age)
print("Total Marks:", total_marks)


# --------------------------------------------------
# 9. Check Variable Type
# --------------------------------------------------

print("\nVariable Types")

print(type(name))
print(type(age))
print(type(height))
print(type(is_engineer))


# --------------------------------------------------
# 10. Final Example
# --------------------------------------------------

employee_name = "Stavan"
employee_role = "AI Engineer"
employee_experience = 6

print("\n--- Employee Details ---")
print("Name:", employee_name)
print("Role:", employee_role)
print("Experience:", employee_experience, "Years")
