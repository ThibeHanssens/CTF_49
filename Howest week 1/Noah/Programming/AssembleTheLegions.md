<pre>
Context:
Howest
Project week 1

Team:
The San Francisco 49ers


Challenge:
Assemble the legions

Category:
Cryptography


Hints, info:
150 points


Files:
- machine_spirit.zip
    - readme.txt
        ------------------------------------------------------------------------------------
        Make a folder called "Adeptus_Astartes"
        Create a subfolder for each legion in the Adaptus_Astartes folder and in each folder
        create a file with the name of their Primarch

        The Primarchs and their legions are the following:

        Primarch: Horus                 ====> Legion: Sons of Horus
        Primarch: Leman Russ            ====> Legion: Space Wolves
        Primarch: RECORDS REDACTED      ====> Legion: RECORDS REDACTED
        Primarch: Ferrus Manus          ====> Legion: Iron Hands
        Primarch: Fulgrim               ====> Legion: Emperor's Children
        Primarch: Vulkan                ====> Legion: Salamanders
        Primarch: Rogal Dorn            ====> Legion: Imperial Fists
        Primarch: Roboute Guilliman     ====> Legion: Ultramarines
        Primarch: Magnus the Red        ====> Legion: Thousand Sons
        Primarch: Sanguinius            ====> Legion: Blood Angels
        Primarch: Lion El Johnson       ====> Legion: Dark Angels
        Primarch: Perturabo             ====> Legion: Iron Warriors
        Primarch: Mortarion             ====> Legion: Death Guard
        Primarch: Lorgar                ====> Legion: Word Bearers
        Primarch: Jaghatai Khan         ====> Legion: White Scars
        Primarch: Konrad Curze          ====> Legion: Night Lords
        Primarch: Angron                ====> Legion: World Eaters
        Primarch: Corvus Corax          ====> Legion: Raven Guard
        Primarch: REDACTED              ====> Legion: REDACTED
        Primarch: Alpharius Omegon      ====> Legion: Alpha Legion
        ------------------------------------------------------------------------------------
    - controlicus_directus.exe


Problem description:
    - There is a an .exe files with checks if the folder and files exits and are in the correct place.

</pre>


### Write-up:
- Use python to automatically create the files and folders.
- Use the 'os' module.

### Solution
- Convert the names to python arrays.
- Loop through the arrays to create the folder and files.

```python
import os

main_folder = "Adeptus_Astartes"
primarch = ["Horus",            
        "Leman Russ",       
        "RECORDS REDACTED",
        "Ferrus Manus",     
        "Fulgrim",          
        "Vulkan",           
        "Rogal Dorn",     
        "Roboute Guilliman",
        "Magnus the Red",   
        "Sanguinius",       
        "Lion El Johnson",  
        "Perturabo",        
        "Mortarion",        
        "Lorgar",           
        "Jaghatai Khan",    
        "Konrad Curze",     
        "Angron",           
        "Corvus Corax",     
        "REDACTED",         
        "Alpharius Omegon"]

legion = ["Sons of Horus",
        "Space Wolves",
        "RECORDS REDACTED",
        "Iron Hands",
        "Emperors Children",
        "Salamanders",
        "Imperial Fists",
        "Ultramarines",
        "Thousand Sons",
        "Blood Angels",
        "Dark Angels",
        "Iron Warriors",
        "Death Guard",
        "Word Bearers",
        "White Scars",
        "Night Lords",
        "World Eaters",
        "Raven Guard",
        "REDACTED",
        "Alpha Legion"]

try:
    os.mkdir(main_folder)
except Exception:
    print(f"Folder {main_folder} could not be made.")



for i in range(0, len(legion)):
    folder_path = os.path.join(main_folder, legion[i])
    os.makedirs(folder_path, exist_ok=True)
    print(f"Nested directory '{folder_path}' has been created.")
    file_path = os.path.join(folder_path, primarch[i])
    with open(file_path, "w") as f:
        pass
    print(f"File '{file_path}' has been created.")
```
- Then run the `controlicus_directus.exe` to check if everything was created successfully.
- When all files and folders exits in the correct locations the flag will appear `HCT-FLAG-ForHumanityAndTheEmperor!`.
