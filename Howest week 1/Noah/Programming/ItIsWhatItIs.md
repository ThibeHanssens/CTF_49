<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
It is what it is

Category:
Programming


Hints, info:
150 points


Files:
polyglot.exe

Problem description:
    - Is is an executable file.
    - When the file it executed, it creates a temporary folder with generated scripts.
      - We have to find what languages these are.

</pre>


### Write-up:
- Open the .exe file with PEViewer, after some searching you will find strings of programming languages.
- When the program is run it creates the temp folder/files and it asks the user which programming language it is.

### Solution
- Giving the found programming languages strings inside the program, as input in order will give you the flag: `HCTF-FLAG-J4vaScriptIsTheGoat!`
