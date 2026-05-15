import json


def test_ai_report_structure():
    with open("reports/ai_report.json", "r") as file:
        report = json.load(file)

    assert "summary" in report
    assert "severity" in report
    assert "root_cause" in report
    assert "debug_steps" in report


def test_ai_severity_value():
    with open("reports/ai_report.json", "r") as file:
        report = json.load(file)

    assert report["severity"] in ["HIGH", "MEDIUM", "LOW"]


def test_debug_steps_is_list():
    with open("reports/ai_report.json", "r") as file:
        report = json.load(file)

    assert isinstance(report["debug_steps"], list)
    assert len(report["debug_steps"]) > 0