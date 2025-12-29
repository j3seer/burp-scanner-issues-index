# Burp Scanner Issues Index
This repo will auto generate an excel sheet with all issues defined in Burp's Scanner

The list of issues in JSON is extracted from the Burp's community binary itself

The execl sheet currently uses the following structure (Example: OS Command Injection row)

|         name         | description | remediation |                                                                                                                                   references                                                                                                                                  |              CWE/CAPEC             |
|:--------------------:|:-----------:|:-----------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------:|
| OS command injection | ...         | ...         | https://capec.mitre.org/data/definitions/248.html      https://cwe.mitre.org/data/definitions/116.html      https://cwe.mitre.org/data/definitions/77.html      https://cwe.mitre.org/data/definitions/78.html      https://portswigger.net/web-security/os-command-injection | CAPEC-248, CWE-116, CWE-77, CWE-78 |
