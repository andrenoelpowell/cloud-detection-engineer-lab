# Cloud Detection Engineer Lab

This repository tracks my path toward becoming a Cloud Detection Engineer.

## Focus Areas
- Cloud telemetry
- Detection engineering
- Security automation
- AWS lab development
- MITRE ATT&CK mapping

## Project Structure
- `notes/` daily learning notes
- `aws-telemetry/` cloud log source notes
- `detection-rules/` detection ideas and rules
- `automation/` Python scripts
- `lab/` cloud detection lab design
- `terraform/` infrastructure as code

## Detection Engineering Approach

Each detection rule in this repository follows a structured workflow used by detection engineers.

Telemetry Source
Example: AWS CloudTrail logs recording IAM API activity
        ↓
Attacker Behavior
Example: attacker creates new IAM user
        ↓
MITRE ATT&CK Technique
Example: T1136 – Create Account
        ↓
Detection Rule
Example: alert on CreateUser event
        ↓
Investigation Playbook
Example: review actor, IP, permissions
