
import os
import json
from datetime import datetime


def generate_timeline(folder):
    events = []

    if not os.path.isdir(folder):
        print("[!] Folder not found:", folder)
        return events

    for root, dirs, files in os.walk(folder):
        dirs.sort()

        for filename in sorted(files):
            path = os.path.join(root, filename)

            try:
                info = os.stat(path)

                events.append({
                    "file": os.path.abspath(path),
                    "modified_time": datetime.fromtimestamp(
                        info.st_mtime
                    ).astimezone().isoformat(timespec="seconds"),
                    "size_bytes": info.st_size
                })

            except OSError as error:
                print(f"[!] Could not inspect {path}: {error}")

    events.sort(key=lambda event: event["modified_time"])

    return events


def main():
    print("=== FILE TIMELINE GENERATOR ===")

    folder = input("Folder to investigate [samples]: ").strip()
    if not folder:
        folder = "samples"

    events = generate_timeline(folder)

    if not events:
        print("[!] No file events found.")
        return

    os.makedirs("reports", exist_ok=True)

    report_path = "reports/timeline.json"

    with open(report_path, "w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)

    for event in events:
        print(
            f"{event['modified_time']} | "
            f"{event['file']} | "
            f"{event['size_bytes']} bytes"
        )

    print(f"\n[+] Timeline saved to {report_path}")


if __name__ == "__main__":
    main()
