import string

hex_data = "8ae212fefe079dff078a8d6ff38d0787e811fee20c92f448d4ec25bbc336f28d36b6c862b1dd27accc36b7c22cbfc162aecc31addd2aaccc31bb8d3bb1d862acc833abc831aac826fec523ad8d20bbc82cfece2db0cb2bacc027ba83488bde27fed92abb8d24b1c12eb1da2bb0ca62bddf27bac82caac423b28d24b1df62aac527fec327a6d962aec523adc878feee119dd6309bdd719ff971baf21aeedf1d959e1becf2038ce81d99df0d8d980e87f224ede87aef9e3fd4a706bbde36acc23bfed92ab7de62b3c831adcc25bb8d23b8d927ac8d30bbcc26b7c325f0a706b18d2cb1d962adc523acc862a9c436b68d23b0d42db0c862b1d836adc426bb8d36b6c862b1dd27accc36b7c22cf0a748f380629dc22caadf2db2a7"
ciphertext = bytes.fromhex(hex_data)

def try_prefix(prefix_str):
    prefix = prefix_str.encode()
    # XOR the start of the ciphertext with our guess
    key_guess = bytes([ciphertext[i] ^ prefix[i] for i in range(len(prefix))])
    
    # Now use that key to decrypt the WHOLE thing
    # We assume the key repeats every 'loop_length'
    loop_length = 222 # From your previous result
    
    # Actually, let's just XOR the ciphertext with the known prefix 
    # to see what the KEY looks like.
    print(f"Testing Prefix: {prefix_str}")
    print(f"Resulting Key Segment: {key_guess.hex()}")
    
    # Try to see if the key segment is ASCII
    printable_key = "".join(chr(b) if 32 <= b <= 126 else "." for b in key_guess)
    print(f"Key as Text: {printable_key}")
    print("-" * 30)

# Start with what we know
try_prefix("CSC{")