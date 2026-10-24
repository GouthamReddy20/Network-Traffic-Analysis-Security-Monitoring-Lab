import sys
from scapy.all import rdpcap, TCP, UDP, DNS, Raw, IP

def analyze_pcap(file_path):
    print(f"[*] Analyzing PCAP File: {file_path}\n" + "="*50)
    packets = rdpcap(file_path)
    
    syn_counts = {}
    dns_queries = set()
    unencrypted_http = []

    for pkt in packets:
        if pkt.haslayer(TCP) and pkt[TCP].flags == "S":
            src_ip = pkt[IP].src if pkt.haslayer('IP') else 'Unknown'
            syn_counts[src_ip] = syn_counts.get(src_ip, 0) + 1

        if pkt.haslayer(DNS) and pkt[DNS].qr == 0:
            query = pkt[DNS].qd.qname.decode('utf-8', errors='ignore')
            dns_queries.add(query)

        if pkt.haslayer(TCP) and (pkt[TCP].dport == 80 or pkt[TCP].sport == 80):
            if pkt.haslayer(Raw):
                payload = pkt[Raw].load.decode('utf-8', errors='ignore')
                if "GET" in payload or "POST" in payload:
                    unencrypted_http.append(payload.split('\r\n')[0])

    print(f"[+] Total Packets Analyzed: {len(packets)}")
    print(f"[+] Unique DNS Queries Captured ({len(dns_queries)}):")
    for q in list(dns_queries)[:5]:
        print(f"    - {q}")

    print(f"\n[!] Potential Port Scanners (SYN > 10):")
    for ip, count in syn_counts.items():
        if count > 10:
            print(f"    - {ip}: {count} SYN packets sent")

    print(f"\n[!] Cleartext HTTP Requests Detected ({len(unencrypted_http)}):")
    for http_req in unencrypted_http[:5]:
        print(f"    - {http_req}")

if __name__ == "__main__":
    pcap_file = sys.argv[1] if len(sys.argv) > 1 else "sample_capture.pcap"
    analyze_pcap(pcap_file)