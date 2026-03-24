<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
Hex carving

Category:
reverse engineering


Hints, info:
200
Hex carving



Files:
hexcarving.txt
    A .txt file but it's filled with hexa



</pre>


### Write-up:

### Challenge: Hex Carving
**Category:** Reverse Engineering | **Points:** 200

#### Step 1 — Reconnaissance

The file is a single long line of space-separated hex bytes. The first instinct is to decode them directly:

```python
data = open('hexcarving.txt').read().strip().split()
raw = bytes(int(b, 16) for b in data).decode('latin-1')
```

This reveals text in the format:
```
This is byte nr 1: $This is byte nr 2: $This is byte nr 3: \...
```

#### Step 2 — Finding the structure

Looking closer at the decoded content, there are actual newline characters (`0x0a`) embedded in the hex stream — meaning the file has **multiple lines already baked in**. Splitting on newlines gives **11 meaningful rows**, which is the natural structure of the art.


#### Step 3 — Extracting the data bytes

Each line contains entries of the form `"This is byte nr X: Y"` where `Y` is the actual data character. Extracting `Y` from each entry per line:

```python
import re

data = open('hexcarving.txt').read().strip().split()
raw = bytes(int(b, 16) for b in data).decode('latin-1')

for line in raw.split('\n'):
    extracted = ''.join(re.findall(r'This is byte nr \d: (.)', line))
    if extracted.strip():
        print(extracted.replace('$', '#'))
```


#### Step 4 — Reading the flag

The extracted content is figlet ASCII art using `$` as the filled block character and `\`, `|`, `/`, `_` as outlines. Replacing `$` with `#` and printing with the correct line breaks reveals the flag:
