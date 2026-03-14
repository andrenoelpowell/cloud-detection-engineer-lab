# Detection: S3 Bucket Policy Change

Log Source:
AWS CloudTrail

Event:
PutBucketPolicy

Description:
Alert when a bucket policy is modified.

ATT&CK Technique:
T1537 – Data Exfiltration

Why This Matters:
Attackers may modify bucket policies to expose sensitive data.

Investigation Steps:
1. Identify the user performing the action
2. Review the new bucket policy
3. Verify whether the change was authorized