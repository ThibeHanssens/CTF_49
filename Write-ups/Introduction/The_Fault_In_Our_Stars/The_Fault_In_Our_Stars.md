Name:
The Fault In Our Stars

Context:
Uni, subject CTF, introduction

Team:
49 chicken nuggets

Write-up:

![Card stars](cards_stars.png)

1. We received cards, and placed them on the table. We orientated the cards based on the amount of stars in the corner.
2. We looked at the stars on the cards, and treated them as binary.
3. After trying some combinations/possibilities, we figured out that the we could use the following interpretation.
   1. Card 1: 01010011 01000101 01001110 01010101
   2. Card 2: 01010010 01101001 00110001 01010100
   3. Card 3: 01010110 01000100 01010010 01010011
   4. Card 4: 01001110 01010001 00111101 00111101
4. This binary translated into 'SENURi1TVDRSNQ==' We recognized this Base64, which translated to 'HCTF-ST4R5'.
   1. Cyberchef recipe: https://toolbox.itsec.tamu.edu/#recipe=From_Binary('Space',8)From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=MDEwMTAwMTEgMDEwMDAxMDEgMDEwMDExMTAgMDEwMTAxMDEKMDEwMTAwMTAgMDExMDEwMDEgMDAxMTAwMDEgMDEwMTAxMDAKMDEwMTAxMTAgMDEwMDAxMDAgMDEwMTAwMTAgMDEwMTAwMTEKMDEwMDExMTAgMDEwMTAwMDEgMDAxMTExMDEgMDAxMTExMDE
5. We found the flag!