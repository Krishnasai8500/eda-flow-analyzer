# EDA Flow Log Analyzer & Automation Toolkit

A Python-based utility for analyzing sample EDA logs, extracting timing and area metrics, validating report data, and generating a consolidated CSV summary.

## Features

- Scans log files and identifies errors and warnings.
- Reports source filenames and line numbers for findings.
- Identifies repeated error and warning messages.
- Parses timing metrics, including worst slack and violating paths.
- Parses area metrics and checks whether area components match the reported total.
- Generates a consolidated CSV summary.
- Includes a TCL example for report-file validation.
- Includes unit tests for core analysis functions.

## Technology Stack

- Python
- TCL (example workflow script)
- Linux/Unix command-line concepts
- CSV report generation
- Python unittest

## Project Structure

```text
eda-flow-analyzer/
├── main.py
├── src/
│   ├── log_analyzer.py
│   ├── timing_parser.py
│   ├── area_parser.py
│   └── report_generator.py
├── data/
│   ├── logs/
│   └── reports/
├── output/
├── scripts/
│   └── run_analysis.tcl
├── tests/
│   └── test_analyzers.py
├── README.md
└── .gitignore
```

## How to Run

Requires Python 3.

```bash
python main.py
```

The consolidated report is generated at `output/eda_summary.csv`.

Run automated tests:

```bash
python -m unittest discover -s tests -v
```

## Data and Scope

The included logs and reports are synthetic examples created to demonstrate parsing, validation, error reporting, and automation concepts. This project does not invoke Synopsys tools or claim to analyze real synthesis or physical-design runs.

## Future Improvements

- Support additional report formats.
- Add command-line arguments for input and output paths.
- Integrate with real EDA tools when an appropriate licensed environment is available.