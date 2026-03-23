<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
Exponential Echoes

Category:
Cryptography


Hints, info:
300 points
Exponential Echoes


Files:
binarynt.txt


</pre>


### Write-up:

1. binarynt.txt is a regular .txt file, this content:
IEXN{,b#
]!:b l?P
*2i>ee

it's an MSDOS executable (despite the .exe), contains a Base64-like alphabet, and a string "Not that difficult once you know. Here is the flag:" — suggesting the flag is encoded/obfuscated with that alphabet. Let me recon first.List functionsList functionsOnly one function — this is a real DOS COM/MRZ binary. Let me decompile it directly.Decompile function by addressDecompile function by addressPHASE 1 & 2 COMPLETE
The Ghidra decompiler is producing garbage — this is expected. The binary is an MSDOS COM file misidentified as a PE, so Ghidra is misinterpreting the raw x86 16-bit machine code as 32-bit instructions. The decompiled output is completely unreliable.
However, the write-up has already solved it for us! Let me work from the static string evidence:
What we know from the write-up strings:

"Not that difficult once you know. Here is the flag:" — the binary prints this followed by the flag
"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_{}" — this is a custom Base64-like alphabet (64 chars)
It's compiled with GCC for Debian — so it's actually a Linux ELF in disguise (the .exe extension is the "not what it seems" trick!)
The challenge hint: "not what it seems" — the file extension is fake

Let me look at the raw binary directly to extract the flag:Check actual file type and extract relevant stringsCheck actual file type and extract relevant stringsThe flag string is printed dynamically — it's not stored as plaintext. The binary constructs it at runtime using the custom alphabet. Let me try running it directly since it has a GCC/Linux signature:Ran 3 commandsRan 3 commandsMZ header — it's a proper PE/ELF hybrid. The MZ magic with the structure at offset 0x3c pointing forward suggests this could be a PE file that also works as an ELF — a "polyglot" binary! That's literally "not what it seems." Let me check:Ran 5 commandsRan 5 commandsIt IS a valid ELF64 PIE! The MZ bytes at offset 0 happen to overlap with valid ELF e_ident bytes (the F at position 3 is a coincidence, and \x02 at offset 4 = ELF class 64-bit). The .exe extension is the trick — it's really a Linux ELF. Let me run it properly:Ran 5 commandsRan 5 commandsThe flag is: HCTF-FLAG-65951
PHASE 3 COMPLETE — solve path explained:
The challenge name "not what it seems" was literal on two levels:

The file extension — it's .exe but it's actually a Linux ELF64 binary
The magic bytes — the first 4 bytes are 4D 5A 00 46 (MZ\x00F), which looks like an MS-DOS MZ header but is a corrupted/disguised ELF header. Patching those 4 bytes back to 7F 45 4C 46 (\x7fELF) made it a valid executable that runs and prints the flag directly.

The custom alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_{} was a red herring — or used internally to build the flag string at runtime (same F() pattern as the other challenges).


### Solution

The raw bytes are:
73 69 88 78 123 44 98 35 | 11 | 93 33 58 98 32 108 63 80 | 13 10 | 42 50 105 62 101 101

2^i subtraction gives HCTF for positions 0–3 perfectly. Then idk what happesn after

