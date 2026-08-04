"""
Program: Get a Specific Bit
File: 05_get_bit.py
Topic: Bit Manipulation / Design Verification

Description:
    Extract a particular bit from a number/register.

Formula:
    bit = (value >> position) & 1

Example:
    Register = 0xA5
    Binary   = 10100101

    Get Bit 5
    Result = 1
"""


# --------------------------------------------------
# Method 1: Basic Get Bit
# --------------------------------------------------

value = 0xA5

position = 5

bit = (value >> position) & 1

print("Register :", hex(value))
print("Binary   :", f"{value:08b}")
print("Position :", position)
print("Bit Value:", bit)


# --------------------------------------------------
# Method 2: Using Function
# Recommended for Interviews
# --------------------------------------------------

def get_bit(value, position):
    return (value >> position) & 1


register = 0xA5

print("\nGet Individual Bits")

print("Bit 0:", get_bit(register, 0))
print("Bit 1:", get_bit(register, 1))
print("Bit 2:", get_bit(register, 2))
print("Bit 3:", get_bit(register, 3))
print("Bit 4:", get_bit(register, 4))
print("Bit 5:", get_bit(register, 5))
print("Bit 6:", get_bit(register, 6))
print("Bit 7:", get_bit(register, 7))


# --------------------------------------------------
# Method 3: Display All Bits
# --------------------------------------------------

print("\nAll Register Bits")

for position in range(7, -1, -1):

    bit = get_bit(register, position)

    print("Bit", position, "=", bit)


# --------------------------------------------------
# Method 4: User Input
# --------------------------------------------------

value = int(input("\nEnter register value (decimal): "))

position = int(input("Enter bit position: "))

bit = get_bit(value, position)

print("Binary   :", f"{value:08b}")
print("Bit", position, "=", bit)
