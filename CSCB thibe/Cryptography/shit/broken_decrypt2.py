# === CONFIGURATION ===
INPUT_FILE = "brokendata.txt"
KNOWN_PREFIX = "CSC{SECRET_" 
# =====================

def solve():
    with open(INPUT_FILE, "r") as f:
        hex_data = "".join(c for c in f.read() if c in "0123456789abcdefABCDEF")
    ct = bytes.fromhex(hex_data)
    
    # We use a long range to see the pattern
    prefix = KNOWN_PREFIX.encode()
    
    print("[*] Deriving key from prefix...")
    # Calculate the key bytes we know
    derived_key = [ct[i] ^ prefix[i] for i in range(len(prefix))]
    
    # Show the hex and look for the 'deadbeef' pattern
    print(f"[*] Key bytes (Hex): {' '.join(f'{b:02x}' for b in derived_key)}")
    
    # AUTO-FIX: Let's assume the key is 'DEADBEEF' based on your last result
    # Your last hex had 'ad 42 de ad 42' which is 'DEADB'
    # The actual key is likely a 4-byte or 8-byte 'DEADBEEF'
    
    # Let's try 8-byte key: DEADBEEF
    for length in [4, 8, 9, 10]:
        key = [ct[i] ^ ord("CSC{SECRET_"[i]) for i in range(min(length, 11))]
        # If length is 8, and we have 11 chars, we can see if it repeats!
        
        test_key = [ct[i] ^ ord("CSC{")[i] for i in range(4)]
        # Based on 'c9b15185', let's just brute force the shift
        print(f"\n--- Testing Key Length {length} ---")
        full_key = [ct[i] ^ ord(KNOWN_PREFIX[i]) for i in range(min(len(ct), length))]
        dec = bytes([ct[i] ^ full_key[i % len(full_key)] for i in range(len(ct))])
        print(dec.decode(errors="ignore")[:150])

solve()