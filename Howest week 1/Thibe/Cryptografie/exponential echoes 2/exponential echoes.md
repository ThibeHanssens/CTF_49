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


### Context:

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

Op basis van de inhoud van de txt:
https://www.cryptool.org/en/cto/ncid/
    Polyphonic Substitution -> Cipher	Probability
    92.68% (keyphrase needed)
https://www.dcode.fr/cipher-identifier
    25% 

Op basis van de hxd:
https://www.dcode.fr/cipher-identifier
60% ASCII
40% XOR cipher
30% Circular Bit Shift
30% EBCDIC Encoding	
25% RC4 Cipher


### Write-up:

EXPONENTIAL IS ZEER BELANGRIJK

als ai ooit iets voorsteld met HTCF{, ga niet door die rabbit-hole
FLAG IS ALTIJD HTCF-FLAG-...
HTCF-FLAG-... zonder uitzonderingen
voorbeeld flags:
	HCTF-FLAG-ILoveReadingThese
	HCTF-FLAG-SP4C3R4C3
	HCTF-FLAG-44889
	HCTF-FLAG-23794
	HCTF-FLAG-ILoveReadingThese
    vooral letters/nummers, maar het kan ook _ underscores hebben in de flag


Eerst iets met dit doen:

```
import string
print(len(list(string.printable)))
```

string.printable has 100 characters. In a Vigenere-style cipher, instead of working mod 256 (all bytes) or mod 95 (visible ASCII), you work mod 100 over the printable character set.The idea: map each printable char to an index 0-99, apply the key mod 100, map back.



als je het volgens deze sturctuur volgt

H   -> 43   +  1   -> 44   (cipher='I')
C   -> 38   +  2   -> 40   (cipher='E')
T   -> 55   +  4   -> 59   (cipher='X')
F   -> 41   +  8   -> 49   (cipher='N')
-   -> 74   + 16   -> 90   (cipher='{')
F   -> 41   + 32   -> 73   (cipher=',')
L   -> 47   + 64   -> 11   (cipher='b')
A   -> 36   + (1)28   -> 64   (cipher='#')
G   -> 42   + (2)56   -> 98   (cipher='0x0B')
-   -> 74   + (5)12   -> 86   (cipher=']')


en dan achterwaarts verd ewerken vanaf dit script:

```
import string

bin="""IEXN{,b#
]!:b l?P
*2i>ee"""

exp = "HCTF-FLAG-"

chars = list(string.printable)
mod = len(chars)

print(chars)

new_str = ""

for i, char in enumerate(bin):
    new_str += chars[(chars.index(char) - 2**i) % mod]

print(new_str)
```