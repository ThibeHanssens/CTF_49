import collections

# === CONFIGURATION ===
INPUT_FILE = "brokendata.txt"
KNOWN_PREFIX = "CSC{SECRET_B"
# =====================

def get_key_length(data, max_len=40):
    best_len = 0
    max_score = 0
    for l in range(1, max_len):
        score = 0
        for i in range(len(data) - l):
            if data[i] == data[i+l]:
                score += 1
        if score > max_score:
            max_score = score
            best_len = l
    return best_len

def solve():
    with open(INPUT_FILE, "r") as f:
        hex_data = "".join(c for c in f.read() if c in "0123456789abcdefABCDEF")
    ct = bytes.fromhex(hex_data)
    
    # 1. Find Key Length
    length = get_key_length(ct)
    print(f"[*] Likely Key Length: {length}")

    # 2. Recover Key
    # We use the prefix for the first 4 bytes
    prefix = KNOWN_PREFIX.encode()
    key = bytearray([ct[i] ^ prefix[i] for i in range(len(prefix))])
    
    # For the remaining bytes of the key, we use frequency analysis
    # Most common byte in English is often ' ' (space, 0x20)
    for i in range(len(prefix), length):
        # Gather all bytes encrypted with this specific key position
        block = ct[i::length]
        # Find the most frequent byte in this block
        most_common = collections.Counter(block).most_common(1)[0][0]
        # Key byte = ciphertext_byte ^ ' '
        key.append(most_common ^ ord(' '))

    print(f"[*] Recovered Key: {key.decode(errors='ignore')} (Hex: {key.hex()})")
    
    # 3. Decrypt
    decrypted = bytes([b ^ key[i % len(key)] for i, b in enumerate(ct)])
    print("\n=== FULL DECRYPT ===")
    print(decrypted.decode(errors="ignore"))

solve()