
# Custom File System Simulator

This Python project simulates a custom file system that operates on a simulated disk file (`disk.img`).

## Features

- Simulates a block-based file system
- Basic file operations: create, read, write, delete
- Supports file permissions (r, w, x)
- Displays disk usage statistics
- Stores metadata separately (`fs_metadata.json`)

## How to Run

1. Make sure Python 3 is installed.
2. Run the script:
```bash
python fs_main.py
```

## Example Operations
- Creates a file `/file1.txt`
- Writes data to it
- Reads from it
- Deletes the file
- Displays disk usage before and after

You can extend it with more CLI options or directory support as needed.
