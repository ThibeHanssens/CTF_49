# The list of numbers taken directly from your decompiled Kuriboh class
encoded = [
    139, 149, 146, 209, 130, 208, 136, 191, 209, 213, 191, 150, 211, 146, 
    153, 191, 131, 149, 148, 211, 193, 193, 193, 191, 209, 130, 217, 132, 
    129, 217, 131, 134, 215, 132, 213, 130, 215, 134, 209, 133
]

# The XOR key found in the check() function
key = 224

password = ""

# Loop through each number, XOR it with 224, and convert back to a character
for num in encoded:
    password += chr(num ^ key)

print("--- CSCBE Kuriboh Challenge Solver ---")
print(f"Password String: {password}")
print(f"Full Flag: CSC{{{password}}}")