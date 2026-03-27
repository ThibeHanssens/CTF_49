import itertools

def permute_and_format(input_file, output_file):
    formatted_flags = set()

    # Exhaustive l33t-speak dictionary for the letters in "bingus"
    # Numbers in the wordlist will remain untouched
    subs = {
        'b': ['b', 'B', '8'],
        'i': ['i', 'I', '1', '!'],
        'n': ['n', 'N'],
        'g': ['g', 'G', '9'],
        'u': ['u', 'U', 'v', '5'],
        's': ['s', 'S', '$', '5', 'z']
    }

    def exhaust_word(word):
        options = []
        for char in word:
            lower_char = char.lower()
            if lower_char in subs:
                options.append(subs[lower_char])
            else:
                # Keep meme numbers and unmapped characters as they are
                options.append([char])
                
        # Generate every possible combination for this base word
        for combo in itertools.product(*options):
            yield "".join(combo)

    print("[*] Reading base wordlist...")
    with open(input_file, 'r') as f:
        base_words = set(f.read().splitlines())

    print("[*] Generating permutations and formatting flags...")
    with open(output_file, 'w') as f:
        for word in base_words:
            # Enforce the strict 8-character limit you specified
            if len(word) == 8:
                for permuted in exhaust_word(word):
                    # Crucial: Wrap the 8 chars in the full flag format
                    full_flag = f"HCTF-FLAG-{permuted}"
                    
                    if full_flag not in formatted_flags:
                        formatted_flags.add(full_flag)
                        f.write(full_flag + '\n')

    print(f"[+] Success! Wrote {len(formatted_flags)} unique formatted flags to {output_file}")

if __name__ == "__main__":
    permute_and_format("wordlist2.txt", "final_ctf_wordlist.txt")