<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
not what it seems

Category:
reverse engineering


Hints, info:
100 points
not what it seems


Files:
not_what_it_seems.exe

</pre>


### Write-up:

1. in DIE, it shows to be an MSDOS
2. it gevonden in strings:
    Not that difficult once you know. Here is the flag:
    basic_string: construction from null is not valid
    ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_{}
    ;*3$"
    GCC: (Debian 14.2.0-8) 14.2.0

3. 