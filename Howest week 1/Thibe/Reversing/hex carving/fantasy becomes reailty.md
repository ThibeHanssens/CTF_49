<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
What if fantasy becomes reality

Category:
reverse engineering


Hints, info:
What if fantasy becomes reality
100


Files:
fantasy

Context:
    It's an ELF-file64 file
    Written in C


</pre>


### Write-up:

The logic is:

Takes argv[0] (the program's own filename/path)
Calls find_last_of with the string at 0x103008 — almost certainly "/\\" (path separators)
Takes the substr after the last separator — i.e. just the basename of the executable
Compares that basename to "reality"
If it matches → prints the flag

The challenge name is the hint: "What if fantasy becomes reality" — you rename the binary from fantasy to reality and run it!Rename binary to reality and run itRename binary to reality and run itThe flag is: HCTF-FLAG-23797

How it works: The binary reads argv[0] (its own path), strips the directory part to get just the filename, and checks if it equals "reality". If yes, it prints the flag. The challenge title was the exact solution — rename fantasy → reality and run it. The F() calls (reversed: HCTF-FLAG-23797) encode the flag using the same obfuscation pattern seen in all the other challenges.
