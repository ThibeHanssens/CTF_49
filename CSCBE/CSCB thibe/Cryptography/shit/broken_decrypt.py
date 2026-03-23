# === CONFIGURATION ===
INPUT_FILE = "brokendata.txt"
# We use exactly 9 or more characters to recover the full 9-byte key
KNOWN_PREFIX = "CSC{SECRET_B" 
# =====================

def solve():
    try:
        with open(INPUT_FILE, "r") as f:
            hex_data = "".join(c for c in f.read() if c in "0123456789abcdefABCDEF")
        ct = bytes.fromhex(hex_data)
        
        # The 'Broken Record' length we found earlier
        KEY_LEN = 9
        prefix = KNOWN_PREFIX.encode()
        
        # 1. Recover the full 9-byte key
        key = [0] * KEY_LEN
        for i in range(len(prefix)):
            key[i % KEY_LEN] = ct[i] ^ prefix[i]
        
        print(f"[*] Full 9-byte Key Recovered (Hex): {' '.join(f'{b:02x}' for b in key)}")
        
        # 2. Decrypt the entire transmission
        decrypted = bytes([ct[i] ^ key[i % KEY_LEN] for i in range(len(ct))])
        
        print("\n=== FINAL DECRYPTED TRANSMISSION ===")
        # Replace non-printable chars with spaces for a clean output
        decoded_text = "".join(chr(b) if 32 <= b <= 126 or b == 10 else " " for b in decrypted)
        print(decoded_text)
        print("======================================")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    solve()