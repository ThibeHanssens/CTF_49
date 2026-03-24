import itertools, string
from math import gcd

cipher = [73,69,88,78,123,44,98,35,93,33,58,98,32,108,63,80,42,50,105,62,101,101]
prefix = b"HCTF-FLAG-"
charset = (string.ascii_letters + string.digits).encode()

def log(msg):
    print(msg, flush=True)

log("=== Exponential Echoes Solver (fast) ===")

suffix_len = len(cipher) - len(prefix)  # 12

for length in range(1, suffix_len + 1):
    log(f"--- Testing suffix length {length} ---")
    for combo in itertools.product(charset, repeat=length):
        suffix = bytes(combo)
        pt = prefix + suffix
        n = len(pt)
        keys = [(cipher[i] - pt[i]) % 256 for i in range(n)]

        # Compute N directly via GCD
        g = 0
        for i in range(n):
            diff = (1 << i) - keys[i]
            if diff > 0:
                g = gcd(g, diff)

        if g > 1:
            if all(pow(2, i, g) == keys[i] for i in range(n)):
                flag = pt.decode()
                log(f"*** FLAG FOUND N={g}: {flag}")

log("=== Done ===")
