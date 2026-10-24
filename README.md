# Network Traffic Analysis & Security Monitoring Lab

A blue-team portfolio project demonstrating packet inspection using Wireshark/Scapy and SIEM log monitoring rules using Splunk.

## Features
- **PCAP Packet Analyzer (`analyze_packets.py`)**: Parses network traffic captures to detect cleartext HTTP requests, DNS queries, and potential TCP SYN port scans.
- **SIEM Log Generator (`generate_auth_logs.py`)**: Simulates Windows Security Event Logs (Event IDs 4625, 4672, 4624) for threat hunting.
- **Splunk SPL Queries**: Custom search queries to detect brute-force attacks and privilege escalation.