
import os
import json
from datetime import datetime

from collector import collect_evidence
from integrity import save_baseline, verify_file
from timeline import generate_timeline
from log_analyzer import analyze_log


def save_json(data, filename):
    os.makedirs("reports", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"\n[+] Report saved: {filename}")


def evidence_collection():
    folder = input("Folder to investigate [samples]: ").strip()
    folder = folder or "samples"

    evidence = collect_evidence(folder)

    if not evidence:
        print("[!] No evidence collected.")
        return

    report = {
        "investigation_time": datetime.now().astimezone().isoformat(),
        "source_folder": folder,
        "total_files": len(evidence),
        "files": evidence
    }

    filename = datetime.now().strftime(
        "reports/evidence_%Y%m%d_%H%M%S.json"
    )
    save_json(report, filename)
    print(f"[+] Files collected: {len(evidence)}")


def integrity_check():
    print("\n1. Save baseline")
    print("2. Verify file")

    choice = input("Choose (1/2): ").strip()
    path = input("Enter file path: ").strip()

    if choice == "1":
        save_baseline(path)
    elif choice == "2":
        verify_file(path)
    else:
        print("[!] Invalid choice.")


def timeline_report():
    folder = input("Folder to investigate [samples]: ").strip()
    folder = folder or "samples"

    events = generate_timeline(folder)

    if events:
        save_json(events, "reports/timeline.json")
        for event in events:
            print(
                event["modified_time"],
                "|",
                event["file"]
            )
    else:
        print("[!] No timeline events found.")


def log_investigation():
    path = input("Log file [samples/demo.log]: ").strip()
    path = path or "samples/demo.log"

    findings = analyze_log(path)

    if not os.path.isfile(path):
        print("[!] Log file not found.")
        return

    report = {
        "analysis_time": datetime.now().astimezone().isoformat(),
        "log_file": os.path.abspath(path),
        "total_findings": len(findings),
        "findings": findings
    }

    save_json(report, "reports/log_analysis.json")

    print(f"[+] Findings: {len(findings)}")


def main():
    while True:
        print("\n" + "=" * 44)
        print("     LINUX FORENSICS TOOLKIT")
        print("=" * 44)
        print("1. Collect File Evidence")
        print("2. Evidence Integrity Checker")
        print("3. Generate File Timeline")
        print("4. Analyze Log File")
        print("5. Exit")
        print("=" * 44)

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            evidence_collection()
        elif choice == "2":
            integrity_check()
        elif choice == "3":
            timeline_report()
        elif choice == "4":
            log_investigation()
        elif choice == "5":
            print("[+] Toolkit closed.")
            break
        else:
            print("[!] Invalid choice. Select 1-5.")


if __name__ == "__main__":
    main()
