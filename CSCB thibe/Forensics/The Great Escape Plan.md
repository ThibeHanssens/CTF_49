Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)


Name:
The Great Escape Plan

Category:
Forensics

Hints, info:
Hard
Totally normal office traffic. Definitely not a leak.

A file: capture.pcap

Write-up:
1. Looked at the stuff in wireshark
2. One request seemed kinda off
11854	142.959650	172.28.0.40	172.28.0.30	TCP	74	[TCP Port numbers reused] 37972 → 8080 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM TSval=3311094422 TSecr=0 WS=128
3. 