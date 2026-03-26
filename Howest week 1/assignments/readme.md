# The Kakophoni

## Description
> *A spoken lock requires a spoken heresy. Only the true chorus can read these sigils.*
> Flag format is: HCTF-FLAG-

### Check flag:
 SHA-256 hash with 64 rounds: a440f7e1ed3bcada519c49d637a2ab288d87b99901ca5343f2f34db3e026f6d2

## Attachments
* `3 images, or are they...`

---
<!--Hints are provided in base64 to keep them a bit hidden-->
### Hint 1
`VGhlIElucXVpc2l0aW9uIHNlYWxzIHRoZWlyIHNlY3JldHMgZGVlcCBiZW5lYXRoIHRoZSBzdXJmYWNlLiBPbmx5IGJ5IGludm9raW5nIHRoZSBzbGF0ZSdzIG91dHdhcmQgbWFyayBjYW4gdGhlIGlubmVyIHNjcmlwdCBiZSByZWFkLg==`

### Hint 2
`RXZlcnkgYXJ0aWZhY3QgY2FycmllcyB0aGUgbWVtb3JpZXMgb2YgaXRzIGZvcmdpbmcu`

### Hint 3
`TXkgZmF2b3JpdGUgY29tbWFuZHMgYXJlIHN0ZWdoaWRlIGFuZCBleGlmdG9vbA==`


## Write-up

### Phase 1
<h4 style="margin-top:-1em;">Voice cloning & audio preparation</h4>

* **Voice cloning:** To add a personal touch, I cloned "Shan's" voice using [Ultimate RVC](https://github.com/JackismyShephard/ultimate-rvc). 
* **Script generation:** I generated a list of 187 random words and letters and organized them into a spreadsheet. To hide the payload, I replaced specific letters within this dataset to spell out the final flag.
* **Recording:** I went into a quiet room and clearly articulated the 187 words and letters. I took my time, because speaking slowly and clearly was crucial so the AI voice model could accurately replicate the audio.
* **Audio synchronization:** I imported both the word and letter recordings into Adobe Audition, and synced the tracks so the letters lined up with their corresponding words. 
* **AI processing:** Finally, I ran these synchronized recordings through the trained RVC model to generate the "Shan" voice lines.

### Phase 2
<h4 style="margin-top:-1em;">Obfuscation & encoding</h4>

* **Audio to image:** Because raw audio files are a bit too straightforward, I added an extra layer of complexity. I used a [web converter tool](https://p2r3.github.io/convert/) to translate the audio files into image formats.
* **Breadcrumb trail (EXIF-data):** To ensure players weren't entirely in the dark about how to revert the images back to audio, I left a hint. Using [ExifTool](https://exiftool.org/), I embedded the URL of the conversion tool into the image's comment metadata.
* **Encoding the hint:** To prevent the hint from being too obvious, I encoded the URL using a three-step process: **ROT13 -> Hex -> Base64**.

### Phase 3:
<h4 style="margin-top:-1em;">Steganography & final touches</h4>

* **Keylist:** I created a text file called "keylist", which contained the exact words players needed to find in one audio file to link to the letters in the other.
* **Steganography:** To hide this keylist, I used `steghide` to embed the text file inside an extra image (a Warhammer "dataslate," fitting the challenge's theme).
* **The passphrase:** The passphrase required to extract the keylist via steghide is `OBJ-PRIME`. As a clue, this exact phrase is visually integrated into the design of the dataslate image itself.

## Solution Walkthrough: The Kakophoni

**Summary:** Players are given three image files. They must use steganography, metadata analysis, multi-layered decryption, and audio manipulation to extract the hidden flag.

### Step 1: Extracting the keylist (steganography)

1.  **Analyze the images:** The challenge provides three images, including a Warhammer 40k-themed "dataslate." 
2.  **Clue:** Inspecting the dataslate image reveals the text `OBJ-PRIME` clearly visible in the design.
3.  **Steghide extraction:** Knowing the challenge mentions "inner scripts" (or using Hint 1/3), players use `steghide` on the dataslate image. When prompted for a passphrase, entering `OBJ-PRIME` extracts a hidden text file: `keylist.txt`. 
4.  **Review keylist:** Opening `keylist.txt` reveals a specific list of words: it is the map to the flag.

### Step 2: Finding the converter (metadata & decoding)
1.  **EXIF-data:** Checking the metadata of the images using `exiftool` (as nudged by hint 2/3) reveals a strange string hidden in the comments section.
2.  **Decoding the breadcrumb:** The string is heavily encoded. Players must process the data through a multi-stage decoding chain to reveal the final destination
    * Decode from **Base64** -> yields a Hex string.
    * Decode from **Hex** -> yields a ROT13 string.
    * Decode from **ROT13** -> reveals a URL: `https://p2r3.github.io/convert/`
3.  **Image to audio:** The remaining two " images" aren't actually images at all. Uploading them to the discovered web tool converts them back into their true form: two audio files. One contains spoken words, the other contains spoken letters.

### Step 3: The spoken heresy (audio editing)
1.  **Audio workspace:** Import both the "Words" audio file and the "Letters" audio file into an audio editing program like Audacity or Adobe Audition. Place them on parallel tracks.
2.  **Cross-referencing:** Open the keylist extracted in Step 1. 
3.  **Splicing the flag:** Listen to the "Words" track and find the exact timestamps where the words from the keylist are spoken.
    * Drop down to the exact same timestamps on the "Letters" track. 
    * Cut or isolate the letters spoken at those specific moments. 
4.  **The reveal:** By cutting out and stringing together only the letters that align with the keylist words, players spell out the final flag. By stringing together the letters that align with the keylist words, players spell out the final flag: "HCTF-FLAG-SHAN_L0V3S_C5HARP"