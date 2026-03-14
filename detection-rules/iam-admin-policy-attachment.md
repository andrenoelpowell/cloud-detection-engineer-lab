# Detection: IAM Admin Policy Attachment

## Log Source
AWS CloudTrail

## Detection Logic
Alert when an admin policy is attached to a user or role.

## Example Event
eventName: AttachUserPolicy

## ATT&CK Mapping
T1098 - Account Manipulation

## Why This Matters
Attackers often attach AdministratorAccess policies to gain full control of an AWS account.

## Investigation Steps
1. Identify the user who attached the policy
2. Determine if the action was authorized
3. Review the permissions granted
4. Check for other suspicious activity by the same user
