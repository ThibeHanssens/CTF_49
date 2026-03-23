<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
who formatted this

Category:
stego

Hints, info:
250
No seriously who formatted this, I mean it works but why is it so ugly????


Files:
who_formatted_this.py
c_mc_face.c

</pre>


### Write-up:

Both provided files contain the exact same C source code, but with wildly inconsistent and seemingly random indentation -> hence the challenge name.

The category is stego, so the data is hidden in the formatting itself, not in the code logic.

The first instinct was to compare the two files and look at the difference in indentation per line. Every line in c_mc_face.c was indented exactly 4 spaces more than its counterpart in who_formatted_this.py -> a constant offset, which is a dead end on its own (it's always 4 so doesn't bring any value for stego)

BUT: treat the raw leading whitespace count of each line in c_mc_face.c as an ASCII value. Each line is padded to a specific number of spaces, and that number directly maps to a printable character.

```
pythonc_lines = open('c_mc_face.c').readlines()
indents = [len(l) - len(l.lstrip()) for l in c_lines]
flag = ''.join(chr(x) for x in indents)
print(flag)
````

Running this outputs the flag immediately. The .py file turned out to be a red herring -> its indentation encodes garbage values 4 less than the .c file.