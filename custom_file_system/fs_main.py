import os
import json
from datetime import datetime

BLOCK_SIZE = 512
TOTAL_BLOCKS = 1024
DISK_FILE = "disk.img"

class FileSystem:
    def __init__(self):
        if not os.path.exists(DISK_FILE):
            self.format_disk()
        else:
            self.load_fs()

    def format_disk(self):
        self.disk = bytearray(BLOCK_SIZE * TOTAL_BLOCKS)
        self.fs = {
            "superblock": {
                "total_blocks": TOTAL_BLOCKS,
                "used_blocks": 0
            },
            "files": {},
            "free_blocks": list(range(1, TOTAL_BLOCKS))  # reserve block 0 for metadata
        }
        self.save_fs()
        with open(DISK_FILE, "wb") as f:
            f.write(self.disk)
        print("Disk formatted.")

    def save_fs(self):
        with open("fs_metadata.json", "w") as f:
            json.dump(self.fs, f, indent=2)

    def load_fs(self):
        with open("fs_metadata.json", "r") as f:
            self.fs = json.load(f)
        with open(DISK_FILE, "rb") as f:
            self.disk = bytearray(f.read())

    def create_file(self, path, permission="rwx"):
        if path in self.fs["files"]:
            print("File already exists.")
            return
        self.fs["files"][path] = {
            "size": 0,
            "permissions": permission,
            "blocks": [],
            "created": datetime.now().isoformat()
        }
        self.save_fs()
        print(f"File '{path}' created.")

    def write_file(self, path, data):
        if path not in self.fs["files"]:
            print("File does not exist.")
            return
        if "w" not in self.fs["files"][path]["permissions"]:
            print("Permission denied.")
            return

        file_entry = self.fs["files"][path]
        blocks_needed = (len(data) + BLOCK_SIZE - 1) // BLOCK_SIZE

        if len(self.fs["free_blocks"]) < blocks_needed:
            print("Not enough space.")
            return

        for blk in file_entry["blocks"]:
            self.fs["free_blocks"].append(blk)

        file_entry["blocks"] = []
        i = 0
        for _ in range(blocks_needed):
            block_id = self.fs["free_blocks"].pop(0)
            chunk = data[i:i + BLOCK_SIZE].encode('utf-8')
            self.disk[block_id * BLOCK_SIZE:(block_id + 1) * BLOCK_SIZE] = chunk
            file_entry["blocks"].append(block_id)
            i += BLOCK_SIZE

        file_entry["size"] = len(data)
        self.fs["superblock"]["used_blocks"] = TOTAL_BLOCKS - len(self.fs["free_blocks"])
        self.save_fs()
        with open(DISK_FILE, "wb") as f:
            f.write(self.disk)
        print(f"Data written to '{path}'.")

    def read_file(self, path):
        if path not in self.fs["files"]:
            print("File does not exist.")
            return
        if "r" not in self.fs["files"][path]["permissions"]:
            print("Permission denied.")
            return
        content = ""
        for blk in self.fs["files"][path]["blocks"]:
            content += self.disk[blk * BLOCK_SIZE:(blk + 1) * BLOCK_SIZE].decode('utf-8', errors="ignore")
        print(f"--- Contents of {path} ---")
        print(content.strip())

    def delete_file(self, path):
        if path not in self.fs["files"]:
            print("File does not exist.")
            return
        for blk in self.fs["files"][path]["blocks"]:
            self.fs["free_blocks"].append(blk)
        del self.fs["files"][path]
        self.fs["superblock"]["used_blocks"] = TOTAL_BLOCKS - len(self.fs["free_blocks"])
        self.save_fs()
        print(f"File '{path}' deleted.")

    def disk_usage(self):
        used = self.fs["superblock"]["used_blocks"]
        total = self.fs["superblock"]["total_blocks"]
        free = total - used
        print(f"Total blocks: {total}")
        print(f"Used blocks: {used}")
        print(f"Free blocks: {free}")
        print(f"Number of files: {len(self.fs['files'])}")

# Example usage
if __name__ == "__main__":
    fs = FileSystem()
    fs.create_file("/file1.txt", "rw")
    fs.write_file("/file1.txt", "This is a custom file system simulation.")
    fs.read_file("/file1.txt")
    fs.disk_usage()
    fs.delete_file("/file1.txt")
    fs.disk_usage()
