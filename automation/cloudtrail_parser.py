import json
from pathlib import Path

log_file = Path("sample-cloudtrail.json")

if log_file.exists():
    with open(log_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    records = data.get("Records", [])
    for record in records:
        event_name = record.get("eventName")
        if event_name == "CreateUser":
            print("Suspicious event found:", event_name)
else:
    print("sample-cloudtrail.json not found yet")