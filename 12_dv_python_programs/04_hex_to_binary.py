"""
Program: Hexadecimal to Binary Conversion
File: 04_hex_to_binary.py
Topic: Bit Manipulation / Design Verification

Example:
    Hexadecimal : FE
    Binary      : 11111110
"""


# --------------------------------------------------
# Method 1: Using Python int() and bin()
# --------------------------------------------------

hex_number = "FE"

decimal_number = int(hex_number, 16)

binary_number = bin(decimal_number)

print("Hexadecimal :", hex_number)
print("Decimal     :", decimal_number)
print("Binary      :", binary_number)


# --------------------------------------------------
# Remove 0b Prefix
# --------------------------------------------------

binary_without_prefix = bin(decimal_number)[2:]

print("Binary without 0b :", binary_without_prefix)


# --------------------------------------------------
# Method 2: Manual Conversion Using Mapping
# Important for Interviews
# --------------------------------------------------

hex_number = "FE"

hex_to_binary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

binary = ""

for digit in hex_number:
    binary = binary + hex_to_binary[digit]

print("\nManual Conversion")
print("Hexadecimal :", hex_number)
print("Binary      :", binary)


# --------------------------------------------------
# Method 3: User Input
# --------------------------------------------------

hex_number = input("\nEnter Hexadecimal Number: ").upper()

decimal_number = int(hex_number, 16)

binary_number = bin(decimal_number)[2:]

print("Hexadecimal :", hex_number)
print("Binary      :", binary_number)
