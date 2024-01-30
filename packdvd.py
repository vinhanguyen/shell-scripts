import os
import sys
from pathlib import Path
import subprocess

if len(sys.argv) < 3:
    raise Exception('Usage: python packdvd.py dir ext [ext]')

_, dir, *ext = sys.argv

free_space = 4700000000
files = []

for f in sorted([f for f in os.scandir(dir) if Path(f.path).suffix[1:] in ext], key=lambda f: f.name):
    size = f.stat().st_size
    if (size < free_space):
        files.append(f.path)
        free_space -= size

subprocess.run(['brasero', '-d', *files])
