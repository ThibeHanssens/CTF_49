Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)

Name:
Where is my file ?

Category:
Web

Hints, info:
Medium
Yugi decided to improve his skills and digitized all of his playing cards into a mobile application. He invites you to play a game to try and beat each of the monsters he has prepared for you.
Are you ready for the first battle ?


A file:
Medium
You?ve just started your first job and your boss gives you a simple task: find a ?special? file hidden somewhere in the filesystem of an old server with unpredictable behavior. Because of its size, you?ve been given one day to explore it. Your objective is to traverse the filesystem, identify the ?special? file, and deliver it to your boss. However, be careful not to stray from the initial path, as it may lead to ghost files! Will you manage to uncover it?


Pre-requisities:
directory_crawler.js
OLD one is slow, OLD2 also slow but modified settings for this CTF
directory_crawler_improvedspeed.js -> fastest, rewritten by Lars

Write-up:
Using directory_crawler.js (a script made by AI that crawls based on HTML)
I ran it in 10 tabs (in different directories) to speed up the process
CSC{20 mAny d1rEC7Or1ES IN D1s63LIEF}

Note this is probably the only flag I will share directly cuz it requires you to send like 60k ish requests if it is hidden in the latter part of the first directory