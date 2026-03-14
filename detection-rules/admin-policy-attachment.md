# Detection: Administrator Policy Attachment

Log Source:
AWS CloudTrail

Event:
AttachUserPolicy

Description:
Alert when AdministratorAccess policy is attached to a user.

ATT&CK Technique:
T1098 – Account Manipulation

Why This Matters:
Attackers may grant themselves administrator privileges to control the AWS account.

Investigation Steps:
1. Identify the actor performing the action
2. Determine whether the change was approved
3. Review additional activity from the same user