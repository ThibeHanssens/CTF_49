# === CONFIGURATION ===
INPUT_FILE = "brokendata.txt"
KNOWN_PREFIX = "CSC{"   # prefix of the solution, not the key
KNOWN_SUFFIX = "}"      # suffix of the solution, not the key
MAX_KEY_LEN = 50        # We'll check lengths 1 to 50
# =====================

def solve():
    try:
        with open(INPUT_FILE, "r") as f:
            raw_content = f.read().strip()
            # Remove anything that isn't a hex character
            hex_data = "".join(c for c in raw_content if c in "0123456789abcdefABCDEF")
        
        # Hex must be even length. If odd, we trim the last char or pad it.
        if len(hex_data) % 2 != 0:
            print("[!] Warning: Odd length hex detected. Trimming last nibble...")
            hex_data = hex_data[:-1]

        ct_bytes = bytes.fromhex(hex_data)
        print(f"[*] Loaded {len(ct_bytes)} bytes.")

        # --- STEP 1: Find Repeating Patterns ---
        print("[*] Searching for repeating patterns (Broken Record)...")
        for shift in range(1, MAX_KEY_LEN):
            matches = 0
            for i in range(len(ct_bytes) - shift):
                if ct_bytes[i] == ct_bytes[i + shift]:
                    matches += 1
            # If a shift has a high number of matches, it's likely the key length
            if matches > (len(ct_bytes) * 0.1): # Threshold 10%
                print(f"    > Potential Key Length Found: {shift} ({matches} matches)")

        print("-" * 40)

        # --- STEP 2: Derive Key based on Prefix ---
        print(f"[*] Key fragments for likely lengths:")
        prefix_bytes = KNOWN_PREFIX.encode()
        
        for length in range(1, MAX_KEY_LEN):
            # Calculate what the key would look like for this length
            # Key = Ciphertext ^ Plaintext
            derived_key = []
            for i in range(min(length, len(prefix_bytes))):
                derived_key.append(ct_bytes[i] ^ prefix_bytes[i])
            
            key_str = "".join(chr(b) if 32 <= b <= 126 else "." for b in derived_key)
            
            # Check the suffix against this length
            suffix_key_idx = (len(ct_bytes) - 1) % length
            suffix_match = " "
            if suffix_key_idx < len(prefix_bytes):
                expected_last_key_byte = ct_bytes[-1] ^ ord(KNOWN_SUFFIX)
                if derived_key[suffix_key_idx] == expected_last_key_byte:
                    suffix_match = "<- SUFFIX MATCH!"
            
            if len(key_str) >= 3: # Only show lengths that could reasonably be a word
                print(f"Len {length:2}: {key_str:10} {suffix_match}")

        print("-" * 40)
        final_key = input("Look at the output above. Can you see a repeating word?\nEnter full key: ").strip()
        
        if final_key:
            key_bytes = final_key.encode()
            decrypted = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(ct_bytes)])
            print("\n=== DECRYPTED RESULT ===")
            print(decrypted.decode(errors="ignore"))
            print("========================")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    solve()