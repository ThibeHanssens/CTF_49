<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
Change the Jump

Category:
reverse engineering


Hints, info:
150
To jump or not to jump that is the question.


Files:
changethejump


Context:
    It's an ELF-file64 file
    Written in C


</pre>


### Write-up:
Opening the binary in Ghidra reveals the main logic in the entry function. The program:

Builds the flag at runtime using snprintf("HCTF-FLAG-%012lu", 0xaef3279187) into a 20-byte buffer, producing HCTF-FLAG-xxxxxxxxx (truncated due to buffer size)
Sets a string to "Check" (5 characters) and then checks two conditions before printing the flag:

if (length == 7) — "Check" is only 5 chars, so this always fails
if (memcmp(str, "Correct", 7) == 0) — would also fail since the string is "Check", not "Correct"



The program is designed to never print the flag under normal execution — the hint "To jump or not to jump" tells you what to do.
Solution
Two conditional jumps need to be patched in the binary:
File OffsetOriginal bytesPatched bytesReason0x10c574 33 (JE)EB 33 (JMP)Force the length==7 check to always pass0x111275 B3 (JNE)90 90 (NOP)Prevent the memcmp failure from jumping to the fail path

After patching both jumps, running the binary prints the flag