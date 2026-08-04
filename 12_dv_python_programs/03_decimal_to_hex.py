"""
Program: Decimal to Hexadecimal Conversion
File: 03_decimal_to_hex.py
Topic: Bit Manipulation / Design Verification

Example:
    Decimal     : 254
    Hexadecimal : FE
"""


# --------------------------------------------------
# Method 1: Using Python hex()
# --------------------------------------------------

decimal_number = 254

hex_number = hex(decimal_number)

print("Decimal     :", decimal_number)
print("Hexadecimal :", hex_number)

# Output:
# 0xfe


# --------------------------------------------------
# Remove 0x Prefix and Convert to Uppercase
# --------------------------------------------------

hex_without_prefix = hex(decimal_number)[2:].upper()

print("Hex without 0x :", hex_without_prefix)


# --------------------------------------------------
# Method 2: Manual Conversion
# Important for Interviews
# --------------------------------------------------

number = 254
temp = number

hex_digits = "0123456789ABCDEF"

hexadecimal = ""

while temp > 0:

    remainder = temp % 16

    hexadecimal = hex_digits[remainder] + hexadecimal

    temp = temp // 16


print("\nManual Conversion")

print("Decimal     :", number)
print("Hexadecimal :", hexadecimal)


# --------------------------------------------------
# Method 3: User Input
# --------------------------------------------------

number = int(input("\nEnter Decimal Number: "))

hexadecimal = hex(number)[2:].upper()

print("Decimal     :", number)
print("Hexadecimal :", hexadecimal)
