from Crypto.Cipher import AES
import hashlib

# De ciphertext uit je opgave
ciphertext_hex = "66e83538c85aee74c8ad5ae783bd6686cd7943bf221cadc183b30af7346c4829"
ciphertext = bytes.fromhex(ciphertext_hex)

def is_printable(data):
    return all(32 <= b <= 126 for b in data)

def try_decrypt(key):
    # Probeer verschillende modi (ECB is het meest 'niet intelligent')
    # 1. ECB Mode
    try:
        cipher = AES.new(key, AES.MODE_ECB)
        pt = cipher.decrypt(ciphertext)
        if b"HCTF" in pt:
            return f"ECB", pt
    except:
        pass

    # 2. CBC Mode (vaak is IV gelijk aan de Key bij 'domme' implementaties)
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv=key[:16])
        pt = cipher.decrypt(ciphertext)
        if b"HCTF" in pt:
            return f"CBC", pt
    except:
        pass
    
    return None

print("--- Start Brute Force op HCTF-FLAG-AESxxx ---")

found = False
for i in range(1000):
    num = str(i).zfill(3)
    candidate_flag = f"HCTF-FLAG-AES{num}" # Dit is 16 karakters lang!
    
    # AES keys moeten 16, 24 of 32 bytes zijn. 
    # "HCTF-FLAG-AESxxx" is precies 16 bytes.
    key = candidate_flag.encode()

    result = try_decrypt(key)
    if result:
        mode, pt = result
        print(f"\n[!] MATCH GEVONDEN!")
        print(f"Nummer: {num}")
        print(f"Modus:  {mode}")
        print(f"Key:    {candidate_flag}")
        print(f"Result: {pt.decode(errors='ignore')}")
        found = True
        break

if not found:
    print("\n[-] Geen directe match gevonden met de standaard key-format.")
    print("[*] Suggestie: Is de key misschien de MD5 hash van 'AESxxx'?")