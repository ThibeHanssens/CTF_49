<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
The event

Category:
cryptografie

Hints, info:
400
the event

Thomas was alone drinking from some exotic block tea when he created this challenge. When you remove the dashes of Thomas' real name you get the key.
xtWslCa1iwvxhojyfU4qCs/nCOsjXeQIEv5LJabStvg62BbK

Context:
    Tea is probably XXTEA
    What is thomas?
    Although, there is something important with the dashes, but i don't know what
        It might be that the flag is encrypted without dashes, like HCTFFLAG instead of HCTF-FLAG-
    All flag prefixes are "HCTF-FLAG-...3

Cipher:
xtWslCa1iwvxhojyfU4qCs/nCOsjXeQIEv5LJabStvg62BbK

</pre>


### Write-up:

python bruteforce.py --wordlist "C:\Users\Thibe\Desktop\Tools\Pentesting\rockyou.txt"
-> niet gewerkt :/

oke dus nadenken
we weten dus al de 

"Thomas was alone" is not filler about isolation, and it's not a hint about single blocks. It is a direct reference to the famous 2012 indie puzzle-platformer video game literally called Thomas Was Alone. The creator of the CTF made a clever pun combining his own first name with the game's title.

In that game, you play as a sentient red rectangle AI named Thomas. But "Thomas" is just his nickname.

If you dig into the lore of the game, what is his real name?
His full system designation is Thomas-AT-23-6-12.

"When you remove the dashes of Thomas' real name you get the key."

Take Thomas-AT-23-6-12.
Remove the dashes.
You get ThomasAT23612.

In that game, the main character's full system designation is Thomas-AT-23-6-12. The hint says "remove the dashes of Thomas' real name to get the key" → strip the dashes → ThomasAT23612.
Finding the flag: Standard XXTEA implementations operate on raw bytes with little-endian word packing. The challenge used a common Python library variant that packs words as big-endian internally. Once we matched that implementation:
pythonxxtea_decrypt(ciphertext, b"ThomasAT23612")


### Note to self
origineel denken
zoek meerdere wegen
PAS OP VOOR VALSE PADEN