(async function findTheFlag() {
    const sleep = (ms) => new Promise(res => setTimeout(res, ms));
    const exhausted = new Set(); // Folders where we've seen everything inside
    const visited = new Set();   // Folders we are currently exploring
    
    async function getPath() {
        const el = document.getElementById('current-dir');
        // Clean the text to get just the path
        return el ? el.innerText.replace("Current directory: ", "").split('\n')[0].trim() : "/";
    }

    async function solve() {
        while (true) {
            const currentPath = await getPath();
            const statusText = document.getElementById('current-dir').innerText;

            console.log(currentPathn, statusText)
            // 1. Check for the Flag
            if (currentPath.includes('.') && !statusText.includes("not the flag")) {
                console.log("%c >>> FLAG FOUND! <<<", "color: lime; font-size: 25px; font-weight: bold;");
                console.log("Path:", currentPath);
                return;
            }

            // 2. Find clickable children
            const dirs = Array.from(document.querySelectorAll('#dir-list li.dir'));
            let clickedSomething = false;

            for (let dir of dirs) {
                const targetPath = dir.getAttribute('data-name');
                
                // Only click if we haven't exhausted this path already
                if (!exhausted.has(targetPath)) {
                    dir.querySelector('a').click();
                    await sleep(200); // Give it time to load the POST request
                    clickedSomething = true;
                    break; 
                }
            }

            // 3. Backtracking Logic
            if (!clickedSomething) {
                // If we are here, we've clicked everything in this folder.
                // Mark this specific directory as exhausted.
                exhausted.add(currentPath);
                
                const parentBtn = document.getElementById('to-parent-btn');
                if (currentPath === "/" || !parentBtn || parentBtn.disabled) {
                    console.log("Search complete. No more paths to explore.");
                    break;
                }

                console.log("Exhausted", currentPath, "--- Returning to Parent");
                parentBtn.click();
                await sleep(200);
            }
        }
    }

    console.log("Starting Robust Search...");
    await solve();
})();