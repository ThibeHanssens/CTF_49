Platform, link:
picoCTF
https://play.picoctf.org/practice/challenge/363?page=1&search=permis

Name:
Permissions

Context:
Howest, subject CTF, assignment

Team:
solo

Hints, info:
Can you read files in the root file?
Additional details will be available after launching your challenge instance.

Write-up:
1. First ssh into the machine
2. When looking around, you'll find /challenge (root-folder)
    But, no sudo-permissions to open the file (tested with 'sudo cat challenge')
3. 'sudo -l'
    'sudo -l' shows what root-powers that you may use as an user.
        Shows this:
            User picoplayer may run the following commands on challenge:
            (ALL) /usr/bin/vi
        This basically means we can run vi as sudo/root, and do anything that's possible with vi.
4. 'sudo vi challenge'
    This uses your elevated permissions (assigned to you for vi), to open the file.
    Shows the key