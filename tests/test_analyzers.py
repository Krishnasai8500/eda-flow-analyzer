
import unittest

from src.log_analyzer import analyze_logs
from src.timing_parser import parse_timing_report
from src.area_parser import parse_area_report


class TestEDAAnalyzers(unittest.TestCase):

    def test_log_analysis(self):
        result = analyze_logs("data/logs")
        self.assertEqual(result["files_processed"], 2)
        self.assertEqual(len(result["errors"]), 3)
        self.assertEqual(len(result["warnings"]), 4)

    def test_timing_report(self):
        result = parse_timing_report("data/reports/timing.rpt")
        self.assertEqual(result["design"], "alu_core")
        self.assertEqual(result["timing_status"], "VIOLATIONS")
        self.assertEqual(result["violating_paths"], 3)

    def test_area_report(self):
        result = parse_area_report("data/reports/area.rpt")
        self.assertEqual(result["total_cell_area"], 200.0)
        self.assertTrue(result["area_components_match"])


if __name__ == "__main__":
    unittest.main()
