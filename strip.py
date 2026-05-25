"""
strip.py
Live cleanup: delete .jpg, .ini, and .db junk files from a music folder tree,
then remove any empty folders left behind.

Note: deletions are permanent (os.remove) — not sent to Recycle Bin.
Intended behavior for bulk strip operations.

Usage:
    py strip.py                    # targets C:\Users\Public\Music (default)
    py strip.py <root_folder>      # targets specified folder
"""

import os
import sys

# 📍 Target directory – from CLI or default to MUSICbox
music_root = sys.argv[1] if len(sys.argv) > 1 else r'C:\Users\Public\Music'

# 🧹 Extensions to actively strip (non-audio clutter)
extensions_to_strip = {'.jpg', '.ini', '.db'}

# 📋 Tracking removed files and folders
files_removed = []
folders_removed = []

print(f"\n🧨 Strip Mode: Removing unwanted files from {music_root}\n")

# 🚮 First pass – delete junk files
for dirpath, _, filenames in os.walk(music_root):
    for file in filenames:
        ext = os.path.splitext(file)[1].lower()
        if ext in extensions_to_strip:
            full_path = os.path.join(dirpath, file)
            try:
                os.remove(full_path)
                files_removed.append(full_path)
                print(f"🗑️ Deleted: {full_path}")
            except Exception as e:
                print(f"❌ Error deleting {full_path}: {e}")

# 🧽 Second pass (bottom-up) – remove empty folders
for dirpath, dirnames, filenames in os.walk(music_root, topdown=False):
    if not dirnames and not filenames:
        try:
            os.rmdir(dirpath)
            folders_removed.append(dirpath)
            print(f"🚪 Removed empty folder: {dirpath}")
        except Exception as e:
            print(f"❌ Error removing folder {dirpath}: {e}")

# 📊 Final Summary
print(f"\n✅ {len(files_removed)} file(s) successfully removed.")
print(f"🧽 {len(folders_removed)} empty folder(s) cleaned up.")
print("\n⚠️ Changes were made — this was a live strip.\n")
