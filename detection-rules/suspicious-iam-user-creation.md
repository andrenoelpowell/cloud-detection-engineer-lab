# Detection: Suspicious IAM User Creation

## Log Source
CloudTrail

## Detection Logic
Alert when a `CreateUser` event occurs outside normal business hours.

## ATT&CK
T1136 - Create Account

## Investigation Steps
1. Identify the actor
2. Review source IP
3. Confirm whether the action was authorized
4. Review attached permissions