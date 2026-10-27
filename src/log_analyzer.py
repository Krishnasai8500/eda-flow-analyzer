
from pathlib import Path
from collections import Counter
import re


def analyze_logs(log_directory):
    """Analyze log files and return errors, warnings and statistics."""

    directory = Path(log_directory)

    if not directory.exists():
        raise FileNotFoundError(
            f"Log directory does not exist: {directory}"
        )

    if not directory.is_dir():
        raise NotADirectoryError(
            f"Expected a directory: {directory}"
        )

    log_files = sorted(directory.glob("*.log"))

    results = {
        "files_processed": 0,
        "errors": [],
        "warnings": [],
        "error_counts": Counter(),
        "warning_counts": Counter(),
        "files_with_no_findings": [],
        "unreadable_files": [],
    }

    for file_path in log_files:
        try:
            with file_path.open(
                "r", encoding="utf-8", errors="replace"
            ) as file:
                lines = file.readlines()
        except OSError as exc:
            results["unreadable_files"].append(
                {"file": file_path.name, "reason": str(exc)}
            )
            continue

        results["files_processed"] += 1
        findings_in_file = 0

        for line_number, raw_line in enumerate(lines, start=1):
            message = raw_line.strip()

            if not message:
                continue

            match = re.match(
                r"^\[(ERROR|WARNING|INFO)\]\s*(.*)$",
                message,
                flags=re.IGNORECASE,
            )

            if not match:
                continue

            level = match.group(1).upper()
            detail = match.group(2).strip()

            if level not in ("ERROR", "WARNING"):
                continue

            finding = {
                "file": file_path.name,
                "line": line_number,
                "level": level,
                "message": detail,
            }

            if level == "ERROR":
                results["errors"].append(finding)
                results["error_counts"][detail] += 1
            else:
                results["warnings"].append(finding)
                results["warning_counts"][detail] += 1

            findings_in_file += 1

        if findings_in_file == 0:
            results["files_with_no_findings"].append(
                file_path.name
            )

    return results


def print_log_summary(results):
    """Print a readable summary of the analysis."""

    print("\n========== EDA LOG ANALYSIS ==========")
    print(f"Files processed : {results['files_processed']}")
    print(f"Total errors    : {len(results['errors'])}")
    print(f"Total warnings  : {len(results['warnings'])}")

    print("\n--- Errors ---")
    for item in results["errors"]:
        print(
            f"{item['file']}:{item['line']} | "
            f"{item['message']}"
        )

    print("\n--- Warnings ---")
    for item in results["warnings"]:
        print(
            f"{item['file']}:{item['line']} | "
            f"{item['message']}"
        )

    print("\n--- Repeated Errors ---")
    for message, count in results["error_counts"].most_common():
        if count > 1:
            print(f"{count} occurrences: {message}")

    print("\n--- Repeated Warnings ---")
    for message, count in results["warning_counts"].most_common():
        if count > 1:
            print(f"{count} occurrences: {message}")
