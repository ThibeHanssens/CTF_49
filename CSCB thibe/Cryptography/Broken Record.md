Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)


Name:
Broken Record

Category:
Cryptography

Hints, info:
Easy

Our field agents intercepted a coded radio transmission from a numbers station broadcasting on a loop. The signal repeats the same short pattern over and over ? almost like a broken record.

Analysts believe the message contains classified operational intel. Connect to the listening post to retrieve the intercepted ciphertext.


Files: Instance

Write-up:
1. First we compare what we have and what it needs to become:
CTD{COQ_BUVB_LD-UNYP_CZON-SOY_LVXSHRS}
-> CSC{...}
So CTD has to become CSC
2. Since it's only ascii, i first assumed a rotational encryption
C either rotated 26, or didn't rotate at all.
T can rotate with -1
C can rotate with -1 also
...
3. Fibonacci sequence uses the sequence 0, 1, 1, 2, 3, 5, 8, 13,... to determine the shift for each letter.
Using this sequence, we can find the decryption.