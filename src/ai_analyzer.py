import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def read_log(log_file_path):
    with open(log_file_path, "r") as file:
        return file.read()


def analyze_log_with_ai(log_text):
    prompt = f"""
You are a firmware debugging assistant.

Analyze this firmware log.

Severity must be one of: HIGH, MEDIUM, LOW.

Return the response ONLY in valid JSON format.

Use this structure:

{{
  "summary": "...",
  "severity": "...",
  "root_cause": "...",
  "debug_steps": [
      "...",
      "..."
  ]
}}

Firmware Log:
{log_text}
"""

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    return json.loads(response.output_text)


def main():
    log_file = Path("logs/sample_log_macsec.txt")

    log_text = read_log(log_file)

    ai_report = analyze_log_with_ai(log_text)

    report_file = Path("reports/ai_report.json")

    with open(report_file, "w") as file:
        json.dump(ai_report, file, indent=4)

    print("FirmSight V2 AI Report Generated")


if __name__ == "__main__":
    main()