Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)


Name:
D?j? Brew

Category:
Reverse Engineering

Hints, info:
Easy
The local coffee shop "D?j? Brew" just launched their new digital loyalty program. They claim that only premium members get access to the secret house blend recipe. You managed to grab a copy of their membership validation app. Can you figure out the secret membership code?

2 files:
deja_brew


Pre-requisities:

sudo apt install checksec

I use the command below:

TARGET="deja_brew" # <--- Put your new filename here
{
  echo "--- 1. FILE TYPE & ARCHITECTURE ---"; 
  file "$TARGET";
  
  echo -e "\n--- 2. SECURITY MITIGATIONS ---"; 
  checksec --file="$TARGET";
  
  echo -e "\n--- 3. STRINGS TRIAGE (FLAG/URL/PATH) ---"; 
  strings "$TARGET" | grep -E -i "flag|ctf|http|/home/|/etc/";
  
  echo -e "\n--- 4. INTERESTING FUNCTIONS (User Defined) ---"; 
  # This filters for code (T) but ignores common library junk like __libc
  nm "$TARGET" | grep " T " | grep -v "__"; 
  
  echo -e "\n--- 5. SHA256 HASH (For OSINT/VT) ---"; 
  sha256sum "$TARGET";
} > triage_report.txt


Write-up:
1. Run the command above for initial triage
when you look for stuff in the file, like "check"s
-> check_membership (0x00401720)
This file is also statically linked and has No PIE, the memory addresses are fixed, making it very easy to navigate
-> easy for IDA!

2. Then in the Ida, we go to check_membership
then i just kinda went out the graph mode and copy-pasted that assembly into gemini

CSC{3xtr4_h0t_3spr3ss0}