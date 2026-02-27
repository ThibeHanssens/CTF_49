Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)


Name:
Catch of the Day

Category:
Forensics

Hints, info:
Our network admin was monitoring traffic on the corporate LAN when they spotted something unusual. It seems someone accessed a classified internal report they definitely shouldn't have.
We managed to grab a packet capture before the connection ended. Can you take a look and figure out what was stolen?

A file: catch_of_the_day_.pcap

Write-up:
1. Open file in wireshark
2. http.request.method == "GET" -> shows some interesting stuff related to the issue
    But if you remove this filter and just filter for strings with "CSC", you'll find the key immeadetely (copy as ASCII)