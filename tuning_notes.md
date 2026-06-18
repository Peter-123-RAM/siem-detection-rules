# Production Tuning Notes


## Credential Stuffing

Possible false positives:

- Shared office networks
- VPN gateways
- Password reset events


Improvements:

- Add threat intelligence IP checks
- Create user behaviour baselines
- Adjust thresholds


## Web Shell Detection

Possible false positives:

- Developers running scripts
- Legitimate automation


Improvements:

- Whitelist approved admin tools
- Monitor production servers only


## OAuth Detection

Possible false positives:

- New business applications
- SaaS onboarding


Improvements:

- Maintain approved OAuth application list
- Alert only risky permissions
