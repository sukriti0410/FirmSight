import json
from unittest.mock import patch, Mock

from src.ai_analyzer import analyze_log_with_ai


def test_analyze_log_with_ai_mocked_response():
    fake_response = Mock()
    fake_response.output_text = json.dumps({
        "summary": "MACsec authentication failed.",
        "severity": "HIGH",
        "root_cause": "Possible CAK/CKN mismatch.",
        "debug_steps": [
            "Verify MACsec credentials",
            "Check MKA peer configuration"
        ]
    })

    with patch("src.ai_analyzer.client.responses.create", return_value=fake_response):
        result = analyze_log_with_ai("[ERROR] MKA authentication failed")

    assert result["summary"] == "MACsec authentication failed."
    assert result["severity"] == "HIGH"
    assert result["root_cause"] == "Possible CAK/CKN mismatch."
    assert isinstance(result["debug_steps"], list)
    assert len(result["debug_steps"]) > 0