// Global variables shared across all crawlers
let flagFound = false;
const visited = new Set();
const targetUrl = "/subdirectories";

// Centralized parsing function to handle the 4 unpredictable formats
function extractPaths(text) {
    let paths = [];
    let cleanText = text.trim();

    if (cleanText.startsWith("nviso")) {
        paths = cleanText.split("nviso").filter(p => p.startsWith("/"));
    } else if (cleanText.startsWith("dir")) {
        paths = cleanText.split("\n").slice(1).map(p => p.trim()).filter(p => p.startsWith("/"));
    } else if (cleanText.startsWith("<")) {
        const matches = cleanText.matchAll(/name="([^"]+)"/g);
        for (const match of matches) paths.push(match[1]);
    } else if (cleanText.startsWith("{")) {
        try {
            const data = JSON.parse(cleanText);
            paths = data.dir || [];
        } catch (e) {}
    }

    // Return unique paths only
    return [...new Set(paths.map(p => p.trim()).filter(p => p))];
}

// The individual crawler logic
async function exploreBranch(startDir, crawlerId) {
    const stack = [startDir];

    // Keep digging until the stack is empty, OR another crawler finds the flag
    while (stack.length > 0 && !flagFound) {
        const currentDir = stack.pop();

        if (visited.has(currentDir)) continue;
        visited.add(currentDir);

        console.log(`[Crawler ${crawlerId}] Visiting: ${currentDir}`);

        try {
            const response = await fetch(targetUrl, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ dir: currentDir })
            });

            const text = await response.text();

            // Check if we hit a text file
            if (currentDir.endsWith(".txt")) {
                if (text.includes("CSC{")) {
                    flagFound = true; // STOP ALL OTHER CRAWLERS!
                    console.log("\n" + "=".repeat(60));
                    console.log(`[!!!] FLAG FOUND BY CRAWLER ${crawlerId} IN: ${currentDir} [!!!]`);
                    console.log(`Flag Content: ${text.trim()}`);
                    console.log("=".repeat(60) + "\n");
                    return; 
                }
                continue; // Just a dummy text file, keep going
            }

            // Extract new directories and add them to this crawler's stack
            const newPaths = extractPaths(text);
            for (let i = newPaths.length - 1; i >= 0; i--) {
                if (!visited.has(newPaths[i])) {
                    stack.push(newPaths[i]);
                }
            }

        } catch (error) {
            console.error(`[Crawler ${crawlerId}] Error accessing ${currentDir}:`, error);
        }
    }
}

// The master function that starts the attack
async function launchSwarm() {
    console.log("[*] Fetching root directory to initialize the swarm...");
    
    try {
        // 1. Get the very first set of subdirectories
        const response = await fetch(targetUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ dir: "/" })
        });
        const text = await response.text();
        const initialDirs = extractPaths(text);

        console.log(`[*] Found ${initialDirs.length} initial directories. Spawning ${initialDirs.length} crawlers...\n`);
        visited.add("/");

        // 2. Spawn a concurrent crawler for each initial directory
        // Map creates an array of Promises that run simultaneously
        const swarm = initialDirs.map((dir, index) => exploreBranch(dir, index + 1));

        // 3. Wait for all of them to finish (or stop early if the flag is found)
        await Promise.all(swarm);

        if (!flagFound) {
            console.log("[*] Swarm finished. No flag found anywhere.");
        }
    } catch (err) {
        console.error("[!] Failed to launch swarm:", err);
    }
}

// Fire the swarm!
launchSwarm();