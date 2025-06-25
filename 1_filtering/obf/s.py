# -*- coding: utf-8 -*-
import os
import time
from datetime import datetime

FOLDER = os.path.dirname(os.path.abspath(__file__))
LIMIT_GB = 38
LOG_FILE = os.path.join(FOLDER, "reolink_cleaner.log")

def log(msg):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        line = f"[{now}] {msg}\n"
        f.write(line)

def get_folder_size(start_path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            if f.lower().endswith('.mp4'):
                fp = os.path.join(dirpath, f)
                if os.path.isfile(fp):
                    total += os.path.getsize(fp)
    return total

def get_oldest_mp4(start_path):
    mp4_files = []
    for dirpath, _, filenames in os.walk(start_path):
        for f in filenames:
            if f.lower().endswith('.mp4'):
                full_path = os.path.join(dirpath, f)
                try:
                    mp4_files.append((full_path, os.path.getmtime(full_path)))
                except Exception:
                    pass
    mp4_files.sort(key=lambda x: x[1])  # sort by oldest
    return [f[0] for f in mp4_files]

def main():
    folder = FOLDER
    limit_bytes = LIMIT_GB * (1024 ** 3)

    current_size = get_folder_size(folder)
    log(f"Current size: {current_size / (1024 ** 3):.2f} GB")

    deleted_files = 0
    while current_size > limit_bytes:
        oldest_files = get_oldest_mp4(folder)
        if not oldest_files:
            log("No more MP4 files to delete.")
            break
        oldest = oldest_files[0]
        try:
            os.remove(oldest)
            log(f"Deleted: {oldest}")
            deleted_files += 1
        except Exception as e:
            log(f"Failed to delete {oldest}: {e}")
            break
        current_size = get_folder_size(folder)

    log(f"Cleanup finished. Total deleted: {deleted_files} files. Final size: {current_size / (1024 ** 3):.2f} GB")

if __name__ == '__main__':
    main()
