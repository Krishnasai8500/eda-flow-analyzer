
from src.log_analyzer import analyze_logs, print_log_summary
from src.timing_parser import parse_timing_report
from src.area_parser import parse_area_report
from src.report_generator import generate_summary


def main():
    log_results = analyze_logs("data/logs")
    timing_metrics = parse_timing_report("data/reports/timing.rpt")
    area_metrics = parse_area_report("data/reports/area.rpt")

    print_log_summary(log_results)

    print("\n========== TIMING SUMMARY ==========")
    print(f"Worst Slack: {timing_metrics['worst_slack']}")
    print(f"Violating Paths: {timing_metrics['violating_paths']}")
    print(f"Timing Status: {timing_metrics['timing_status']}")

    print("\n========== AREA SUMMARY ==========")
    print(f"Total Cell Area: {area_metrics['total_cell_area']}")
    print(
        "Area Components Match: "
        f"{area_metrics['area_components_match']}"
    )

    generate_summary(
        log_results,
        timing_metrics,
        area_metrics,
        "output",
    )


if __name__ == "__main__":
    main()
