
import csv
from pathlib import Path


def generate_summary(log_results, timing_metrics, area_metrics, output_dir):
    """Generate a combined engineering summary in CSV format."""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    csv_path = output_path / "eda_summary.csv"

    rows = [
        ("Log Files Processed", log_results["files_processed"]),
        ("Total Errors", len(log_results["errors"])),
        ("Total Warnings", len(log_results["warnings"])),
        ("Timing Design", timing_metrics["design"]),
        ("Clock Period", timing_metrics["clock_period"]),
        ("Worst Slack", timing_metrics["worst_slack"]),
        ("Total Negative Slack", timing_metrics["total_negative_slack"]),
        ("Violating Paths", timing_metrics["violating_paths"]),
        ("Timing Status", timing_metrics["timing_status"]),
        ("Area Design", area_metrics["design"]),
        ("Combinational Area", area_metrics["combinational_area"]),
        ("Sequential Area", area_metrics["sequential_area"]),
        ("Total Cell Area", area_metrics["total_cell_area"]),
        ("Area Components Match", area_metrics["area_components_match"]),
    ]

    with csv_path.open(
        "w", newline="", encoding="utf-8"
    ) as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Metric", "Value"])
        writer.writerows(rows)

    print(f"\nSummary report generated: {csv_path}")
    return csv_path
