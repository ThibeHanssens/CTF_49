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