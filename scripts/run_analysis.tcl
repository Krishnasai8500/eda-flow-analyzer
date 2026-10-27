
# Example EDA workflow automation script
# Demonstration only — does not invoke Synopsys tools.

set design_name "alu_core"
set report_dir "data/reports"

puts "Starting analysis for design: $design_name"

foreach report [list "timing.rpt" "area.rpt"] {
    set report_path [file join $report_dir $report]

    if {[file exists $report_path]} {
        puts "Found report: $report_path"
    } else {
        puts "WARNING: Missing report: $report_path"
    }
}

puts "EDA report validation complete."
