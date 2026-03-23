Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)


Name:
Neon Nights 

Category:
Reverse Engineering

Hints, info:
Easy
Welcome to the Neon Nights Arcade, the hottest retro gaming spot in town! The arcade's high score board has a special validation system to prevent cheaters. A friend slipped you a copy of their score validator program. Can you crack the validation code and prove you're the ultimate arcade champion?

Files:
neon_nights

Write-up:
1. First I ran 'file neon_nights' & 'checksec --file=neon_nights'
    -> ELF 64-bit executable
    + not stripped
        -> so can be used in Ghidra easily
    + debug_info
I also ran some stuff like 'strings neon_nights | grep -i "flag";'
    -> niet veel nuttige dingen
Or 'nm neon_nights | grep " T ";'
 = nm queries the symbol table of the ELF file to map memory addresses to identifiers
 = filtered with " T " searches for global symbols defined in the Code (Text) section of the binary
-> found some things like 
    main (0000000000401750)
    insert_coin (00000000004016b4)
    display_leaderboard (0000000000401685)
    validate_score (00000000004016d6)
        -> handig voor correcte input
    game_over (00000000004016c5)
No PIE (Position Independent Executable): Het programma wordt altijd op hetzelfde adres in het geheugen geladen. De adressen die je in de symbolenlijst ziet (zoals 0x4016d6 voor validate_score) zijn dus fixed. Dit maakt het debuggen met GDB veel eenvoudiger.

For later re-use:

{
  echo "--- FILE INFO ---"; file neon_nights;
  echo -e "\n--- CHECKSEC ---"; checksec --file=neon_nights;
  echo -e "\n--- STRINGS (FLAG) ---"; strings neon_nights | grep -i "flag";
  echo -e "\n--- SYMBOLS (FUNCTIONS) ---"; nm neon_nights | grep " T ";
} > file_analysis.txt


2. Then throw it into Ghidra/IDA

You see this:
- call validate_score: The program runs your input through this function.
- test eax, eax: It checks the return value of that function. In assembly, eax usually holds the result.
- jz short loc_4017F9: This is a Jump if Zero.
- If validate_score returns 0, it jumps to the "INVALID CODE" block (red arrow).
    If validate_score returns anything else (not zero),
    it continues to the "SCORE VALIDATED!" block (green arrow).
-> Double-click on the word validate_score in that middle block. IDA will jump you inside that function.
    Goal: Find out what mathematical operations or comparisons it is doing to make it return something other than zero.


Look closely at these specific lines in the first block of `validate_score`:

1. **`mov [rbp+var_8], 18h`**: This sets a local variable (`var_8`) to the hex value **`18h`**.
* **$18$ in hex is $24$ in decimal.**


2. **`call j_strlen`**: The program measures the length of the string you typed in.
3. **`cmp rdx, rax`**: It compares the length of your input (`rax`) with that value of $24$ (`rdx`).
4. **`jz short loc_401707`**: This is the critical branch.
* **Green Arrow (Fail):** If the length is **NOT** $24$, it jumps to `loc_401707`, which sets a "fail" flag (`mov [rbp+var_4], 0`) and exits.
* **Red Arrow (Success):** If the length **IS exactly $24$ characters**, it continues downward (following the red arrow) to the next check.

Then if we keep following that
to the right
The Loop Index: rbp+var_4 is the counter (starting at 0 and going up to 24).
Your Character: It grabs the next character from your input (movzx eax, byte ptr [rax]).
The Secret Data: It grabs a byte from a stored array called secret_data.
The Key: It grabs a byte from another variable called xor_key.
The Math: It performs secret_data[i] ^ xor_key.
The Comparison: cmp cl, al. It checks if Your Character matches the result of that XOR math.
    If it matches (jz): It goes to loc_40173D, adds 1 to the counter, and checks the next character.
    If it fails: It exits and returns 0 (Invalid).


Double-click on the name secret_data in the assembly. It will take you to the data section. Copy those 24 hex bytes.

Double-click on xor_key. Note that hex value.

xor_key: De waarde is 42h (in decimal is dit 66).

secret_data: Een lijst van exact 24 bytes (wat overeenkomt met de lengte-check die we eerder zagen).





CSC{n30n_l1t_h1gh_sc0r3}





write-up incomplete


First


To run the file in linux:
chmod +x neon_nights
    -> make it executable
./neon_nights