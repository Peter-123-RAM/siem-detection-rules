# SIEM Detection Validation Report


## Detection 1: Credential Stuffing

MITRE ATT&CK:
T1110.003 Password Spraying


TRUE POSITIVE:

Attacker performs 50 failed login attempts from one IP.

Expected:
Alert generated.

Result:
PASS


FALSE POSITIVE:

Normal user enters wrong password twice.

Expected:
No alert.

Result:
PASS



## Detection 2: Web Shell


MITRE ATT&CK:
T1505.003 Web Shell


TRUE POSITIVE:

Apache process launches bash.

Expected:
Critical alert.

Result:
PASS


FALSE POSITIVE:

Normal website request.

Expected:
No alert.

Result:
PASS



## Detection 3: OAuth Abuse


MITRE ATT&CK:
T1098 Account Manipulation


TRUE POSITIVE:

Unknown application receives admin permissions.

Expected:
Alert generated.

Result:
PASS


FALSE POSITIVE:

Approved company application.

Expected:
No alert.

Result:
PASS
