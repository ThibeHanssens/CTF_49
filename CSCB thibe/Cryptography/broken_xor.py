def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

# The intercepted transmission
hex_data = "8ae212fefe079dff078a8d6ff38d0787e811fee20c92f448d4ec25bbc336f28d36b6c862b1dd27accc36b7c22cbfc162aecc31addd2aaccc31bb8d3bb1d862acc833abc831aac826fec523ad8d20bbc82cfece2db0cb2bacc027ba83488bde27fed92abb8d24b1c12eb1da2bb0ca62bddf27bac82caac423b28d24b1df62aac527fec327a6d962aec523adc878feee119dd6309bdd719ff971baf21aeedf1d959e1becf2038ce81d99df0d8d980e87f224ede87aef9e3fd4a706bbde36acc23bfed92ab7de62b3c831adcc25bb8d23b8d927ac8d30bbcc26b7c325f0a706b18d2cb1d962adc523acc862a9c436b68d23b0d42db0c862b1d836adc426bb8d36b6c862b1dd27accc36b7c22cf0a748f380629dc22caadf2db2a7"
ciphertext = bytes.fromhex(hex_data)

# Known prefix
prefix = b"CSC{"

# 1. Recover the start of the key
# Since Ciphertext ^ Plaintext = Key
recovered_key_part = xor_bytes(ciphertext[:4], prefix)
print(f"[*] Potential Key Start: {recovered_key_part}")

# 2. Finding the Key Length (The 'Broken Record' loop)
# We look for the distance between the repeating hex pattern you found
pattern = bytes.fromhex("8d36b6c862b1dd27accc36b7c22c")
first_occurrence = ciphertext.find(pattern)
second_occurrence = ciphertext.find(pattern, first_occurrence + 1)
key_length = second_occurrence - first_occurrence

print(f"[*] Detected loop length: {key_length} bytes")

# 3. Recover the FULL Key
# We know the key repeats every 'key_length' bytes. 
# Let's take the first 'key_length' bytes of ciphertext and 
# try to guess the plaintext to get the key. 
# BUT, if the whole message IS the flag, then the key is likely 
# just a shorter word.

def try_decrypt(k):
    decrypted = ""
    for i in range(len(ciphertext)):
        decrypted += chr(ciphertext[i] ^ k[i % len(k)])
    return decrypted

# Let's use the property that the key itself is likely repeating 
# and the message contains the flag.
# If we XOR the ciphertext with itself shifted by the loop length, 
# we can often eliminate the key.

# Strategy: XOR the ciphertext with 'CSC{' to see if the key emerges
full_recovered_key = xor_bytes(ciphertext, b"CSC{S") # Based on your "CSC{S" find
print(f"[*] Hex of key start: {full_recovered_key[:10].hex()}")

# Manual override: Based on the pattern, let's try to extract the key 
# by assuming the flag starts at the beginning.
full_key = xor_bytes(ciphertext[:key_length], b"") # Placeholder

# FINAL ATTACK: Since it's a "Broken Record", the message itself 
# might be the key, or the flag is hidden inside a repeating stream.
# Let's print the XOR with the first 4 bytes and see the pattern.
key_segment = xor_bytes(ciphertext[:4], b"CSC{")

# Let's try to brute force the key length from 1 to 50
for length in range(1, 60):
    key = xor_bytes(ciphertext[:4], b"CSC{")
    # This is a simplification; realistically we use a tool like 'xortool'

