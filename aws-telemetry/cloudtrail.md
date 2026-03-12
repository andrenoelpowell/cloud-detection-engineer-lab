# CloudTrail Notes
Detection engineers constantly ask:
What logs exist?
What attacker behavior appears in those logs?
How can I detect it?

## What CloudTrail Does
CloudTrail records AWS API activity.

## Important Fields
- eventName
- eventTime
- userIdentity
- sourceIPAddress
- awsRegion

## Example Detection Idea
Alert on `CreateUser` or `AssumeRole` activity outside expected admin behavior.

## Example CloudTrail Events

### CreateUser
description:
Creates a new IAM user

Security Concern:
Attackers may create a new user to maintain persistence after gaining access.

Detection Idea:
Alert when CreateUser occurs outside normal admin activity

### AttachUserPolicy
Description:
Attaches a policy to an IAM user.

Security Concern:
Attackers may attach AdministratorAccess to escalate privileges.

Detection Idea:
Alert when AdministratorAccess policy is attached to a user.

### AssumeRole
Description:
Allows a user or service to assume an IAM role.

Security Concern:
Attackers often assume roles to move laterally across accounts.

Detection Idea:
Alert when AssumeRole occurs from unfamiliar IP addresses or regions.

---

### DeleteTrail
Description:
Deletes a CloudTrail logging trail.

Security Concern:
Attackers may disable logging to hide their activity.

Detection Idea:
Alert whenever DeleteTrail is executed.