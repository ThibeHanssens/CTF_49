Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
vault

Category:
reverse engineering


Hints, info:
vault.exe


Files:
vault.exe
```

### Write-up:

1. Open in Ghidra. Embedded Rust crate paths in `.rdata` immediately reveal the crypto library: `xor_cryptor-2.0.4` and `rand_chacha-0.3.1`

2. Decompile main (`FUN_140001100`). The logic is:
    - Prints welcome banner and password prompt
    - Reads user input from stdin
    - Encrypts the hardcoded string `"xxd -d out.txt"` using a 56-byte key blob from `.rdata` (`0x14001f380`) with xor_cryptor v2
    - Compares user input against that ciphertext
    - On match: encrypts `"password"` with a second 48-byte key blob (`0x14001f3b0`) and prints the result as the flag
    - If user typed literally `"password"`: prints `"Nice try!"`

3. The xor_cryptor v2 cipher seeds its internal ChaCha20 PRNG with `SystemTime::now()` in milliseconds, so the ciphertext changes every run. The flag cannot be precomputed — it must be captured at runtime.

4. Open `vault.exe` in x64dbg. Press F9 twice to pass the system breakpoint and TLS callback. Set a breakpoint at `vault+1380` (the `CMP` that checks input length against ciphertext length, just before `memcmp`).

5. Type `aaaaaa` in the console and press Enter. The breakpoint fires. At this point the binary has already computed `encrypt("xxd -d out.txt", key1)` and has the ciphertext live in memory. RIP is sitting at the comparison.

6. In the registers panel, double-click **RIP** and change it to `7FF784251478` (module base + `0x1478`) — the start of the flag computation path — skipping the `memcmp` result check entirely.

7. The flag encrypt (`encrypt("password", key2)`) runs. When RIP reaches `vault+1533` (a `JNO` that branches to an error path if the encrypt Result is Err), redirect RIP to `vault+1539` to skip the error branch and force the success path.

8. The flag is visible in the registers panel and memory dump before it even prints:
```
HCTF-FLAG-WatchZeztzNowItGood