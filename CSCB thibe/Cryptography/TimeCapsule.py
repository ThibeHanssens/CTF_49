import random
import time

# The hex you intercepted from the server
intercepted_hex = "829cde77958da228c5e7363d1e38306f202851459213d3524467a6c1caab532d9786ce85bc559eda8290a6"
ciphertext = bytes.fromhex(intercepted_hex)

# 1. Get current time as a starting point
now = int(time.time())

print(f"[*] Starting brute-force around timestamp: {now}")

# 2. Search a window of 300 seconds (5 minutes) backwards from now
for offset in range(300):
    test_seed = now - offset
    
    # 3. Replicate the server's encryption logic
    rng = random.Random(test_seed)
    keystream = bytes([rng.randint(0, 255) for _ in range(len(ciphertext))])
    
    # 4. XOR the ciphertext with our guessed keystream
    decrypted = bytes(a ^ b for a, b in zip(ciphertext, keystream))
    
    # 5. Check if we found the flag (usually starts with CSC)
    if b"CSC" in decrypted:
        print(f"\n[+] SUCCESS! Seed found: {test_seed}")
        print(f"[+] Flag: {decrypted.decode()}")
        break
else:
    print("\n[-] Failed to find the seed. Try increasing the search window or checking your system clock.")