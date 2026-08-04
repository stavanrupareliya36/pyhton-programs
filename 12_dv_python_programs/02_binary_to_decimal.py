"""
Program: Binary to Decimal Conversion
File: 02_binary_to_decimal.py
Topic: Bit Manipulation / Design Verification

Example:
    Binary  : 1010
    Decimal : 10
"""


# --------------------------------------------------
# Method 1: Using Python int()
# --------------------------------------------------

binary_number = "1010"

decimal_number = int(binary_number, 2)

print("Binary  :", binary_number)
print("Decimal :", decimal_number)


# --------------------------------------------------
# Method 2: Manual Conversion
# Important for Interviews
# --------------------------------------------------

binary = "1010"

decimal = 0
power = 0

# Start from rightmost bit
for bit in reversed(binary):

    decimal = decimal + int(bit) * (2 ** power)
    print("decimal:", decimal)

    power = power + 1
    print("power:", power)

print("\nManual Conversion")
print("Binary  :", binary)
print("Decimal :", decimal)


# --------------------------------------------------
# Method 3: User Input
# --------------------------------------------------

binary = input("\nEnter Binary Number: ")

decimal = int(binary, 2)

print("Binary  :", binary)
print("Decimal :", decimal)
