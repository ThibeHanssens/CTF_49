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


Files:
Instance -> broken-record.873f56e58eb232d1.challenge.zone:1339

Write-up:
Write-up:
1. You get this thing with this port, and you have to TCP-connect with that to listen from it

2. Open linux distro, and
'sudo apt install ncat'
'nc broken-record.873f56e58eb232d1.challenge.zone 1339'

netcat is igenlijk een soort TCP-connectie zonder HTTP
so there are 2 ways to listen to these CTF-things
- either it's http and you can see it in web (just use a browser)
- or it's a port that allows an TCP-connection, via a port (use netcat)
netcat is a tool that allows you to make a TCP- or UDP-connection

thibe@DESKTOP-HO00B3T:/mnt/c/Users/Thibe$ nc broken-record.873f56e58eb232d1.challenge.zone 1339 

3. Look at the output:
thibe@DESKTOP-HO00B3T:/mnt/c/Users/Thibe$ nc broken-record.873f56e58eb232d1.challenge.zone 1339
=== INTERCEPTED TRANSMISSION ===
The following encrypted message was captured from a numbers station.
Our analysts believe a short, repeating key was used.

8ae212fefe079dff078a8d6ff38d0787e811fee20c92f448d4ec25bbc336f28d36b6c862b1dd27accc36b7c22cbfc162aecc31addd2aaccc31bb8d3bb1d862acc833abc831aac826fec523ad8d20bbc82cfece2db0cb2bacc027ba83488bde27fed92abb8d24b1c12eb1da2bb0ca62bddf27bac82caac423b28d24b1df62aac527fec327a6d962aec523adc878feee119dd6309bdd719ff971baf21aeedf1d959e1becf2038ce81d99df0d8d980e87f224ede87aef9e3fd4a706bbde36acc23bfed92ab7de62b3c831adcc25bb8d23b8d927ac8d30bbcc26b7c325f0a706b18d2cb1d962adc523acc862a9c436b68d23b0d42db0c862b1d836adc426bb8d36b6c862b1dd27accc36b7c22cf0a748f380629dc22caadf2db2a7
=================================


3. 
When you hear "repeating key" or "looping pattern," it almost always refers to an XOR cipher.
    The Process: Each byte of your plaintext (the flag) is XORed with a byte from a secret key.
    The "Broken Record": If the key is ABC and the message is long, the encryption uses ABCABCABC....
    The Vulnerability: Since you know the flag format for CSCBE is CSC{...}, we can use a Known Plaintext Attack.

4. Decryption strategy:

Phase A: Identify the Key Length
To decrypt XOR, you first need the key. Since the key repeats, we can find its length by looking for patterns, but a faster way is to test the first few bytes against the known flag prefix.

Phase B: Perform the XOR Operation
The ciphertext is in hexadecimal. You need to convert those hex pairs (like 8a, e2, 12) back into bytes and then XOR them with the key.

5. I wrote a script, it's called xor_known_plaintext_attack.py
- First, put the data in a file and refer to that file in the top of the script
- Then, fill in the known prefix/suffix -> CSC{ + }
(This script may be improve or modified depending on the CTF
some CTFs may use the flag as key
some CTFs may use the flag as encrypted text)



=== FULL DECRYPT ===
CSC{S
    EC

-> 
Update prefix to: CSC{S
Run the script.
Look at the output again. You will see the next character clearly

after this it was kinda just monkeyworking my way through it with gemini and creating new ai-generated scripts
no write-up because there is probably just a better way to solve this
    - tools
    - better scripts
    - different techniques
    - ...


i know the pre-fix of either the solution or the decryption is this:
CSC{
and the suffix is htis }
i don't know if we can do a plaintext attack based on the output that we need to decrept
or if we do assume that the pre-fix is from the key itself
also we know that there is some repetition going on, so we don't know when it starts and when it ends. we only know at some point in there it starts and at some point it ends but it may fully rotate i guess

Method 1: The Fast Way (CyberChef)
You can solve this in seconds without coding:
    Open CyberChef.
    Input your hex string.
    Add the "From Hex" recipe.
    Add the "XOR Brute Force" recipe (set key length to 1-10 or use "Index of Coincidence" to find the length).
        Set the Key Length to 1. Usually, this won't show the whole flag, but it might show fragments.
    The "Better" Way: Add "XOR".
        Change the "Key" format to UTF-8.
        Type CSC{ as the key.
        Look at the first 4 bytes of the output. If the result looks like readable text (e.g., repe), those are the first 4 bytes of your Key.
    Identify Key Length: Look for repeating patterns in the hex. If you see the same 4 or 8 hex bytes appearing every $N$ characters, $N$ is your key length.