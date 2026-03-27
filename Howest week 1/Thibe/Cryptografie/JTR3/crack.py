import bcrypt
import itertools
import sys

HASH = b"$2a$10$wLs6DbWb1RlkYVGwciiuvuu70Cd2jFPiOGMcc4fPcjwKSpFloMS5i"

def all_case_variants(word):
    options = []
    for c in word:
        if c.isalpha():
            options.append([c.lower(), c.upper()])
        else:
            options.append([c])
    for combo in itertools.product(*options):
        yield ''.join(combo)

def leet_variants(word):
    leet = {
        'i': ['i', '1', '!'],
        's': ['s', '5', '$'],
        'o': ['o', '0'],
        'a': ['a', '@', '4'],
        'e': ['e', '3'],
        'g': ['g', '9'],
        'u': ['u'],
    }
    options = []
    for c in word.lower():
        options.append(leet.get(c, [c]))
    for combo in itertools.product(*options):
        yield ''.join(combo)

# Build wordlist: all leet+case variants of "bingus" + "67"
candidates = set()
for leet in leet_variants("bingus"):
    for cased in all_case_variants(leet):
        candidates.add(cased + "67")

total = len(candidates)
print(f"Trying {total} candidates...\n")

for i, word in enumerate(sorted(candidates), 1):
    sys.stdout.write(f"\r[{i}/{total}] Trying: {word}   ")
    sys.stdout.flush()
    if bcrypt.checkpw(word.encode(), HASH):
        print(f"\n\n✅ CRACKED! Password: {word}")
        print(f"🚩 Flag: HCTF-FLAG-{word}")
        sys.exit(0)

print("\n\n❌ Not found in wordlist.")
