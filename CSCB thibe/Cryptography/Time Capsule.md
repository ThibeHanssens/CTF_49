Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)


Name:
Time Capsule

Category:
Cryptography

Hints, info:
Easy
Professor Langford's time capsule encryption service has been running since the early days of the internet. He claims that every message is sealed with a unique, unpredictable key ? locked away forever.
We've intercepted a transmission from the service containing a classified secret. Can you unseal it?

Files:
server.py
Instance: time-capsule.b841e857a61a33e3.challenge.zone:1339

Write-up:
1. You get this thing with this port, and you have to TCP-connect with that to listen from it

2. Open linux distro, and
'sudo apt install ncat'
'nc time-capsule.b841e857a61a33e3.challenge.zone:1339'

netcat is igenlijk een soort TCP-connectie zonder HTTP
so there are 2 ways to listen to these CTF-things
- either it's http and you can see it in web (just use a browser)
- or it's a port that allows an TCP-connection, via a port (use netcat)
netcat is a tool that allows you to make a TCP- or UDP-connection

thibe@DESKTOP-HO00B3T:/mnt/c/Users/Thibe$ nc time-capsule.b841e857a61a33e3.challenge.zone 1339

  ╔══════════════════════════════════════════╗
  ║     ⏳  TIME CAPSULE ENCRYPTION  ⏳      ║
  ║  "Sealed with a unique, unbreakable key" ║
  ╚══════════════════════════════════════════╝

Sealed message (hex) : 7b7d997b76bd71028afdbaf515a5cda77c4345a3e1ed35eab9355f3e988b7229bcdb1562ccdb152ab061f4

Good luck unsealing it!



4. Now we look at server.py

Found it! The vulnerability is exactly what we suspected: The seed for the PRNG (Pseudo-Random Number Generator) is the current UNIX timestamp.

Python
timestamp = int(time.time()) # This is the vulnerability
rng = random.Random(timestamp)
In cryptography, if you know the seed, you know the entire key. Since you know roughly when you connected to the server, you can brute-force the timestamp around that window until the decrypted message looks like a flag.

The Strategy
- Get the Current Time: Use int(time.time()) to find the current UNIX timestamp.

- Brute-Force Window: Since there might be a slight clock drift between your computer and the server (or a delay in your connection), check timestamps from, say, 2 minutes ago up until now.

- Replicate Logic: Use the exact same random.Random(seed) logic from server.py to generate the keystream.

- XOR to Victory: XOR the intercepted hex with your generated keystream.

5. Write a file for the above (see TimeCapsule.py)
Refresh the netcat connection, and run the script at the same time