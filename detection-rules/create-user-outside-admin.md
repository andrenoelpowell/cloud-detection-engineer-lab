# Detection: Unexpected IAM User Creation

Log Source:
AWS CloudTrail

Event:
CreateUser

Description:
Alert when a new IAM user is created outside expected administrator activity.

ATT&CK Technique:
T1136 – Create Account

Why This Matters:
Attackers may create new accounts to maintain persistence in the AWS environment.

Investigation Steps:
1. Identify who created the user
2. Review source IP address
3. Verify whether the action was authorized
4. Review permissions assigned to the new user