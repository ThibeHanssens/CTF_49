import string

# Full ciphertext sequence for Line 2 (starting after the 0B separator)
# 0x5D(9) 0x21(10) 0x3A(11) 0x62(12) 0x20(13) 0x6C(14) 0x3F(15) 0x50(16)
c_line2 = [0x5D, 0x21, 0x3A, 0x62, 0x20, 0x6C, 0x3F, 0x50]
prev_c = 0x0B # Start with the separator as the first 'echo' [cite: 102]

VALID_CHARS = string.ascii_letters + string.digits

def get_mods():
    return [0] + [2**i for i in range(8)] + [-(2**i) for i in range(8)]

def solve_line_2(idx, current_str, last_c, shift_val):
    if idx == len(c_line2):
        print(f"FOUND POTENTIAL FLAG PIECE: HCTF-FLAG-{current_str}")
        return

    target_c = c_line2[idx]
    
    # We follow the 'Exponential' hint: shift increases each step 
    for mod in get_mods():
        # Try left shift
        k = ((last_c << shift_val) + mod) % 256
        p = (target_c - k) % 256
        if chr(p) in VALID_CHARS:
            solve_line_2(idx + 1, current_str + chr(p), target_c, shift_val + 1)
            
        # Try right shift (if it produces a different result)
        k_r = ((last_c >> 1) + mod) % 256 # Some echoes used >> 1 in Line 1 [cite: 100]
        p_r = (target_c - k_r) % 256
        if chr(p_r) in VALID_CHARS and k_r != k:
            # If we hit a >> branch, we might stay at a specific shift or reset
            solve_line_2(idx + 1, current_str + chr(p_r), target_c, shift_val)

print("Searching with Logic Filter...")
solve_line_2(0, "G-", 0x5D, 3) # Starting from Index 11 (after G-), shift should be 3