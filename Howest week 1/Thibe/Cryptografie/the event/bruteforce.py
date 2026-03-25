#!/usr/bin/env python3
"""
XXTEA brute-force — Howest CTF "The event"
Cipher : xtWslCa1iwvxhojyfU4qCs/nCOsjXeQIEv5LJabStvg62BbK
Prefix : HCTFFLAG (first 8 bytes of plaintext)

Usage:
  python solve.py --wordlist /path/to/rockyou.txt
  python solve.py --brute
  python solve.py --wordlist /path/to/rockyou.txt --brute
  python solve.py --brute-only --max-len 7
"""

import base64, struct, itertools, string, sys, argparse

# ── XXTEA ─────────────────────────────────────────────────────────────────────
DELTA = 0x9e3779b9

def xxtea_decrypt_words(data, key4):
    data = data[:]
    n = len(data)
    q = 6 + 52 // n
    s = (q * DELTA) & 0xFFFFFFFF
    y = data[n - 1]
    while s:
        e = (s >> 2) & 3
        for p in range(n - 1, -1, -1):
            z = data[p - 1] if p > 0 else data[n - 1]
            mx = (
                (((z >> 5) ^ (y << 2)) + ((y >> 3) ^ (z << 4)))
                ^ ((s ^ y) + (key4[(p & 3) ^ e] ^ z))
            ) & 0xFFFFFFFF
            data[p] = (data[p] - mx) & 0xFFFFFFFF
            y = data[p]
        s = (s - DELTA) & 0xFFFFFFFF
    return data

# ── Setup ──────────────────────────────────────────────────────────────────────
CT = list(struct.unpack('<9I', base64.b64decode("xtWslCa1iwvxhojyfU4qCs/nCOsjXeQIEv5LJabStvg62BbK")))

# Known prefix: first 8 bytes = "HCTFFLAG"
W0 = struct.unpack('<I', b'HCTF')[0]  # word[0] must equal this
W1 = struct.unpack('<I', b'FLAG')[0]  # word[1] must equal this

def try_key(key_bytes):
    """Pad/truncate key_bytes to 16 bytes, decrypt, check prefix."""
    kb = (key_bytes + b'\x00' * 16)[:16]
    key4 = list(struct.unpack('<4I', kb))
    pt = xxtea_decrypt_words(CT, key4)
    if pt[0] == W0 and pt[1] == W1:
        return struct.pack('<9I', *pt)
    return None

def report(key_bytes, plaintext):
    print(f"\n{'='*60}")
    print(f"[FLAG FOUND]")
    print(f"  Key (raw) : {key_bytes}")
    try:
        print(f"  Key (str) : {key_bytes.decode(errors='replace')}")
    except:
        pass
    print(f"  Plaintext : {plaintext}")
    try:
        print(f"  Decoded   : {plaintext.decode(errors='replace')}")
    except:
        pass
    print(f"{'='*60}\n")
    sys.exit(0)

# ── Phase 1: Wordlist ──────────────────────────────────────────────────────────
def run_wordlist(path):
    print(f"[Phase 1] Wordlist attack: {path}")
    count = 0
    try:
        with open(path, 'rb') as f:
            for line in f:
                word = line.rstrip(b'\r\n')
                if not word:
                    continue
                count += 1
                if count % 500_000 == 0:
                    print(f"  ... {count:,} words tested (last: {word[:30]})")

                for variant in (word, word.lower(), word.upper()):
                    result = try_key(variant)
                    if result:
                        report(variant, result)

    except FileNotFoundError:
        print(f"  [!] Wordlist not found: {path}")
        return
    print(f"  [Phase 1 done] {count:,} words tested — no match.")

# ── Phase 2: Brute-force ───────────────────────────────────────────────────────
def run_brute(max_len=6):
    # Phase 2a: lowercase + digits (36 chars) — feasible up to len 6
    charset = string.ascii_lowercase + string.digits
    print(f"[Phase 2a] Brute-force: charset=[a-z0-9] lengths 1..{max_len}")
    for length in range(1, max_len + 1):
        total = len(charset) ** length
        print(f"  Testing length {length} ({total:,} combinations)...")
        count = 0
        for combo in itertools.product(charset, repeat=length):
            key_bytes = ''.join(combo).encode()
            count += 1
            if count % 5_000_000 == 0:
                pct = 100 * count // total
                print(f"    ... {count:,}/{total:,} ({pct}%)")
            result = try_key(key_bytes)
            if result:
                report(key_bytes, result)
        print(f"  Length {length} done — no match.")

    # Phase 2b: mixed-case + digits (62 chars) — feasible up to len 5
    charset2 = string.ascii_letters + string.digits
    print(f"[Phase 2b] Brute-force: charset=[a-zA-Z0-9] lengths 1..5")
    for length in range(1, 6):
        total = len(charset2) ** length
        print(f"  Testing length {length} ({total:,} combinations)...")
        count = 0
        for combo in itertools.product(charset2, repeat=length):
            key_bytes = ''.join(combo).encode()
            count += 1
            if count % 5_000_000 == 0:
                pct = 100 * count // total
                print(f"    ... {count:,}/{total:,} ({pct}%)")
            result = try_key(key_bytes)
            if result:
                report(key_bytes, result)
        print(f"  Length {length} done — no match.")

# ── Main ───────────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser()
parser.add_argument('--wordlist', help='Path to wordlist (e.g. rockyou.txt)')
parser.add_argument('--brute', action='store_true', help='Run brute-force after wordlist')
parser.add_argument('--max-len', type=int, default=6, help='Max brute-force key length (default 6)')
parser.add_argument('--brute-only', action='store_true', help='Skip wordlist, only brute-force')
args = parser.parse_args()

print(f"[*] CT words : {[hex(w) for w in CT]}")
print(f"[*] Target   : word[0]={hex(W0)} word[1]={hex(W1)}  (= 'HCTFFLAG')")
print()

if not args.brute_only and args.wordlist:
    run_wordlist(args.wordlist)

if args.brute or args.brute_only:
    run_brute(args.max_len)

if not args.wordlist and not args.brute and not args.brute_only:
    print("No mode selected. Examples:")
    print("  python solve.py --wordlist rockyou.txt")
    print("  python solve.py --brute")
    print("  python solve.py --wordlist rockyou.txt --brute")
    print("  python solve.py --brute-only --max-len 7")
