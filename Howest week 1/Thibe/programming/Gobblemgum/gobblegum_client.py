#!/usr/bin/env python3
"""
Gobblegum CTF client — interacts with gobblegum.exe over 127.0.0.1:34254

From reversing FUN_140006150 (main loop):
  - Server prints a banner: "I am Alpharius Omegon, Primarch of the Alpha Legion..."
  - Server prints: "Pick an option:"
  - Server prints 4 menu items (options 1-4)
  - Option 4 dispatches to FUN_140006070 → FUN_1400064e0 → decrypts + prints flag

Usage:
  1. Run gobblegum.exe on your Windows machine first
  2. Then run this script: python gobblegum_client.py
"""

import socket
import time
import sys

HOST = "127.0.0.1"
PORT = 34254

def recvall_until_prompt(sock, timeout=3.0):
    """Read from socket until data stops arriving (menu prompt)."""
    sock.settimeout(timeout)
    data = b""
    try:
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
            # Stop reading once we see the prompt ending
            if b"Pick an option" in data or b"option" in data.lower():
                # Give a short window for the rest of the menu to arrive
                sock.settimeout(0.5)
    except socket.timeout:
        pass
    return data

def send_line(sock, text):
    """Send a line terminated with newline."""
    msg = (text + "\n").encode()
    sock.sendall(msg)

def main():
    print(f"[*] Connecting to {HOST}:{PORT} ...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("[!] Connection refused.")
        print("    Make sure gobblegum.exe is running on your Windows machine first!")
        sys.exit(1)

    print("[+] Connected!\n")

    # Step 1: Read the banner + menu
    banner = recvall_until_prompt(s, timeout=3.0)
    print("[SERVER]:\n" + banner.decode(errors="replace"))

    # Step 2: Try all 4 options, starting with 4 (most likely to give the flag
    #         based on reversing: option 4 → FUN_140006070 → FUN_1400064e0 → flag)
    for option in ["4", "1", "2", "3"]:
        print(f"\n[*] Sending option: {option}")
        send_line(s, option)
        time.sleep(0.5)

        response = recvall_until_prompt(s, timeout=4.0)
        decoded = response.decode(errors="replace")
        print(f"[SERVER]: {decoded}")

        # Check if we got the flag
        if "HCTF" in decoded or "FLAG" in decoded or "flag" in decoded.lower():
            print("\n[!!!] FLAG FOUND:", decoded)
            break

        # If the server re-prompts, keep going
        if "Pick an option" not in decoded and "option" not in decoded.lower():
            print("[*] Server closed or changed state, trying fresh connection for next option.")
            s.close()
            time.sleep(0.3)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
                banner = recvall_until_prompt(s, timeout=2.0)
            except Exception as e:
                print(f"[!] Could not reconnect: {e}")
                break

    s.close()
    print("\n[*] Done.")

if __name__ == "__main__":
    main()
