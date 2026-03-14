# MITRE ATT&CK Techniques Used in This Lab

## T1136 – Create Account
Attackers create new accounts to maintain persistence.

Example Detection
CreateUser CloudTrail event.

---

## T1098 – Account Manipulation
Attackers modify account permissions to escalate privileges.

Example Detection
AttachUserPolicy event.

---

## T1078 – Valid Accounts
Attackers use legitimate credentials to move laterally.

Example Detection
AssumeRole activity.

---

## T1562 – Impair Defenses
Attackers disable security controls or logging.

Example Detection
DeleteTrail event.
