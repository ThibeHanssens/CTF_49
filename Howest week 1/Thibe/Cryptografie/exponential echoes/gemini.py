def test_hypotheses():
    # --- The Knowns ---
    seed = 11         # The 0B separator at Index 8
    target_key = 48   # The required K_0 value for Index 9 (93 - 45)
    
    print(f"--- Testing Seed (11) to Target Key (48) ---")

    # Hypothesis 1: Additive/Subtractive Offset
    # Is the key just the seed plus a constant?
    offset = target_key - seed
    print(f"[+] Additive: Seed + {offset} = {target_key}")
    
    # Hypothesis 2: Multiplicative 
    # Does the seed multiply by something to get near 48?
    # 11 * 4 = 44 (Close, maybe a +4 offset?)
    multiplier = target_key // seed
    remainder = target_key % seed
    print(f"[+] Multiplicative: (Seed * {multiplier}) + {remainder} = {target_key}")

    # Hypothesis 3: Bitwise XOR and Shifts
    # What XORs with 11 to make 48?
    xor_val = seed ^ target_key
    print(f"[+] XOR: Seed ^ {xor_val} = {target_key}")
    
    # Let's look at the binary of the XOR value to see if it's a "clean" number
    print(f"    Binary of {xor_val} is {bin(xor_val)}")

    # Hypothesis 4: The Previous Plaintext Block (CBC style)
    # In CBC, the previous ciphertext or plaintext feeds the next.
    # If Index 8 was a literal plaintext byte, what if it interacts with the next plaintext ('-')?
    pt_9 = 45 # '-'
    print("\n--- Testing CBC/CFB Style Chaining ---")
    print(f"[+] (Seed + PT_9) % 256 = {(seed + pt_9) % 256}")
    print(f"[+] Seed ^ PT_9 = {seed ^ pt_9}") 
    # Note: 11 ^ 45 = 38 (close to 48, but not exact)

    # Hypothesis 5: Left Shift / Bitwise manipulation of the seed
    # 0B is 00001011. If we shift it left by 2:
    shifted_seed = seed << 2 
    print(f"\n[+] Bit Shift: (Seed << 2) = {shifted_seed}")
    print(f"    Notice that {shifted_seed} + 4 = 48!")

test_hypotheses()