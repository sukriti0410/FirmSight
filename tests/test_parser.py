from src.parser import analyze_log


def test_error_detection():

    sample_logs = [
        "[ERROR] DDR INIT FAILED"
    ]

    report = analyze_log(sample_logs)

    assert report["severity"] == "HIGH"


def test_warning_detection():

    sample_logs = [
        "[WARNING] Retry attempt failed"
    ]

    report = analyze_log(sample_logs)

    assert report["severity"] == "MEDIUM"


def test_ddr_detection():

    sample_logs = [
        "[ERROR] DDR INIT FAILED"
    ]

    report = analyze_log(sample_logs)

    assert report["subsystem"] == "DDR"