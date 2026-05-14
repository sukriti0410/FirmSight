import json
import sys
from pathlib import Path


REPORT_FILE = Path("reports/report.json")


def analyze_log(log_lines):
    severity = "LOW"
    subsystem = "UNKNOWN"

    for line in log_lines:
        if "DDR" in line:
            subsystem = "DDR"

        if "ERROR" in line:
            severity = "HIGH"
        elif "WARNING" in line and severity != "HIGH":
            severity = "MEDIUM"

    return {
        "subsystem": subsystem,
        "severity": severity
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 src/parser.py <log_file_path>")
        return

    log_file = Path(sys.argv[1])

    with open(log_file, "r") as file:
        log_lines = file.readlines()

    report = analyze_log(log_lines)

    with open(REPORT_FILE, "w") as file:
        json.dump(report, file, indent=4)

    print("FirmSight V1 Report Generated:")
    print(report)


if __name__ == "__main__":
    main()