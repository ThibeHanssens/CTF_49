# exponential_echoes_stage2_solver.py

cipher = bytes.fromhex(
    "49 45 58 4E 7B 2C 62 23 0B 5D 21 3A 62 20 6C 3F 50 0D 0A 2A 32 69 3E 65 65"
)

# remove separators for now (we can reintroduce later if needed)
data = bytes(b for b in cipher if b not in (0x0B, 0x0D, 0x0A))

# we ONLY care about reaching this
target = b"HCTF-FLAG-"

# ---------- helpers ----------

def bitrev8(x):
    y = 0
    for _ in range(8):
        y = (y << 1) | (x & 1)
        x >>= 1
    return y

def pow2(x):
    return (1 << (x & 7)) & 0xFF

def decrypt_byte(c, k, mode):
    if mode == "sub":
        return (c - k) & 0xFF
    elif mode == "xor":
        return c ^ k
    elif mode == "add":
        return (c + k) & 0xFF
    else:
        raise ValueError("invalid mode")

def key_from_state(pt, ct, ks, i, rule):
    prev_p = pt[-1] if pt else 0
    prev_c = ct[-1] if ct else 0
    prev_k = ks[-1] if ks else 0

    if rule == "2pow_i":
        return (1 << i) & 0xFF

    if rule == "2pow_i_xor_prevp":
        return ((1 << i) ^ prev_p) & 0xFF

    if rule == "2pow_i_plus_prevp":
        return ((1 << i) + prev_p) & 0xFF

    if rule == "2pow_i_xor_prevc":
        return ((1 << i) ^ prev_c) & 0xFF

    if rule == "2pow_i_plus_prevc":
        return ((1 << i) + prev_c) & 0xFF

    if rule == "prevp":
        return prev_p

    if rule == "prevc":
        return prev_c

    if rule == "prevk":
        return prev_k

    if rule == "2prevk":
        return (2 * prev_k) & 0xFF

    if rule == "2prevk_xor_prevp":
        return ((2 * prev_k) ^ prev_p) & 0xFF

    if rule == "2prevk_plus_prevp":
        return ((2 * prev_k) + prev_p) & 0xFF

    if rule == "2prevk_xor_prevc":
        return ((2 * prev_k) ^ prev_c) & 0xFF

    if rule == "2prevk_plus_prevc":
        return ((2 * prev_k) + prev_c) & 0xFF

    if rule == "pow2_prevp":
        return pow2(prev_p)

    if rule == "pow2_prevc":
        return pow2(prev_c)

    if rule == "pow2_prevk":
        return pow2(prev_k)

    if rule == "rev_prevp":
        return bitrev8(prev_p)

    if rule == "rev_prevc":
        return bitrev8(prev_c)

    if rule == "rev_prevk":
        return bitrev8(prev_k)

    raise ValueError("unknown rule")

# ---------- rule space ----------

rules = [
    "2pow_i",
    "2pow_i_xor_prevp",
    "2pow_i_plus_prevp",
    "2pow_i_xor_prevc",
    "2pow_i_plus_prevc",
    "prevp",
    "prevc",
    "prevk",
    "2prevk",
    "2prevk_xor_prevp",
    "2prevk_plus_prevp",
    "2prevk_xor_prevc",
    "2prevk_plus_prevc",
    "pow2_prevp",
    "pow2_prevc",
    "pow2_prevk",
    "rev_prevp",
    "rev_prevc",
    "rev_prevk",
]

modes = ["sub", "xor", "add"]

# ---------- stage 1 (locked) ----------

pt_seed = list(b"HCTF")
ct_seed = list(data[:4])
ks_seed = [((data[i] - pt_seed[i]) & 0xFF) for i in range(4)]

# ---------- search stage 2 ----------

found = False

for rule in rules:
    for mode in modes:

        pt = pt_seed[:]
        ct = ct_seed[:]
        ks = ks_seed[:]

        ok = True

        for i in range(4, len(target)):
            k = key_from_state(pt, ct, ks, i, rule)
            p = decrypt_byte(data[i], k, mode)

            pt.append(p)
            ct.append(data[i])
            ks.append(k)

            if p != target[i]:
                ok = False
                break

        if ok:
            found = True
            print("=== STAGE 2 MATCH ===")
            print("Rule :", rule)
            print("Mode :", mode)
            print("Plain:", bytes(pt))

if not found:
    print("No valid Stage 2 rule found. Next step: include separators in state.")