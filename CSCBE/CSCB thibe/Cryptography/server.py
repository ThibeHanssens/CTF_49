#!/usr/bin/env python3
"""
Time Capsule — Crypto Challenge Server

Encrypts the flag using Python's random module seeded with the current
UNIX timestamp, then sends the ciphertext to the client.
"""

import os
import random
import socketserver
import time

HOST = "0.0.0.0"
PORT = 1339
FLAG = os.environ.get("FLAG", "CSC{REDACTED}")

BANNER = r"""
  ╔══════════════════════════════════════════╗
  ║     ⏳  TIME CAPSULE ENCRYPTION  ⏳      ║
  ║  "Sealed with a unique, unbreakable key" ║
  ╚══════════════════════════════════════════╝
"""


def encrypt(plaintext: bytes, seed: int) -> bytes:
    """Encrypt plaintext by XORing with a PRNG keystream seeded with `seed`."""
    rng = random.Random(seed)
    keystream = bytes([rng.randint(0, 255) for _ in range(len(plaintext))])
    return bytes(a ^ b for a, b in zip(plaintext, keystream))


class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        timestamp = int(time.time())
        ciphertext = encrypt(FLAG.encode(), timestamp)

        self.wfile.write(BANNER.encode())
        self.wfile.write(b"\n")
        self.wfile.write(f"Sealed message (hex) : {ciphertext.hex()}\n".encode())
        self.wfile.write(b"\nGood luck unsealing it!\n")


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with ThreadedTCPServer((HOST, PORT), Handler) as server:
        print(f"Time Capsule listening on {HOST}:{PORT}")
        server.serve_forever()
