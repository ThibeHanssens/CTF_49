<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
calculate_me_fast

Category:
reverse engineering


Hints, info:
100 points
calculate_me_fast


Files:
calculate_me_fast

Context:
    It's an ELF-file, and if you run it, this happens:
     ./calculate_me_fast
        Question 1: 94 - 20 = ?
        74
        Too slow! You failed.
    doesn't matter how fast or how slow, it keeps saying the same thing



</pre>


### Write-up:

I put it in ghidramcp:

It asks 1000 math questions (only + and -, numbers 0–99)
You must answer each one within a time limit (checked against 
_DAT_00104108 milliseconds — likely ~1ms or so, way too fast for a human)

If you get all 1000 right in time AND within the loop, the flag is revealed using the same F() encoding trick as before

The flag is already visible in the main decompilation! The F() calls are:
F('1'); F('9'); F('6'); F('4'); F('8'); F('-'); F('G'); F('A'); F('L'); F('F'); F('-'); F('F'); F('T'); F('C'); F('H');


### Solution


### Note to self:
