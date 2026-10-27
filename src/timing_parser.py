
from pathlib import Path


def parse_timing_report(report_path):
    """Extract timing metrics from the project's sample report format."""

    path = Path(report_path)

    if not path.is_file():
        raise FileNotFoundError(f"Timing report not found: {path}")

    metrics = {}

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if ":" not in line:
                continue

            key, value = line.split(":", maxsplit=1)
            key = key.strip().lower().replace(" ", "_")
            value = value.strip()

            if not value:
                raise ValueError(
                    f"Empty value at line {line_number}: {path.name}"
                )

            metrics[key] = value

    required = [
        "design",
        "clock_period",
        "worst_slack",
        "total_negative_slack",
        "violating_paths",
    ]

    missing = [key for key in required if key not in metrics]

    if missing:
        raise ValueError(
            f"Missing timing metrics in {path.name}: {', '.join(missing)}"
        )

    try:
        metrics["clock_period"] = float(metrics["clock_period"])
        metrics["worst_slack"] = float(metrics["worst_slack"])
        metrics["total_negative_slack"] = float(
            metrics["total_negative_slack"]
        )
        metrics["violating_paths"] = int(metrics["violating_paths"])
    except ValueError as exc:
        raise ValueError(
            f"Invalid numeric timing metric in {path.name}"
        ) from exc

    if metrics["clock_period"] <= 0:
        raise ValueError("Clock period must be positive.")

    if metrics["violating_paths"] < 0:
        raise ValueError("Violating path count cannot be negative.")

    metrics["timing_status"] = (
        "VIOLATIONS"
        if metrics["worst_slack"] < 0
        or metrics["violating_paths"] > 0
        else "PASS"
    )

    return metrics
