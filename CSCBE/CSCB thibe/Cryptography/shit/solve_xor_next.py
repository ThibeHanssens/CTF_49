import binascii
from collections import Counter

def solve_xor_statistically():
    hex_str = "8ae212fefe079dff078a8d6ff38d0787e811fee20c92f448d4ec25bbc336f28d36b6c862b1dd27accc36b7c22cbfc162aecc31addd2aaccc31bb8d3bb1d862acc833abc831aac826fec523ad8d20bbc82cfece2db0cb2bacc027ba83488bde27fed92abb8d24b1c12eb1da2bb0ca62bddf27bac82caac423b28d24b1df62aac527fec327a6d962aec523adc878feee119dd6309bdd719ff971baf21aeedf1d959e1becf2038ce81d99df0d8d980e87f224ede87aef9e3fd4a706bbde36acc23bfed92ab7de62b3c831adcc25bb8d23b8d927ac8d30bbcc26b7c325f0a706b18d2cb1d962adc523acc862a9c436b68d23b0d42db0c862b1d836adc426bb8d36b6c862b1dd27accc36b7c22cf0a748f380629dc22caadf2db2a7"
    ct = binascii.unhexlify(hex_str)

    # We are betting on Key Length 3 based on your previous output
    K_LEN = 3
    key = []

    for i in range(K_LEN):
        # Grab every 3rd byte (column i)
        column = ct[i::K_LEN]
        
        # In CTF flags, the most common character is usually '_' or ' ' or 'e'
        # But we also KNOW the first 3 bytes are 'CSC'
        # So for column 0: Key[0] = CT[0] ^ 'C'
        # For column 1: Key[1] = CT[1] ^ 'S'
        # For column 2: Key[2] = CT[2] ^ 'C'
        
        prefix = b"CSC"
        key.append(ct[i] ^ prefix[i])

    final_key = bytes(key)
    print(f"[*] Deduced Key: {final_key.hex()} ({final_key})")
    
    # Decrypt everything
    pt = bytes([ct[i] ^ final_key[i % K_LEN] for i in range(len(ct))])
    print("\n[+] Decrypted Message:")
    print(pt.decode(errors='ignore'))

solve_xor_statistically()