# 🔍 Linux Forensics Toolkit

A beginner-friendly Digital Forensics project built using Python on Kali Linux.

## 📌 About the Project

Linux Forensics Toolkit helps users examine files and analyze log entries for basic digital forensic investigations. It collects file metadata, calculates SHA-256 hashes, checks file integrity, generates file timelines, and identifies selected keywords in log files.

## ✨ Features

- **File Evidence Collection** — Collects file names, paths, sizes, types, modification times, and SHA-256 hashes.
- **Evidence Integrity Checker** — Creates a hash baseline and checks whether a file has changed.
- **File Timeline Generator** — Creates a timeline based on file modification times.
- **Log File Analyzer** — Searches log files for keywords such as `failed`, `error`, `warning`, `denied`, and `invalid`.
- **JSON Reports** — Saves analysis results as JSON files.

## 🛠️ Technologies Used

- Python 3
- Kali Linux
- Linux Terminal
- JSON
- Git and GitHub

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/mohammednihal8891-cpu/linux-forensics-toolkit.git
   ```

2. Open the project folder:

   ```bash
   cd linux-forensics-toolkit
   ```

3. Run the program:

   ```bash
   python3 main.py
   ```

4. Select an option from the menu.

## 📁 Project Structure

```text
linux-forensics-toolkit/
├── main.py
├── collector.py
├── integrity.py
├── timeline.py
├── log_analyzer.py
├── evidence/
├── reports/
└── samples/
```

## 🎯 Learning Objectives

- Understand basic digital forensics.
- Learn file metadata collection.
- Verify file integrity using SHA-256.
- Generate file timelines.
- Perform basic log analysis using Python.

## ⚠️ Disclaimer

This project is intended for educational purposes and for analyzing files and logs that you are authorized to access.

## 👨‍💻 Author

**Mohammed Nihal**

Cybersecurity Student
