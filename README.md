# SIEM Detection Engineering Project


## Overview

A detection engineering project simulating attacker behaviour against an African fintech environment.


## Implemented Detections


| Detection | ATT&CK Technique | Purpose |
|-|-|-|
| Credential Stuffing | T1110.003 | Detect account takeover attempts |
| Web Shell | T1505.003 | Detect server persistence |
| OAuth Abuse | T1098 | Detect identity compromise |


## Testing

Each rule includes:

- True positive attacker simulation
- Benign test case
- Validation result
- Production tuning notes


## Tools

- Sigma detection logic
- MITRE ATT&CK mapping
- SIEM detection engineering principles


## AI Usage

AI was used to improve documentation structure, explain detection logic, and review clarity. The detection ideas and validation approach were developed by me.


## Validation Evidence

Each detection includes:

- Sigma YAML rule
- True positive attack simulation
- Benign activity test
- Expected SIEM result
- Production tuning notes


Validation approach:

Rules were tested against structured JSON event samples representing attacker and normal user behaviour.
