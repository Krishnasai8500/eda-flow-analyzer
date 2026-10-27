
from pathlib import Path


def parse_area_report(report_path):
    """Extract area metrics from the project's sample report format."""

    path = Path(report_path)

    if not path.is_file():
        raise FileNotFoundError(f"Area report not found: {path}")

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
        "combinational_area",
        "sequential_area",
        "total_cell_area",
    ]

    missing = [key for key in required if key not in metrics]

    if missing:
        raise ValueError(
            f"Missing area metrics in {path.name}: {', '.join(missing)}"
        )

    try:
        for key in (
            "combinational_area",
            "sequential_area",
            "total_cell_area",
        ):
            metrics[key] = float(metrics[key])
    except ValueError as exc:
        raise ValueError(
            f"Invalid numeric area metric in {path.name}"
        ) from exc

    if any(
        metrics[key] < 0
        for key in (
            "combinational_area",
            "sequential_area",
            "total_cell_area",
        )
    ):
        raise ValueError("Area values cannot be negative.")

    component_sum = (
        metrics["combinational_area"]
        + metrics["sequential_area"]
    )

    metrics["area_components_match"] = abs(
        component_sum - metrics["total_cell_area"]
    ) < 0.01

    return metrics
