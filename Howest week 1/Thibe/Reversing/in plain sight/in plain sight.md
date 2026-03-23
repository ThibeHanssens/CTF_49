<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
in plain sight

Category:
reverse engineering


Hints, info:
100 points
in plain sight


Files:
in_plain_sight

Context:
    It's an ELF-file, and if you run it, this happens:
        Enter the password:...


</pre>


### Write-up:


The password is literally stored as a plaintext string in the binary ("I_should_hide_strings_better") + and the flag uses the same F() encoding as the previous challenges
-> reading the calls reversed gives HCTF-FLAG-44894