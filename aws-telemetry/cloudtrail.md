# CloudTrail Notes

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