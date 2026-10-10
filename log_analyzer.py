
import os
import json
from datetime import datetime


KEYWORDS = ["failed", "error", "warning", "denied", "invalid"]


def analyze_log(filepath):
    findings = []

    if not os.path.isfile(filepath):
        print("[!] Log file not found:", filepath)
        return findings

    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as file:
            for line_number, line in enumerate(file, start=1):
                matched = [
                    keyword for keyword in KEYWORDS
                    if keyword in line.lower()
                ]

                if matched:
                    findings.append({
                        "line_number": line_number,
                        "keywords": matched,
                        "log_entry": line.rstrip()
                    })

    except OSError as error:
        print(f"[!] Could not read log: {error}")

    return findings


def main():
    print("=" * 40)
    print("      LINUX LOG ANALYZER")
    print("=" * 40)

    filepath = input(
        "Enter log file path [samples/demo.log]: "
    ).strip()

    if not filepath:
        filepath = "samples/demo.log"

    findings = analyze_log(filepath)

    if not os.path.isfile(filepath):
        return

    os.makedirs("reports", exist_ok=True)

    report = {
        "analysis_time": datetime.now().astimezone().isoformat(),
        "log_file": os.path.abspath(filepath),
        "total_findings": len(findings),
        "findings": findings
    }

    with open(
        "reports/log_analysis.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(report, file, indent=4)

    for finding in findings:
        print(
            f"[!] Line {finding['line_number']} | "
            f"{', '.join(finding['keywords'])}"
        )
        print(f"    {finding['log_entry']}")

    print(f"\n[+] Findings: {len(findings)}")
    print("[+] Report saved: reports/log_analysis.json")


if __name__ == "__main__":
    main()
