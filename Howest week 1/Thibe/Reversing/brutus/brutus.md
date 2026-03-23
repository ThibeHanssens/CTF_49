<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
brutus

Category:
reverse engineering


Hints, info:
100 points
This is the type of challenge where you need to know the answer ahead of time. Maybe Brutus can help?


Files:
brutus

Context:
    Brutus is an ELF-file, if you run it, it shows this:
        Enter the flag (format HCTF-FLAG-XXXXX):
        Try again!


</pre>


### Write-up:

There's a function called F at 001022a9 -> The flag is constructed by reading the sequence of F() calls in main in reverse order (since strings are built up by prepending/appending characters).
The calls are:
F('9'); F('8'); F('8'); F('4'); F('4'); F('-'); F('G'); F('A'); F('L'); F('F'); F('-'); F('F'); F('T'); F('C'); F('H');
Reading them in reverse gives: HCTF-FLAG-44889
the F function looks up each character in an internal string ( ataddress 0x105340), and main builds the flag character-by-character by calling F() with each encoded character. The characters passed to F() are the encoded values -> reading them reversed reveals the plaintext flag in the expected HCTF-FLAG-XXXXX format

### Solution
The flag is: HCTF-FLAG-44889
