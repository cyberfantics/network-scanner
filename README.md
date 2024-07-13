# Network Scanner

This Python script performs network scanning using the Scapy library. It includes functions for both SYN scanning and DNS scanning. The user can specify the host and scan type (SYN or DNS) via input prompts.

## Features
- **SYN Scan:** Scans for open TCP ports on a specified host.
- **DNS Scan:** Checks for DNS servers on a specified host.
- **Exception Handling:** Ensures robustness and error reporting.
- **User-Friendly:** Input prompts and detailed output for clarity.

## Requirements
- **Python 3.x**
- **Scapy**

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/cyberfantics/network-scanner.git
    cd network-scanner
    ```

2. **Install Scapy:**
    ```sh
    pip install scapy
    ```

## Usage
1. **Run the script:**
    ```sh
    python portScan.py
    ```

2. **Enter the host:**
   When prompted, enter the IP address or hostname you want to scan.

3. **Select the scan type:**
   When prompted, enter either `syn` for a SYN scan or `dns` for a DNS scan.

4. **View the results:**
   The script will display the results of the selected scan.

## Example
```sh
Enter the host to scan: 192.168.1.1
Enter the scan type (syn/dns): syn
Starting SYN scan on 192.168.1.1
Open ports on 192.168.1.1: [80, 443]
```

## Contact
```sh
Created by Syed Mansoor ul Hassan Bukhari - [GitHub](https://github.com/cyberfantics)
```
