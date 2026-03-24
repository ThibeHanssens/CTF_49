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