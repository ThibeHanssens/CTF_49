Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)

Name:
Kuriboh

Category:
Reverse Engineering

Hints, info:
Medium
Yugi decided to improve his skills and digitized all of his playing cards into a mobile application. He invites you to play a game to try and beat each of the monsters he has prepared for you.
Are you ready for the first battle ?

A file: kuriboh.apk

Write-up:
1. First, for triage I looked at strings.
Which showed a very long list, I just grepped for "CSC" and moved on without results.
2. Then, I put the .apk file into DIE
-> It’s an Android app (API 31/Android 12) written in Java using Gradle 8.1.1.
3. Now I decided to put it into Jadx-GUI
https://github.com/skylot/jadx/releases
4. Open the file in Jadx-GUI
Look at resources -> assets -> private.tar
export this file
5. Extract the .tar
tar -xvf private.tar
Within the files, you find main.pyc
6. .pyc compiled python-code
So we wanna decompile it
Tool: https://github.com/extremecoders-re/decompyle-builds/releases/latest/download/pycdc.exe
.\pycdc.exe main.pyc > main_decompiled.py
7. Look at the main_decompiled.py file
Based on that code, we still need the password.
But based on that code, we can wrote a new python-script to solve this problem.
We just need the list with encoded-numbers, and use the XOR-key to decode it.


encoded = [
    see decompiled python-code, re-use that list
]

key = 224
password = ""

for num in encoded:
    password += chr(num ^ key)

print(f"CSC{{{password}}}")


I saved this as kuriboh.py

And then do:
python kuriboh.py