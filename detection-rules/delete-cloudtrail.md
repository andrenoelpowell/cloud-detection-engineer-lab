# Detection: CloudTrail Deletion

Log Source:
AWS CloudTrail

Event:
DeleteTrail

Description:
Alert whenever a CloudTrail logging trail is deleted.

ATT&CK Technique:
T1562 – Impair Defenses

Why This Matters:
Attackers may delete logging to hide malicious activity.

Investigation Steps:
1. Identify the user performing the action
2. Determine if the action was approved
3. Immediately verify logging is restored