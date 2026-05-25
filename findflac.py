"""
findflac.py
Recursively search a music folder tree for .flac files and print their paths.

Usage:
    py findflac.py                    # scans D:\MUSICbox (default)
    py findflac.py <root_folder>      # scans specified folder
"""

import os
import sys

music_root = sys.argv[1] if len(sys.argv) > 1 else r'D:\MUSICbox'

print(f"\n🎯 Searching for .flac files in: {music_root}\n")

flac_files = []

for dirpath, _, filenames in os.walk(music_root):
    for file in filenames:
        if file.lower().endswith('.flac'):
            full_path = os.path.join(dirpath, file)
            flac_files.append(full_path)

if flac_files:
    print(f"🎵 Found {len(flac_files)} .flac file(s):\n")
    for path in flac_files:
        print(f"  {path}")
else:
    print("🚫 No .flac files found.")

print("\n✅ Scan complete.\n")
