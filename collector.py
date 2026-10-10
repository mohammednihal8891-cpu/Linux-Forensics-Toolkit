
import os
import hashlib
import mimetypes
from datetime import datetime


def collect_evidence(folder):
    evidence = []

    if not os.path.isdir(folder):
        print("Error: Folder not found!")
        return evidence

    for root, dirs, files in os.walk(folder):
        dirs.sort()

        for filename in sorted(files):
            path = os.path.join(root, filename)

            try:
                info = os.stat(path)

                with open(path, "rb") as file:
                    file_hash = hashlib.sha256(file.read()).hexdigest()

                evidence.append({
                    "file_name": filename,
                    "path": os.path.abspath(path),
                    "size_bytes": info.st_size,
                    "file_type": (
                        mimetypes.guess_type(filename)[0]
                        or "unknown"
                    ),
                    "modified_time": datetime.fromtimestamp(
                        info.st_mtime
                    ).isoformat(timespec="seconds"),
                    "sha256": file_hash
                })

            except (OSError, PermissionError) as error:
                print(f"Could not read {path}: {error}")

    return evidence
