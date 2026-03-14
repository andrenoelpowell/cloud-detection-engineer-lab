# Attack Scenario: CloudTrail Logging Disabled

## Description

An attacker attempts to disable logging to hide malicious activity.

## Attack Steps

1. Attacker gains access to AWS account
2. Attacker calls DeleteTrail or StopLogging
3. Logging visibility is removed

## Cloud Telemetry

Log Source: AWS CloudTrail

Relevant Events:
DeleteTrail  
StopLogging

## MITRE ATT&CK

T1562 – Impair Defenses

## Detection

Alert whenever:

eventName = DeleteTrail  
OR eventName = StopLogging

## Investigation

1. Identify the actor performing the action
2. Confirm whether the change was authorized
3. Restore logging immediately
4. Review previous CloudTrail activity