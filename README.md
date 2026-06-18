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

## Example Sigma Detection Logic

Credential Stuffing:

```yaml
detection:

 selection:
  EventID: 4625
  Status: "0xC000006A"


 condition:

  selection | count(distinct TargetUserName) > 10 by IpAddress


 timeframe:

  5m

## Detection Execution Evidence

The detection rules were validated using a Python test harness that replayed malicious and benign security events.

Execution:

python tests/run_detection_tests.py


Expected Output:


Credential Stuffing TP:
True


Credential Stuffing FP:
False


Web Shell TP:
True


Web Shell FP:
False


OAuth TP:
True


OAuth FP:
False


The test confirms that each detection fires on attacker behaviour and remains quiet on benign activity.
