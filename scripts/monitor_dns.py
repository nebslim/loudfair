#!/usr/bin/env python3
import subprocess
import time

def check_propagation():
    """Check if DNS changes have propagated"""
    
    print("Checking DNS propagation...")
    
    # Check DMARC
    dmarc = subprocess.run(["dig", "+short", "TXT", "_dmarc.loudfair.com"], 
                          capture_output=True, text=True).stdout.strip()
    
    if "p=none" in dmarc:
        print("✅ DMARC updated successfully!")
    else:
        print("⏳ DMARC not updated yet...")
    
    # Check SPF
    spf = subprocess.run(["dig", "+short", "TXT", "loudfair.com"], 
                        capture_output=True, text=True).stdout.strip()
    
    if "-all" in spf and "~all" not in spf:
        print("✅ SPF optimized!")
    else:
        print("⏳ SPF not optimized yet...")

if __name__ == "__main__":
    check_propagation()
