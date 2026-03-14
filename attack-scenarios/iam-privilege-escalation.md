# Attack Scenario: IAM Privilege Escalation

## Description

An attacker with access to a low-privilege IAM user attempts to escalate privileges by attaching an administrator policy.

## Attack Steps

1. Attacker compromises IAM user credentials
2. Attacker calls AttachUserPolicy API
3. AdministratorAccess policy is attached
4. Attacker gains full account permissions

## Cloud Telemetry

Log Source: AWS CloudTrail

Relevant Events:
AttachUserPolicy

Important Fields:
eventName
userIdentity
sourceIPAddress

## MITRE ATT&CK

T1098 – Account Manipulation

## Detection

Alert when:

eventName = AttachUserPolicy  
AND policy = AdministratorAccess

## Investigation

1. Identify the actor
2. Review the source IP address
3. Confirm whether the change was authorized
4. Remove the policy if malicious