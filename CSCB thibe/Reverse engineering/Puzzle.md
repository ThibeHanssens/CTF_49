Context:
CSCBE competition, 2026

Team:
Thibe Hanssens (solo)


Name:
Puzzle

Category:
Reverse Engineering

Hints, info:
Hard
Push all the boxes onto a goal. Simple enough, ...right?

2 files:
puzzle
dockerfile

Pre-requisities:
Update your package list
    sudo apt update
Install Docker
    sudo apt install -y docker.io
Start the Docker service
    sudo systemctl start docker

Write-up:
1. I first threw puzzle into DIE to analyze what it was
    -> ELF file, so from now i'm working on linux

2. Open linux
    -> sudo docker build -t cscbe-puzzle .
    -> sudo docker run -it cscbe-puzzle /bin/bash

3. Run file
chmod +x puzzle
./puzzle

4. we see this puzzle-like thing that's impossible to solve
-> so we probably need ghidra/ida to modify it
sudo apt update
sudo apt install -y ghidra
ghidra

5. Working with Ghidra
Once Ghidra is open, here is your tactical plan to find the flag:

A. Initial Analysis
    Create a New Project: File -> New Project -> Non-Shared -> [Name it CSCBE].
    Import the File: Press I and select the puzzle ELF file.
    Analyze: Double-click the file to open the "CodeBrowser." When it asks if you want to analyze it, click Yes. Keep the default options and hit Analyze.

B. Hunting the Logic
Since this is a puzzle game, look at the Symbol Tree on the left. Expand Functions and search for these "Golden" terms:
    main: Always start here to see how the game loop works.
    check_win or is_solved: This is where the magic happens.
    load_map: This tells you where the grid data is stored.
    move_player: This shows you how inputs (WASD) affect memory.

C. Finding the "Win" Check
In the Decompiler window (usually on the right), look for a function that checks if all boxes are on goals.
    The Trap: In "Hard" challenges, simply "winning" the game in the UI might not give the flag. The flag might be decrypted based on the sequence of moves you made.
    The Cheat: If the flag is just printed when a certain variable becomes 1, you can use Ghidra to find the address of that check and use GDB (GNU Debugger) to manually change that variable in memory to "force" a win.

6. Then i looked into AIs, since the competitors seemed to be using them a lot 
I found Claude Opus 4.6 very very helpful
GhidraMCP


Setting It Up (Quick Guide)
Prerequisites:

Java JDK 21+
Ghidra (v11.x recommended)
    https://github.com/NationalSecurityAgency/ghidra/releases
GhidraMCP
    https://github.com/LaurieWired/GhidraMCP/releases
Python 3 + pip install mcp requests
Claude Desktop (or another MCP-compatible client)

Steps:

Download the latest GhidraMCP release
In Ghidra: File → Install Extensions → select the .zip → restart Ghidra
Open your CTF binary in Ghidra and run auto-analysis
In Claude Desktop, go to Settings → Developer → Edit Config → claude_desktop_config.json and add:

json{
  "mcpServers": {
    "ghidra": {
      "command": "python",
      "args": [
        "/ABSOLUTE_PATH_TO/bridge_mcp_ghidra.py",
        "--ghidra-server",
        "http://127.0.0.1:8080/"
      ]
    }
  }
}
GitHub

5. Restart Claude Desktop — you'll now have Ghidra tools available in your chat

6. 
 Laad de binary in Ghidra

Open Ghidra
File → Import File → selecteer het puzzle bestand
Klik Yes → Analyze en wacht tot de analyse klaar is
Zodra Ghidra klaar is met analyseren, kan je via de MCP tools oplossen

