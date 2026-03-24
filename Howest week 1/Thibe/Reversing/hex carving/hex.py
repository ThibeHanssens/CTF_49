import re

data = open('hexcarving.txt').read().strip().split()
raw = bytes(int(b, 16) for b in data).decode('latin-1')

for line in raw.split('\n'):
    extracted = ''.join(re.findall(r'This is byte nr \d: (.)', line))
    if extracted.strip():
        print(extracted.replace('$', '#'))