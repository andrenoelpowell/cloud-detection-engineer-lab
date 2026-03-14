# Detection: Suspicious Role Assumption

## Log Source
AWS CloudTrail

## Detection Logic
Alert when an IAM role is assumed from an unfamiliar IP address or geographic region.

## Example Event
eventName: AssumeRole

## ATT&CK Mapping
T1078 - Valid Accounts

## Why This Matters
Attackers often assume roles after gaining access to an account to move laterally or escalate privileges.

## Investigation Steps
1. Identify the user performing the AssumeRole action
2. Review the source IP address
3. Determine if the role usage was expected
4. Review additional CloudTrail activity from the user
