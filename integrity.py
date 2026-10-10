
import hashlib
import json
import os


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def save_baseline(filepath, baseline_file="evidence/baseline.json"):
    if not os.path.isfile(filepath):
        print("[!] File not found:", filepath)
        return

    os.makedirs(os.path.dirname(baseline_file), exist_ok=True)

    baseline = {}

    if os.path.exists(baseline_file):
        with open(baseline_file, "r", encoding="utf-8") as file:
            baseline = json.load(file)

    baseline[os.path.abspath(filepath)] = calculate_hash(filepath)

    with open(baseline_file, "w", encoding="utf-8") as file:
        json.dump(baseline, file, indent=4)

    print("[+] Baseline hash saved successfully.")


def verify_file(filepath, baseline_file="evidence/baseline.json"):
    if not os.path.isfile(baseline_file):
        print("[!] Baseline not found. Save a baseline first.")
        return

    with open(baseline_file, "r", encoding="utf-8") as file:
        baseline = json.load(file)

    key = os.path.abspath(filepath)

    if key not in baseline:
        print("[!] File is not present in the baseline.")
        return

    if not os.path.isfile(filepath):
        print("[!] ALERT: File is missing!")
        return

    current_hash = calculate_hash(filepath)

    if current_hash == baseline[key]:
        print("[+] Integrity OK: File unchanged.")
    else:
        print("[!] ALERT: File content has changed!")


if __name__ == "__main__":
    print("=== Evidence Integrity Checker ===")
    print("1. Save baseline")
    print("2. Verify file")

    choice = input("Choose (1/2): ").strip()
    filepath = input("Enter file path: ").strip()

    if choice == "1":
        save_baseline(filepath)
    elif choice == "2":
        verify_file(filepath)
    else:
        print("[!] Invalid choice.")
