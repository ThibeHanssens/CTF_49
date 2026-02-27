Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)


Name:
Hear no flag

Category:
Cryptography

Hints, info:
Medium

The Canticle of Turning
    In the eastern wing of the Sanctum of the Veiled Crown stood the Hall of Resonance ? a circular chamber of smooth marble walls and a domed ceiling crafted to carry even the faintest whisper. There, the Custodians practiced the Discipline of Echoes. They believed that truth, like sound, does not vanish. It travels. It bends. It returns altered by the path it has taken. What begins as a simple utterance may, through repetition and motion, become something entirely transformed. Among the relics recovered from the Hall lies a narrow strip of vellum known as The Canticle of Turning. Upon it is inscribed a single sequence of characters ? bold, deliberate, and uninterrupted. The Custodians left no commentary beside it. No marginal notes. No translation.

    This is the Canticle exactly as it was found: CTD{COQ_BUVB_LD-UNYP_CZON-SOY_LVXSHRS}

    No other markings accompany it. No additional instructions survive.

    The Hall of Resonance now stands silent, its echoes long faded from stone.

    The Canticle remains.

    Decipher it.

    p.s. ({}_-) are not encrypted



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