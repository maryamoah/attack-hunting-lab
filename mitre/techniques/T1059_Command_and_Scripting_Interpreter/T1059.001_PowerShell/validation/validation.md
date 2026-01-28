## Prerequisites
- Enable Security Event 4688 with command line
- Enable PowerShell Script Block Logging (4104)

## Test (lab only)
powershell.exe -EncodedCommand SQBFAFgA

Expected:
- 4688 contains -EncodedCommand / -enc
- 4104 logs script block content (if enabled)
