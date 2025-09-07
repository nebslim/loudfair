#!/usr/bin/env python3
"""
Check DNS records for loudfair.com to ensure proper email configuration
"""

import subprocess
import sys

def run_dig(record_type, domain, nameserver="8.8.8.8"):
    """Run dig command and return output"""
    try:
        cmd = ["dig", f"@{nameserver}", domain, record_type, "+short"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

def check_dns_records():
    """Check all email-related DNS records"""
    domain = "loudfair.com"
    
    print("=== DNS Record Check for loudfair.com ===\n")
    
    # Check MX records
    print("MX Records:")
    mx_records = run_dig("MX", domain)
    print(mx_records)
    print()
    
    # Check SPF record
    print("SPF Record:")
    txt_records = run_dig("TXT", domain)
    for line in txt_records.split('\n'):
        if 'spf1' in line:
            print(line)
    print()
    
    # Check DKIM records
    print("DKIM Records:")
    dkim_selectors = ["protonmail", "protonmail2", "protonmail3"]
    for selector in dkim_selectors:
        dkim_domain = f"{selector}._domainkey.{domain}"
        dkim_record = run_dig("CNAME", dkim_domain)
        if dkim_record:
            print(f"{selector}: {dkim_record}")
    print()
    
    # Check DMARC record
    print("DMARC Record:")
    dmarc_record = run_dig("TXT", f"_dmarc.{domain}")
    print(dmarc_record)
    print()
    
    # Check verification record
    print("Proton Verification Record:")
    for line in txt_records.split('\n'):
        if 'protonmail-verification' in line:
            print(line)

if __name__ == "__main__":
    # Check if dig is available
    try:
        subprocess.run(["which", "dig"], check=True, capture_output=True)
    except:
        print("Error: 'dig' command not found. Installing dnsutils...")
        print("On macOS, you can install it with: brew install bind")
        sys.exit(1)
    
    check_dns_records()
