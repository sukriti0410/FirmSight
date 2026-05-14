import json
import sys
from pathlib import Path


REPORT_FILE = Path("reports/report.json")


def analyze_log(log_lines):

    severity = "LOW"
    subsystem = "UNKNOWN"

    error_count = 0
    warning_count = 0

    detected_issues = []

    for line in log_lines:

        if "DDR" in line:
            subsystem = "DDR"

        elif "UART" in line:
            subsystem = "UART"

        elif "MACsec" in line or "MKA" in line:
            subsystem = "MACsec"

        if "ERROR" in line:
            severity = "HIGH"
            error_count += 1
            detected_issues.append(line.strip())

        elif "WARNING" in line:
            if severity != "HIGH":
                severity = "MEDIUM"

            warning_count += 1
            detected_issues.append(line.strip())

    return {
        "analysis_status": "COMPLETED",
        "subsystem": subsystem,
        "severity": severity,
        "error_count": error_count,
        "warning_count": warning_count,
        "detected_issues": detected_issues,
        "summary": f"{subsystem} subsystem reported {error_count} error(s) and {warning_count} warning(s)."
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