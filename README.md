# MusicOrg

Python utilities for scanning, cleaning, and organizing a local music archive.

## Scripts

### mboxcnt.py
Scans a music folder tree and prints a summary: subfolder count, total file count, empty folders, and a full breakdown of file extensions.

```
py mboxcnt.py                        # scans C:\Users\Public\Music (default)
py mboxcnt.py <root_folder>
```

### drystrip.py
Dry-run preview — reports `.jpg`, `.ini`, and `.db` junk files and empty folders that *would* be removed, without touching anything.

```
py drystrip.py                       # scans C:\Users\Public\Music (default)
py drystrip.py <root_folder>
```

### strip.py
Live cleanup — deletes `.jpg`, `.ini`, and `.db` junk files, then removes any empty folders left behind.

> **Warning:** deletions are permanent (`os.remove`) — files are not sent to the Recycle Bin. Run `drystrip.py` first to preview.

```
py strip.py                          # targets C:\Users\Public\Music (default)
py strip.py <root_folder>
```

### findflac.py
Recursively searches a folder tree for `.flac` files and prints their full paths.

```
py findflac.py                       # scans D:\MUSICbox (default)
py findflac.py <root_folder>
```

## Requirements

Python 3.x, stdlib only (`os`, `sys`, `collections`)

## License

MIT — Copyright Drew Adkins | Unsung Images
