Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)


Name:
Is This a Rainbow

Category:
Forensics

Hints, info:
Medium
Our SOC team intercepted a phishing email with a PDF attachment and one of our users clicked on it. We need to analyze the PDF and figure out what the attacker was trying to do. Can you help us out?

A file: challenge.pdf
File to be found: download.jpg

Write-up:
1. Open pdf in HxD
2. Filter for strings with "csc"
    Find this: https://s3.eu-west-1.amazonaws.com/be.cscbe.challenges.2025/007aafd6-e5f5-40d7-b80c-e670f5749642/download.jpg
    And right below:
        Decode k: Lo6IKXqql3sGC3UzMwRqsQ==
        Decode v: bNUoKPHvFCX2dLxAEGZoPw==
    b64d(s)
3. Then idk
    unsolved
