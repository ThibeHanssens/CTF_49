<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
Exponential Echoes

Category:
Cryptography


Hints, info:
300 points
Exponential Echoes


Files:
binarynt.txt


</pre>


### Write-up:

1. binarynt.txt is a regular .txt file, this content:
IEXN{,b#
]!:b l?P
*2i>ee
--------
xxd binarynt.txt
00000000: 4945 584e 7b2c 6223 0b5d 213a 6220 6c3f  IEXN{,b#.]!:b l?
00000010: 500d 0a2a 3269 3e65 65                   P..*2i>ee
--------
from HxD
"49 45 58 4E 7B 2C 62 23 0B 5D 21 3A 62 20 6C 3F 50 0D 0A 2A 32 69 3E 65 65"
------------
### Solution

notiteis:
exponential echoes
kut
belangrijk:
1. soms begint ai zichzelf om te leiden en denkt ie dat de flag-prefix HTCF{...} is
als ai ooit iets voorsteld met HTCF{, ga niet door die rabbit-hole
vermeld duidelijk dat de prefix sowieso HTCF-FLAG-... is

2. je begint door eerst xxd te doen
dan de rauwe bytes te nemen
2^i subtraction gives HCTF for positions 0–3 perfectly, then idk what happesn after
key = 2^i (subtract): 1, 2, 4, 8, ...?
73-1=72='H', 69-2=67='C', 88-4=84='T', 78-8=70='F'?
perhaps try these things out and then if it doesn't work whatever?


The formula used is:
Plaintext Byte = Ciphertext Byte - 2^i
(where 'i' is the index starting from 0)

Here is the exact mathematical breakdown for the first four characters:

Index 0: Ciphertext 'I' (ASCII 73)
Calculation: 73 - 2^0 = 73 - 1 = 72
Result: ASCII 72 is 'H'

Index 1: Ciphertext 'E' (ASCII 69)
Calculation: 69 - 2^1 = 69 - 2 = 67
Result: ASCII 67 is 'C'

Index 2: Ciphertext 'X' (ASCII 88)
Calculation: 88 - 2^2 = 88 - 4 = 84
Result: ASCII 84 is 'T'

Index 3: Ciphertext 'N' (ASCII 78)
Calculation: 78 - 2^3 = 78 - 8 = 70
Result: ASCII 70 is 'F'



but what happens after? idk

keep trying new new things

onthoud de tips:
binarynt.exe
exponential echo
waar wijst binarynt naar?
wat zo er exponential zijn? waar zit de echo?
misschien betekent de echo dat je de eerste bytes kan xoren met de latere bytes?
misschien exponential omdat je voor elk regeltje een gelijkaardige formule moet gebruiken met exponentieel increasende values?




HCTF-FLAG- confirmed with key[i-2] XOR key[i-3]! Position 10 gives F then breaks. But we're SO close.
The recurrence key[i] = key[i-2] XOR key[i-3] gives HCTF-FLAG-F then non-printable. The suffix digits need keys that produce ASCII 0-9 (48-57).




Start-Process cmd -ArgumentList '/c start "" /high python3 solve.py ^| tee results.txt'
Start-Process cmd -ArgumentList '/c start "" /high python3 solve.py > results.txt'



key[i-2] XOR key[i-3] : HCTF-FLAG-F[128] V]...

key[i-3] XOR key[i-4] : HCTF-FLAG-Fn>1?:H2SJ...

key[i-1] XOR key[i//2] : HCTF-FLAG-(n>x)\H>iJ...

key[i-1] XOR key[i>>3] : HCTF-FLAG-Dn*xI\:>yJuq

key[i-1] XOR key[i>>4] : HCTF-FLAG-En+xJ\4>sJoq

key[i-3] XOR key[i>>1] : HCTF-FLAG-6r>Z-P&.uNEu

Cycling period 10 : HCTF-FLAG-9\ ...



key[i-2]^key[i-3] → F then breaks
key[i-3]^key[i-4] → Fn>l?:H2SJ
lag=2^(i%1) → Fn,xK\6>uJqq


