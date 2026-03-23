<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
Meaning in tragedies

Category:
stego

Hints, info:
300
Meaning in tragedies


</pre>


### Write-up:

The file hides data using three invisible Unicode characters embedded throughout the text: U+200C (ZWNJ), U+200D (ZWJ), and U+FEFF (BOM/ZWNJ no-break space)
There are 327 total invisible chars: 220× ZWNJ, 74× ZWJ, 33× FEFF
Every cluster of invisible chars starts with exactly 4× ZWNJ — this is clearly a structural marker/prefix, not data

Simple ZWNJ=0 / ZWJ=1 binary stream (at any 8-bit alignment) → produces garbage
FEFF as word separator, decoding segments between them → segments have inconsistent lengths, no clean output
Each cluster (after stripping the 4-ZWNJ prefix) decoding to one character → values are all over the place
FEFF = 10 in binary → still garbage
File signatures (PNG, ZIP, JPEG, PDF, GIF) hidden in the bitstream → nothing found


breakthrough: found the 4th invisible character — U+202C (Pop Directional Formatting), which I had been misreading as U+FEFF.
There were actually four symbols:
Char    Code    Bits
ZWNJ    U+200C  00
ZWJ     U+200D  01
PDF     U+202C  10
BOM     U+FEFF  11

Each character is encoded as 2 bits per symbol × 8 symbols = 16 bits, but every other byte is 0x00 (a null), meaning the real data is in every other byte — giving 45 chars total. The encoding is essentially UTF-16 big-endian under the hood, where the [0] bytes are the high bytes of each BMP character.
The CCCC prefix on every cluster was just null bytes padding out the zero high-bytes of ASCII characters.



```
python3 << 'EOF'
# EUREKA! There are FOUR different invisible characters, not three!
# U+200C (ZWNJ): 220
# U+200D (ZWJ): 74  
# U+202C (PDF - Pop Directional Formatting): 33  <-- I was treating this as FEFF!
# U+FEFF (BOM): 33
#
# So we have a 4-symbol alphabet! Total = 220+74+33+33 = 360 symbols
# 360 / 8 = 45 chars
# 360 / 9 = 40 chars
# Let's try with 4 symbols: 200C=0, 200D=1, 202C=2, FEFF=3

text = open('/mnt/user-data/uploads/A_story_not_from_a_jedi.txt', encoding='utf-8').read()

all_inv = [(i, ch) for i, ch in enumerate(text) if ch in '\u200c\u200d\u202c\ufeff']
print(f"Total invisible chars: {len(all_inv)}")

# Map to symbols
sym_map = {'\u200c': 'C', '\u200d': 'D', '\u202c': 'P', '\ufeff': 'F'}
symbols = ''.join(sym_map[ch] for _, ch in all_inv)
print(f"Symbol stream: {symbols}")
print(f"Length: {len(symbols)}")
print()

# Try base-4: C=0, D=1, P=2, F=3
# 360/8=45 chars
print("Base-4, 2 digits per byte attempt (won't work, only 16 values):")
print(f"360 / 8 = {360/8}")  # if 8 base-4 digits per char

# If 8 symbols = 1 char in base-4... that's overkill (4^8 = 65536 values)
# More likely: fixed bits per char
# With 4 symbols = 2 bits each: 360 * 2 = 720 bits / 8 = 90 chars
# OR: treat as binary pairs: CC=00, CD=01, DC=10, DD=11

# First try: each symbol = 2 bits (C=00, D=01, P=10, F=11)
bits = ''.join({'C':'00','D':'01','P':'10','F':'11'}[s] for s in symbols)
print(f"\n2-bits-per-symbol stream length: {len(bits)}")
result = ''
for i in range(0, len(bits)-7, 8):
    val = int(bits[i:i+8], 2)
    result += chr(val) if 32 <= val < 127 else f'[{val}]'
print(f"Decoded: {result}")

# Try other mappings
for mapping in [
    {'C':'00','D':'11','P':'01','F':'10'},
    {'C':'00','D':'10','P':'01','F':'11'},
    {'C':'00','D':'01','P':'11','F':'10'},
]:
    bits2 = ''.join(mapping[s] for s in symbols)
    result2 = ''
    for i in range(0, len(bits2)-7, 8):
        val = int(bits2[i:i+8], 2)
        result2 += chr(val) if 32 <= val < 127 else '.'
    if result2.count('.')/len(result2) < 0.4:
        print(f"Mapping {mapping}: {result2}")
EOF
Output

Total invisible chars: 360
Symbol stream: CCCCDCPCCCCCDCCFCCCCDDDCCCCCDCDPCCCCCPFDCCCCDCDPCCCCDCFCCCCCDCCDCCCCDCDFCCCCCPFDCCCCDCCDCCCCDFCFCCCCDPPFCCCCDDCFCCCCDPPCCCCCDPCDCCCCDPFPCCCCDCCDCCCCDPCPCCCCDPFFCCCCDFDDCCCCDFDCCCCCDDCFCCCCDFDCCCCCDPCDCCCCDFCPCCCCDFDFCCCCDPCDCCCCDFCPCCCCDFCFCCCCDCPDCCCCDPDPCCCCDDPDCCCCDPFFCCCCDFDDCCCCDCPCCCCCDPCDCCCCDFDPCCCCDPDDCCCCCFCPCCCCDPPCCCCCDPFFCCCCDFDDCCCCDFCPCCCCDFCF
Length: 360

Base-4, 2 digits per byte attempt (won't work, only 16 values):
360 / 8 = 45.0

2-bits-per-symbol stream length: 720
Decoded: [0]H[0]C[0]T[0]F[0]-[0]F[0]L[0]A[0]G[0]-[0]A[0]s[0]k[0]S[0]h[0]a[0]n[0]A[0]b[0]o[0]u[0]t[0]S[0]t[0]a[0]r[0]w[0]a[0]r[0]s[0]I[0]f[0]Y[0]o[0]u[0]H[0]a[0]v[0]e[0]2[0]h[0]o[0]u[0]r[0]s
```