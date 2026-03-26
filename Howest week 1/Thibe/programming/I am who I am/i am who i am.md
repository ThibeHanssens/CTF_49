<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
I am who I am

Category:
misc

Hints, info:
250 points


Files:
me.exe


</pre>


### Write-up:

It's a programming challenge in rust, so the usual solution methodology, is:
1. Analyse in GhidraMCP
2. Write a rust script that does the same thing as the exe, but with hardcoded values


initial reverse engineering showed:
A Windows x64 Rust binary that reads your MAC address, checks it against a hardcoded value, and if it matches, decrypts and prints the flag using `xor_cryptor`.

how to find this:

Load the binary in Ghidra. The embedded Rust source paths immediately reveal the key libraries:
- `mac_address-1.1.8` — reads the MAC
- `xor_cryptor-2.0.4` — encrypts/decrypts the flag
- `rand_chacha-0.3.1` — used internally by xor_cryptor

Then to find the check
In `main` (traced via `__scrt_common_main_seh` → `FUN_1400017c0` → `FUN_140001260`), you find:

```asm
PCMPEQB XMM0, xmmword ptr [0x14001e380]   ; compare MAC string against hardcoded value
CMP EAX, 0xffff
JZ  <flag_path>                            ; jump if all 17 bytes match
```

Reading `0x14001e380` from the binary gives: `AA:BB:CC:DD:EE:FF`


**IF YOU RUN A WINDOWS-SIMULATED ENVIRONMENT ON A LINUX OS, IT'S EASIER BECAUSE YOU CAN SPOOF YOUR OWN MAC ADDRESS**
**ON WINDOWS-BASED OS YOU HAVE TO WRITE YOUR OWN RUST CODE**
1. op windows suckt et om te spoofen, maar op een linux vm (WINE  om .exe te runnen) kan je et spoofen
2. rust script waar je de mac ingeeft als hardcoded value


Just below the check, the encrypted flag is loaded:

```asm
MOVAPS XMM0, [0x14001e3a0]    ; 16 bytes
MOVDQU [RAX], XMM0
MOVDQA XMM0, [0x14001e3b0]    ; 16 bytes
MOVDQU [RAX+0x10], XMM0
MOV    RCX, -0xff00ff00ff06ff ; last 8 bytes
MOV    [RAX+0x20], RCX
```

That gives 40 bytes of ciphertext.

The key passed to `XORCryptor::decrypt_v2` is the MAC address formatted as the string `"AA:BB:CC:DD:EE:FF"` — confirmed by the comparison at `0x14001e380` and the format routine at `FUN_1400177c0` (lowercase hex with colons).

Since the binary uses `xor_cryptor v2`, write a minimal Rust solver:

**Cargo.toml:**
```toml
[dependencies]
xor_cryptor = "2.0.4"
```

**src/main.rs:**
```rust
use xor_cryptor::XORCryptor;

fn main() {
    let key = b"AA:BB:CC:DD:EE:FF";
    let ciphertext: Vec<u8> = vec![
        0x1e,0x2b,0x03,0xa8,0x0d,0x14,0x53,0x2a,
        0x31,0x53,0x44,0x59,0x77,0x1c,0x22,0x51,
        0x60,0x71,0x16,0x72,0x12,0x6b,0x24,0xa3,
        0x63,0xb2,0x66,0xfc,0x0f,0x03,0x01,0xff,
        0x01,0xf9,0x00,0xff,0x00,0xff,0x00,0xff,
    ];
    let decrypted = XORCryptor::decrypt_v2(key, ciphertext).unwrap();
    println!("{}", String::from_utf8_lossy(&decrypted));
}
```

```
cargo run
```

---


## Key Takeaways
- Rust binaries embed full source paths — immediately reveals third-party crates used
- The MAC check and the decryption key are the same value, both hardcoded in `.rdata`
- No need to run the binary at all — everything needed (ciphertext + key + algorithm) is statically present in the binary


## Note to self
WINE

It's a programming challenge in rust, so the usual solution methodology, is:
1. Analyse in GhidraMCP
2. Write a rust script that does the same thing as the exe, but with hardcoded values