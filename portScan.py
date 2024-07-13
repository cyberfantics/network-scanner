# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 15:03:53 2024

@author: Mansoor
"""

from scapy.all import *
from concurrent.futures import ThreadPoolExecutor

ports = [25, 80, 53, 443, 445, 8080, 8443]

def syn_scan(host):
    try:
        print(f"Starting SYN scan on {host}")
        ans, unans = sr(IP(dst=host) / TCP(sport=5555, dport=ports, flags='S'), timeout=2, verbose=0)
        
        open_ports = []
        for s, r in ans:
            if s[TCP].dport == r[TCP].dport:
                open_ports.append(s[TCP].dport)
        
        if open_ports:
            print(f"Open ports on {host}: {open_ports}")
        else:
            print(f"No open ports found on {host}")
    
    except Exception as e:
        print(f"Error during SYN scan on {host}: {e}")

def dns_scan(host):
    try:
        print(f"Starting DNS scan on {host}")
        ans, unans = sr(IP(dst=host) / UDP(sport=5555, dport=53) / DNS(rd=1, qd=DNSQR(qname='google.com')), timeout=2, verbose=0)
        
        if ans:
            print(f"DNS Server at {host}")
        else:
            print(f"No DNS server found at {host}")
    
    except Exception as e:
        print(f"Error during DNS scan on {host}: {e}")

def main():
    host = input("Enter the host to scan: ")
    scan_type = input("Enter the scan type (syn/dns): ").lower()
    
    if scan_type == 'syn':
        syn_scan(host)
    elif scan_type == 'dns':
        dns_scan(host)
    else:
        print("Invalid scan type. Please enter 'syn' or 'dns'.")

if __name__ == "__main__":
    main()
