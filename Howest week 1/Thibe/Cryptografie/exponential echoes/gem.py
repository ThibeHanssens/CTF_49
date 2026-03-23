# Exponential Echoes - Universal Matrix Decoder
# Reconstructs the mathematical space to visually reveal the flag

def generate_matrix():
    # 1. The undeniable raw hex bytes straight from xxd
    raw_hex = "4945584e7b2c62230b5d213a62206c3f500d0a2a32693e6565"
    raw_bytes = bytes.fromhex(raw_hex)

    powers_sub = [128, 64, 32, 16, 8, 4, 2, 1]
    powers_add = [1, 2, 4, 8, 16, 32, 64, 128]

    print("Idx | Raw | -128 -64 -32 -16  -8  -4  -2  -1 |  0 | +1  +2  +4  +8 +16 +32 +64 +128")
    print("-" * 88)

    for i, b in enumerate(raw_bytes):
        row = f"{i:2d}  | {b:3d} |"
        
        # 2. Test all exponential subtractions
        for p in powers_sub:
            val = (b - p) % 256
            # Only print readable ASCII characters to clear out the noise
            char = chr(val) if 32 <= val <= 126 else '.'
            row += f"  {char}"
            
        # 3. Zero shift (The structural walls like '{' and '\n')
        char = chr(b) if 32 <= b <= 126 else '.'
        row += f" |  {char} |"
        
        # 4. Test all exponential additions (in case the echo flips polarity)
        for p in powers_add:
            val = (b + p) % 256
            char = chr(val) if 32 <= val <= 126 else '.'
            row += f"  {char}"
            
        print(row)

if __name__ == "__main__":
    generate_matrix()