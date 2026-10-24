# Network Traffic Analysis & Security Monitoring Lab

A comprehensive blue-team security portfolio project demonstrating network packet inspection using Python (`Scapy`) and SIEM threat hunting using Splunk Search Processing Language (SPL).

---

## 🏗️ Project Architecture & Structure

```text
network-security-monitoring-lab/
├── pcap_analysis/
│   └── analyze_packets.py       # Scapy-based network traffic parser
├── splunk_siem/
│   ├── generate_auth_logs.py    # Windows Event Log simulator
│   ├── failed_logins.spl        # SPL query for brute-force detection
│   └── privilege_escalation.spl # SPL query for privilege escalation hunting
└── README.md


(
echo # Network Traffic Analysis ^& Security Monitoring Lab
echo.
echo A comprehensive blue-team security portfolio project demonstrating network packet inspection using Python ^(`Scapy`^) and SIEM threat hunting using Splunk Search Processing Language ^(SPL^).
echo.
echo ## 🏗️ Project Architecture ^& Structure
echo ```text
echo network-security-monitoring-lab/
echo ├── pcap_analysis/
echo │   └── analyze_packets.py       # Scapy-based network traffic parser
echo ├── splunk_siem/
echo │   ├── generate_auth_logs.py    # Windows Event Log simulator
echo │   ├── failed_logins.spl        # SPL query for brute-force detection
echo │   └── privilege_escalation.spl # SPL query for privilege escalation hunting
echo └── README.md
echo ```
echo.
echo ## 🔍 Key Features ^& Capabilities
echo.
echo ### 1. PCAP Packet Analysis ^(`pcap_analysis/analyze_packets.py`^)
echo Parses raw network packet captures to detect potential indicators of compromise ^(IoCs^) and misconfigurations:
echo * **TCP SYN Scan Detection**: Identifies potential port scanning activity by tracking anomalous outbound or inbound SYN flag frequencies.
echo * **DNS Query Extraction**: Aggregates unique domain queries to inspect potential command-and-control ^(C2^) or data exfiltration lookups.
echo * **Cleartext Protocol Inspection**: Inspects HTTP packet payloads ^(`GET` / `POST`^) to flag unencrypted credential transmission or insecure communication channels.
echo.
echo ### 2. SIEM Log Generation ^(`splunk_siem/generate_auth_logs.py`^)
echo Simulates realistic Windows Active Directory security event logs to test monitoring pipelines:
echo * **Event ID 4625**: Audit Failures ^(Failed logins / bad password attempts^).
echo * **Event ID 4672**: Special Privileges Assigned ^(Privilege escalation tracking^).
echo * **Event ID 4624**: Successful logins via Kerberos authentication packages.
echo.
echo ### 3. Splunk SPL Detection Rules ^(`splunk_siem/`^)
echo Includes production-ready Search Processing Language queries designed for SIEM platforms:
echo * **Brute-Force Detection**: Aggregates failed authentication attempts ^(`EventID=4625`^) grouped by user and source IP over a sliding window.
echo * **Privilege Escalation Tracking**: Monitors high-privilege administrative assignments ^(`EventID=4672`^) outside of standard service accounts.
) > README.md