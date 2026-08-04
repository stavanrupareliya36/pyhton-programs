"""
Program: Decimal to Binary Conversion
File: 01_decimal_to_binary.py
Topic: Bit Manipulation / Design Verification

Description:
    Convert a decimal number into binary.

    Method 1: Using Python built-in bin()
    Method 2: Manual conversion without bin()

Example:
    Decimal : 10
    Binary  : 1010
"""


# --------------------------------------------------
# Method 1: Using Python built-in bin()
# --------------------------------------------------

decimal_number = 10

binary_number = bin(decimal_number)

print("Decimal Number :", decimal_number)
print("Binary Number  :", binary_number)

# bin() returns 0b prefix
# Example: 10 -> 0b1010


# --------------------------------------------------
# Remove 0b Prefix
# --------------------------------------------------

binary_without_prefix = bin(decimal_number)[2:]

print("Binary without 0b :", binary_without_prefix)


# --------------------------------------------------
# Method 2: Manual Decimal to Binary Conversion
# Important for Interviews
# --------------------------------------------------

number = 10
temp = number
binary = ""

while temp > 0:

    remainder = temp % 2
    print("remainder:" ,remainder)
    binary = str(remainder) + binary
    print("binary:" , binary)
    temp = temp // 2
    print("temp:" , temp)


print("\nManual Conversion")
print("Decimal :", number)
print("Binary  :", binary)


# --------------------------------------------------
# Method 3: User Input
# --------------------------------------------------

number = int(input("\nEnter Decimal Number: "))

binary = bin(number)[2:]

print("Decimal :", number)
print("Binary  :", binary)
