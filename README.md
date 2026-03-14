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
---

## Detection Engineering Approach

Each detection rule in this repository follows a structured workflow used by detection engineers.

### 1. Telemetry Source
Example:
- AWS CloudTrail logs recording IAM API activity

↓

### 2. Attacker Behavior
Example:
- Attacker creates a new IAM user to maintain persistence

↓

### 3. MITRE ATT&CK Technique
Example:
- T1136 – Create Account

↓

### 4. Detection Rule
Example:
- Alert when a CloudTrail event with `eventName = CreateUser` occurs

↓

### 5. Investigation Playbook
Example:
- Identify the actor who created the IAM user  
- Review the source IP address  
- Check permissions attached to the account  
- Verify whether the action was authorized
