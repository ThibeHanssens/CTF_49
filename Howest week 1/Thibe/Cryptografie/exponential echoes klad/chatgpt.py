# exponential_echoes_debug.py

cipher = bytes.fromhex(
    "49 45 58 4E 7B 2C 62 23 0B 5D 21 3A 62 20 6C 3F 50 0D 0A 2A 32 69 3E 65 65"
)

target = b"HCTF-FLAG-"

SEPARATORS = {0x0B, 0x0D, 0x0A}

def decrypt(c, k):
    return (c - k) & 0xFF

def is_printable(x):
    return 32 <= x <= 126

def run(rule_name):
    print(f"\n=== Testing rule: {rule_name} ===")

    pt = []
    ks = []

    sep_state = 0   # this will track separator influence

    for i, c in enumerate(cipher):

        if c in SEPARATORS:
            print(f"[{i}] SEP {hex(c)} -> state change")
            
            # try different interpretations here
            if rule_name == "add_sep":
                sep_state = (sep_state + c) & 0xFF
            elif rule_name == "xor_sep":
                sep_state ^= c
            elif rule_name == "reset":
                sep_state = 0
            elif rule_name == "index_shift":
                sep_state += 1
            
            continue

        # base exponential
        base_k = (1 << i) & 0xFF

        # apply modification
        if rule_name == "add_sep":
            k = (base_k + sep_state) & 0xFF
        elif rule_name == "xor_sep":
            k = base_k ^ sep_state
        elif rule_name == "mul_sep":
            k = (base_k * (sep_state or 1)) & 0xFF
        elif rule_name == "index_shift":
            k = (1 << (i + sep_state)) & 0xFF
        elif rule_name == "reset":
            k = base_k
        else:
            k = base_k

        p = decrypt(c, k)

        pt.append(p)
        ks.append(k)

        char = chr(p) if is_printable(p) else "."

        print(f"[{i}] c={c:02X} k={k:02X} p={p:02X} ({char}) state={sep_state}")

        # early validation
        if len(pt) <= len(target):
            if p != target[len(pt)-1]:
                print("❌ mismatch with target")
                return

    print("✅ reached full prefix")
    print("Plain so far:", bytes(pt))


rules = [
    "add_sep",
    "xor_sep",
    "mul_sep",
    "index_shift",
    "reset",
]

for r in rules:
    run(r)