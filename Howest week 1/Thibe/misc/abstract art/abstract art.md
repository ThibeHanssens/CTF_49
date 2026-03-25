<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
Abstract Art


Category:
misc

Hints, info:
100
My programmer friend went to art school, and now he won’t stop talking about how his newest masterpiece is "executable." I thought he was just being metaphorical, but he insists there's something hidden in there!


Files:
art.png
    iets vaag, moelijk om te zien


</pre>


### Write-up:

The file

Art.png is actually a JPEG (starts with ff d8 ff e0), not a PNG — file and binwalk lied because of the extension
File size: 2002 bytes
Image dimensions: 209×12 pixels

The pixel content

The image visually shows a repeating rainbow stripe: R → M → B → C → G → Y cycling left to right
Each color appears in blocks of ~12 pixels wide, 12 pixels tall
The blocks vary slightly in height (5–7 colored pixels, rest are black)
The blocks vary slightly in width (11–13 columns wide)

The challenge says
the image should be executable

So let's just go back to google

"programming language that looks like art"
"coding with images"
"executable painting language"
"CTF image that is a program"

-> Piet

https://www.bertnase.de/npiet/npiet-execute.php

upload the file, and boom


### Note to self:
less monkeytyping, more googling