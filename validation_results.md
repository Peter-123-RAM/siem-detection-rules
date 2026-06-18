# SIEM Detection Validation Results


## Credential Stuffing

ATT&CK:
T1110.004


True Positive:

25 failed logins from one IP targeting multiple users.

Result:

PASS - Alert generated


Benign:

Employee failed login twice.

Result:

PASS - No alert



## Web Shell

ATT&CK:
T1505.003


True Positive:

Apache spawned bash command execution.

Result:

PASS - Critical alert generated


Benign:

Normal PHP web request.

Result:

PASS - No alert



## OAuth Abuse

ATT&CK:
T1098


True Positive:

Unknown application requested Mail.ReadWrite permission.

Result:

PASS - Alert generated


Benign:

Approved Microsoft Teams application.

Result:

PASS - No alert



## Threshold Explanation

Credential stuffing:

20 attempts in 5 minutes chosen because normal users rarely generate this volume of failures.


Web shell:

Detection focuses on abnormal web server to shell process relationships.


OAuth:

Only high-risk permissions trigger alerts.
