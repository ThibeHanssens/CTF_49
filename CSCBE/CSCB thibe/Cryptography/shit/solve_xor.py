import binascii

def xor(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

def solve():
    # Your intercepted hex
    hex_str = "8ae212fefe079dff078a8d6ff38d0787e811fee20c92f448d4ec25bbc336f28d36b6c862b1dd27accc36b7c22cbfc162aecc31addd2aaccc31bb8d3bb1d862acc833abc831aac826fec523ad8d20bbc82cfece2db0cb2bacc027ba83488bde27fed92abb8d24b1c12eb1da2bb0ca62bddf27bac82caac423b28d24b1df62aac527fec327a6d962aec523adc878feee119dd6309bdd719ff971baf21aeedf1d959e1becf2038ce81d99df0d8d980e87f224ede87aef9e3fd4a706bbde36acc23bfed92ab7de62b3c831adcc25bb8d23b8d927ac8d30bbcc26b7c325f0a706b18d2cb1d962adc523acc862a9c436b68d23b0d42db0c862b1d836adc426bb8d36b6c862b1dd27accc36b7c22cf0a748f380629dc22caadf2db2a7"
    ciphertext = binascii.unhexlify(hex_str)
    
    prefix = b"CSC{"
    
    print(f"{'LEN':<5} | {'POTENTIAL KEY (HEX)':<20} | {'DECRYPTED PREFIX'}")
    print("-" * 60)

    for klen in range(1, 31):
        # Derive the key for this length using the first 'klen' bytes
        # We only know the first 4 bytes of plaintext ('CSC{')
        # So we can only reliably get the first 4 bytes of the key.
        # However, if klen <= 4, we have the full key!
        
        # If klen > 4, we have to 'guess' the rest or look for patterns.
        # Let's try the most common key lengths used in CTFs.
        
        derived_key = []
        for i in range(klen):
            if i < len(prefix):
                # We know these!
                derived_key.append(ciphertext[i] ^ prefix[i])
            else:
                # We don't know these yet... let's mark them as 00
                derived_key.append(0)
        
        key_bytes = bytes(derived_key)
        decrypted = xor(ciphertext, key_bytes)
        
        # Clean up output for display
        display_text = "".join([chr(b) if 32 <= b <= 126 else "." for b in decrypted[:30]])
        print(f"{klen:<5} | {key_bytes[:4].hex():<20} | {display_text}...")

solve()