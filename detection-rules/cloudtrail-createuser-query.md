# Detection Query: IAM User Creation

Log Source:
AWS CloudTrail

Event:
CreateUser

Detection Logic:
Alert when CreateUser occurs outside expected administrator activity.

Example Query Logic:

eventSource = "iam.amazonaws.com"
AND eventName = "CreateUser"

Possible Investigation:

1. Identify the actor who created the user
2. Review source IP address
3. Check attached policies
4. Confirm authorization