## Prerequisites
- Enable Security auditing for logon events
- Collect Event IDs 4624 and 4625
- Collect RDP connection events (1149)

## What to look for
- LogonType=10 (RemoteInteractive)
- New source hosts for known admin accounts
- Multiple hosts accessed in short succession
