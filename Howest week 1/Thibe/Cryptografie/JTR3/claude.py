import bcrypt
import itertools
import sys

HASH = b"$2a$10$wLs6DbWb1RlkYVGwciiuvuu70Cd2jFPiOGMcc4fPcjwKSpFloMS5i"

def leet_and_case(word):
    leet = {
        'b': ['b', '6'],
        'i': ['i', '1', '!'],
        's': ['s', '5', '$'],
        'g': ['g', '9'],
        'u': ['u'],
        'n': ['n'],
    }
    options = []
    for c in word.lower():
        opts = leet.get(c, [c])
        expanded = set()
        for o in opts:
            if o.isalpha():
                expanded.add(o.lower())
                expanded.add(o.upper())
            else:
                expanded.add(o)
        options.append(sorted(expanded))
    for combo in itertools.product(*options):
        yield ''.join(combo)

candidates = sorted(set("HCTF-FLAG-" + v + "67" for v in leet_and_case("bingus")))
total = len(candidates)
print(f"Trying {total} candidates...\n")

for i, word in enumerate(candidates, 1):
    sys.stdout.write(f"\r[{i}/{total}] Trying: {word}   ")
    sys.stdout.flush()
    if bcrypt.checkpw(word.encode(), HASH):
        print(f"\n\n✅ CRACKED!")
        print(f"🚩 Flag: {word}")
        sys.exit(0)

print("\n\n❌ Niet gevonden.")
